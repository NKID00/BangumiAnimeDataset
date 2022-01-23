from datetime import datetime
from collections import deque
from json import load

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

with open('bgm_anime_dataset.json', 'r', encoding='utf8') as f:
    data = load(f)

air_dates = [
    datetime.fromisoformat(bangumi['air_date']) for bangumi in data
    if bangumi['air_date'].startswith('20')
]

scores = np.array(
    [bangumi['rating']['score'] for bangumi in data
        if bangumi['air_date'].startswith('20')],
    dtype=np.float64
)

rc('font', family='Sarasa Gothic SC', size=14)

fig, ax = plt.subplots()
ax.scatter(air_dates, scores, c='#fca2ae')

scores = {}

for bangumi in data:
    if bangumi['air_date'].startswith('0'):
        continue
    year = datetime.fromisoformat(bangumi['air_date']).year
    if year < 2000:
        continue
    if year not in scores:
        scores[year] = deque()
    scores[year].append(bangumi['rating']['score'])

mean_scores = {}
median_scores = {}

for year, scores in scores.items():
    scores_arr = np.array([scores], dtype=np.float64)
    mean_scores[year] = np.mean(scores)
    median_scores[year] = np.median(scores)

mean_scores = list(zip(*sorted(mean_scores.items(), key=lambda x: x[0])))
mean_scores[0] = [datetime(y, 1, 1) for y in mean_scores[0]]
median_scores = list(zip(*sorted(median_scores.items(), key=lambda x: x[0])))
median_scores[0] = [datetime(y, 1, 1) for y in median_scores[0]]

ax.plot(*mean_scores, c='#06b0ff')
# ax.plot(*median_scores, c='#18ff52')

ax.yaxis.set_ticks([x / 2 for x in range(2, 20, 1)])
ax.xaxis.set_ticks([datetime(y, 1, 1) for y in range(2000, 2023, 2)])
ax.grid(True, axis='both')
ax.set_xlabel('放送时间')
ax.set_ylabel('评分')
ax.set_title('Bangumi 动画 放送时间—评分 分布（蓝线是每年平均分）')
fig.tight_layout()
plt.show()
