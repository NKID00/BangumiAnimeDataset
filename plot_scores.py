from itertools import cycle
from json import load

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

with open('bgm_anime_dataset.json', 'r', encoding='utf8') as f:
    data = load(f)

counts = np.array(
    [[bangumi['rating']['count'][str(i)] for i in range(1, 10+1)] for bangumi in data],
    dtype=np.int
)
counts = np.array([counts[:,i].sum() for i in range(10)], dtype=np.int)

total = counts.sum()
mean = sum(counts[i] * (i+1) for i in range(10)) / total

rc('font', family='FZZhunYuan-M02', size=14)

fig, ax = plt.subplots()
for i, c in zip(range(10), cycle(('#fca2ae', '#f6c2d0'))):
    bar = ax.bar(i + 1, counts[i], width=0.8, color=c)
    ax.bar_label(bar, [counts[i]])
ax.annotate(
    '平均：%.3f' % (mean),
    (mean, 0),
    xycoords='data', xytext=(0.63, -0.12), textcoords='axes fraction',
    arrowprops={'arrowstyle': '->'}
)
ax.grid(True, axis='y')
ax.set_xticks(np.arange(0, 10 + 0.1, 1, dtype=np.int))
ax.set_xlabel('评分')
ax.set_yticks(np.arange(0, 2000000, 300000, dtype=np.int))
ax.set_yticklabels(['0'] + list(map(
    lambda n: f'{n//10000:d}w',
    np.arange(0, 2000000, 300000, dtype=np.int)[1:]
)))
ax.set_ylabel('评分数')
ax.set_title(f'Bangumi 动画单次评分分布    总计{total}次评分')
fig.tight_layout()
plt.show()