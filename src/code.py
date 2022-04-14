# mecabを用いた分かち書き
import MeCab
import re
tagger = MeCab.Tagger("-Owakati")
def wakati(sentence):
    # MeCabで分かち書き
    sentence = tagger.parse(sentence)
    # 半角全角英数字除去
    sentence = re.sub(r'[0-9０-９a-zA-Zａ-ｚＡ-Ｚ]+', " ", sentence)
    # 記号もろもろ除去
    sentence = re.sub(r'[\．_－―─！＠＃＄％＾＆\-‐|\\＊\“（）＿■×+α※÷⇒—●★☆〇◎◆▼◇△□(：〜～＋=)／*&^%$#@!~`){}［］…\[\]\"\'\”\’:;<>?＜＞〔〕〈〉？、。・,\./『』【】「」→←○《》≪≫\n\u3000]+', "", sentence)
    # スペースで区切って形態素の配列へ
    wakati = sentence.split(" ")
    # 空の要素は削除
    wakati = list(filter(("").__ne__, wakati))
    return wakati

# mecab-ipadic-NEologdで単語分かち書きをする場合
TAGGAR = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

# Colabでドライブをマウントするおまじない
from google.colab import drive
drive.mount('/content/drive')

# GPUを使うときのおまじない
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# xxx.ipynbからxxx.pyを生成するおまじない
jupyter nbconvert --to python xxx.ipynb

# 連番のフォルダを作成する
import os
for i in range(10):
    os.mkdir("./folder{}".format(i))

# 連番のファイルの作成 
import pathlib 
path = '***'
for i in range(10):
    file = pathlib.Path("./file{}.py".format(i))
    file.touch()

# スクレイピングの雛形
import requests
from bs4 import BeautifulSoup
response = requests.get('https://www.pasonatech.co.jp/')
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find('title').get_text()
print(title)

# Flaskの雛形
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<html><body><h1>sample</h1></body></html>'
if __name__ == '__main__':
    app.run()

# シードの設定
import random
random.seed(2022)

# TSVファイルの保存
df.to_csv(f'{file_name}.tsv', sep='\t', index=False)

# PythonからBQを操作する

## Load from BQ
import pandas as pd
query = "SELECT * \
FROM `{Pj_name}.{db_name}.{table_name}` \
"
df = pd.read_gbq(query, '{Pj_name}')

## Upload to BQ
df.to_gbq('{db_name}.{table_name}', project_id='{Pj_name}', if_exists='replace')

# PythonからMySQLを操作する

## Load from MySQL
import MySQLdb
connection = MySQLdb.connect(
    host='IP_address',
    user='root',
    passwd='passward',
    db='db_name')
cursor = connection.cursor()

## Edit in Python
cursor.execute("SELECT * FROM {db_name}.{table_name}")

cursor.execute("""insert into {table_name}
(id, title, content, created_at) VALUES
(0, 'aaa', 'Th', '1970-01-01 00:00:01.000000')
""")

## Print the results
rows = cursor.fetchall()
for row in rows:
    print(row)

# loggerの表示
from logging import basicConfig, getLogger
logFmt = "%(asctime)s %(levelname)s %(name)s :%(message)s"
level = 'INFO'
basicConfig(level=level, format=logFmt)
logger = getLogger()

