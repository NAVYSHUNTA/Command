# Colabのフォルダをダウンロードする方法を以下で説明する。
# Web上で画像の収集処理を行い、その画像の入ったフォルダをダウンロードする方法を例に説明する。


# icrawlerのインストールを行う。
!pip install icrawler


# icrawlerのインポートを行う。
from icrawler.builtin import BingImageCrawler
# 収集した画像を./file-nameに保存する。
crawler = BingImageCrawler(storage = {"root_dir":"file-name"})
# キーワードと最大枚数を指定する。
crawler.crawl(keyword="モンスターエナジー　パイプラインパンチ", max_num = 100)

# 収集した画像が含まれるフォルダをzip化してダウンロードする。
!zip -r download-file-name.zip file-name
from google.colab import files
files.download("download-file-name.zip")
