from itertools import cycle
from json import load

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

with open('bgm_anime_dataset.json', 'r', encoding='utf8') as f:
    data = load(f)

scores = np.array(
    [bangumi['rating']['score'] for bangumi in data],
    dtype=np.float64
)

count = scores.size
mean = np.mean(scores, dtype=np.float64)
median = np.median(scores)
min_score = np.min(scores)
max_score = np.max(scores)

n, bins = np.histogram(scores, bins=np.arange(-0.05, 10.05, 0.1))
hist = np.vstack((bins[:-1] + 0.05, n))

for i in range(hist.shape[1]):
    print('%.1f %3d' % (hist[0, i], hist[1, i]))

rc('font', family='FZZhunYuan-M02', size=14)

fig, ax = plt.subplots()
for i, c in zip(range(20), cycle(('#fca2ae', '#f6c2d0'))):
    ax.bar(hist[0, i*5:i*5+5], hist[1, i*5:i*5+5], width=0.05, color=c)
ax.annotate(
    '最高：%d @ %.1f' % (hist[1, 66], hist[0, 66]),
    (hist[0, 66], hist[1, 66]),
    xycoords='data', xytext=(0.25, 0.56), textcoords='axes fraction',
    arrowprops={'arrowstyle': '->'}
)
ax.annotate(
    '局部最低：%d @ %.1f' % (hist[1, 69], hist[0, 69]),
    (hist[0, 69], hist[1, 69]),
    xycoords='data', xytext=(0.25, 0.43), textcoords='axes fraction',
    arrowprops={'arrowstyle': '->'}
)
ax.annotate(
    '平均：%.3f' % (mean),
    (mean, 0),
    xycoords='data', xytext=(0.58, -0.12), textcoords='axes fraction',
    arrowprops={'arrowstyle': '->'}
)
ax.annotate(
    '中位：%.1f' % (median),
    (median, 0),
    xycoords='data', xytext=(0.68, -0.12), textcoords='axes fraction',
    arrowprops={'arrowstyle': '->'}
)
ax.annotate(
    '最低：%.1f' % (min_score),
    (min_score, 0),
    xycoords='data', xytext=(0.125, -0.12), textcoords='axes fraction',
    arrowprops={'arrowstyle': '->'}
)
ax.annotate(
    '最高：%.1f' % (max_score),
    (max_score, 0),
    xycoords='data', xytext=(0.87, -0.12), textcoords='axes fraction',
    arrowprops={'arrowstyle': '->'}
)
ax.grid(True, axis='y')
ax.set_xticks(np.arange(0, 10 + 0.1, 0.5))
ax.set_xlabel('评分')
ax.set_ylabel('动画数')
ax.set_title(f'Bangumi 动画评分分布    总计{count}部')
fig.tight_layout()
plt.show()