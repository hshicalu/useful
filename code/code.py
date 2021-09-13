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

# Colabでドライブをマウントするおまじない
from google.colab import drive
drive.mount('/content/drive')
# GPUを使うときのおまじない
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# xxx.ipynbからxxx.pyを生成するおまじない
jupyter nbconvert --to python xxx.ipynb