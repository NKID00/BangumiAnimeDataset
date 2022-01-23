from itertools import cycle
from json import load

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager

with open('bgm_anime_dataset.json', 'r', encoding='utf8') as f:
    data = load(f)

counts_1 = np.array(
    [[bangumi['rating']['count']['1']] for bangumi in data],
    dtype=np.int
)

counts_10 = np.array(
    [[bangumi['rating']['count']['10']] for bangumi in data],
    dtype=np.int
)

rc('font', family='Sarasa Gothic SC', size=14)

fig, ax = plt.subplots()
ax.scatter(counts_10, counts_1, c='#fca2ae')
ax.grid(True, axis='both')
ax.set_xlabel('10分评分数')
ax.set_ylabel('1分评分数')
ax.set_title(f'Bangumi 动画 1分—10分 评分分布')
fig.tight_layout()
plt.show()
