## BangumiAnimeDataset

Bangumi 动画数据集。

下载并预处理好的数据集可从 Release 页面下载。

## 手动下载并预处理数据集

1. 安装依赖：

   ```sh
   pip install -U aiohttp
   ```

2. 下载并预处理数据集：

   ```sh
   $ python ./download_preprocess.py
   ```

   数据存储在 `bgm_anime_dataset.json` 里。

## 绘制图表

```sh
$ python ./plot.py
```

## 数据结构

`bgm_anime_dataset.json` 内的数据格式为 JSON，可解析为一个包含了 Bangumi API 的 [SubjectSmall](https://bangumi.github.io/api/#model-SubjectSmall) 数据格式的所有存在评分及排名的动画列表。
