## BangumiAnimeDataset

Bangumi 动画数据集。

## 效果图

所有动画的评分：

![效果图 动画评分分布](https://github.com/NKID00/BangumiAnimeDataset/raw/main/Figure.png)

对任意动画的所有单次评分：

![效果图 动画单次评分分布](https://github.com/NKID00/BangumiAnimeDataset/raw/main/FigureScores.png)

以单个动画的 10 分评分数为横坐标，1 分评分数为纵坐标：

![效果图 动画 1分—10分 评分分布](https://github.com/NKID00/BangumiAnimeDataset/raw/main/Figure_1_10.png)

将上一张图放大：

![效果图 动画 1分—10分 评分分布 放大](https://github.com/NKID00/BangumiAnimeDataset/raw/main/Figure1_10_Zoom.png)

## 下载并预处理数据集

下载并预处理好的数据集可从 [Release 页面](https://github.com/NKID00/BangumiAnimeDataset/releases) 下载。

需要 `python>=3.6`。

安装依赖：

```sh
pip install -U aiohttp
```

运行程序：

```sh
$ python ./download_preprocess.py
```

数据存储在 `bgm_anime_dataset.json` 里。

## 绘制图表

需要 `python>=3.6`。

安装依赖：

```sh
pip install -U numpy matplotlib
```

运行程序：

```sh
$ python ./plot.py  # 动画评分分布
$ python ./plot_scores.py  # 动画单次评分分布
$ python ./plot_1_10.py  # 动画 1分—10分 评分分布
```

## 数据结构

`bgm_anime_dataset.json` 内的数据格式为 JSON，可解析为一个包含了 [Bangumi API 的 SubjectSmall 数据格式](https://bangumi.github.io/api/#model-SubjectSmall) 的所有存在评分及排名的动画列表。
