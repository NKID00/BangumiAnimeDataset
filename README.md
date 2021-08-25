## BangumiAnimeDataset

Bangumi 动画数据集。

![效果图](https://github.com/NKID00/BangumiAnimeDataset/raw/main/Figure.png)

下载并预处理好的数据集可从 [Release 页面](https://github.com/NKID00/BangumiAnimeDataset/releases) 下载。

## 下载并预处理数据集

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
$ python ./plot.py
```

## 数据结构

`bgm_anime_dataset.json` 内的数据格式为 JSON，可解析为一个包含了 [Bangumi API 的 SubjectSmall 数据格式](https://bangumi.github.io/api/#model-SubjectSmall) 的所有存在评分及排名的动画列表。
