from asyncio import get_event_loop, sleep, current_task, TimeoutError
from collections import deque
from itertools import repeat, cycle
from operator import mul, itemgetter
from traceback import format_exception_only
from json import dump

from aiohttp import ClientSession, TCPConnector, ClientError


loop = get_event_loop()


def print_wide(*args, **kwargs):
    print('%-80s' % (' '.join(args)), **kwargs)

async def main():
    client = ClientSession(headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) '
        'Gecko/20100101 Firefox/90.0'
    }, connector=TCPConnector(limit=35))

    finished_tasks = deque()
    raw_data = deque()
    finished_count = accepted_count = skipped_count = error_count = 0
    error_http_count = 0

    async def download_one(index: int):
        nonlocal finished_tasks, client, raw_data
        nonlocal finished_count, accepted_count, skipped_count, error_count
        nonlocal error_http_count
        try:
            # print_wide(f'start @ {index}')
            exc = None
            for i in range(5):
                try:
                    r = await client.get(f'https://api.bgm.tv/subject/{index}')
                    r.raise_for_status()
                    data = await r.json()
                except (ClientError, TimeoutError) as e:
                    exc = e
                    continue
                else:
                    break
            else:
                print_wide(
                    '** {index} @', format_exception_only(type(exc), exc)[-1]
                )
                finished_count += 1
                finished_tasks.append(current_task(loop))
                error_count += 1
                return
            if 'code' in data and data['code'] >= 400:
                #print_wide(f'error http {data["code"]} @ {index}')
                finished_count += 1
                finished_tasks.append(current_task(loop))
                error_http_count += 1
                return
            if data['type'] != 2 or 'rating' not in data or 'rank' not in data:
                # print_wide(f'skip @ {index}')
                finished_count += 1
                finished_tasks.append(current_task(loop))
                skipped_count += 1
                return
            # print_wide(f'done @ {index}')
            raw_data.append(data)
            finished_count += 1
            finished_tasks.append(current_task(loop))
            accepted_count += 1
        except Exception as e:
            print_wide('** {index} @', format_exception_only(type(e), e)[-1])
            finished_count += 1
            finished_tasks.append(current_task(loop))
            error_count += 1
            raise

    print_wide('download ...')
    dots = cycle(map(mul, repeat('.', 3), range(1, 3+1)))
    for i in range(1, 343050+1):
        loop.create_task(download_one(i))
        if i - finished_count > 500:
            while i - finished_count > 100:
                while len(finished_tasks) > 0:
                    await finished_tasks.popleft()
                print_wide('%d/343050 %.2f%% (ac %d, sk %d, er %d, eh %d, '
                'i %d) %s' % (
                    finished_count,
                    finished_count / 343050 * 100,
                    accepted_count,
                    skipped_count,
                    error_count,
                    error_http_count,
                    i,
                    next(dots)
                ), end='\r')
                await sleep(0.1)

    while finished_count != 343050:
        while len(finished_tasks) > 0:
            await finished_tasks.popleft()
        print_wide('%d/343050 %.2f%% (ac %d, sk %d, er %d, eh %d) %s' % (
            finished_count,
            finished_count / 343050 * 100,
            accepted_count,
            skipped_count,
            error_count,
            error_http_count,
            next(dots)
        ), end='\r')
        await sleep(0.1)
    print()

    while len(finished_tasks) > 0:
        await finished_tasks.popleft()

    print_wide('sort ...')
    sorted_data = sorted(raw_data, key=itemgetter('id'))

    print_wide('save ...')
    with open('bgm_anime_dataset.json', 'w', encoding='utf8') as f:
        dump(sorted_data, f, ensure_ascii=False, separators=(',', ':'))
    
    await client.close()


if __name__ == '__main__':
    loop.run_until_complete(main())
