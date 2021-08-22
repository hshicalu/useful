

import MeCab
import re

tagger = MeCab.Tagger("-Owakati")

def make_wakati(sentence):
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

make_wakati("にじさんじMIX UP!! / にじさんじ みっくすあっぷ Season2 \
公式チャンネルで配信されたWeb番組[240]。 \
ぷちさんじ  \
公式チャンネルで配信の、動画の一部を紙芝居風にした切り抜き動画[240]。イラスト/動画はうちさ。当初はうちさの個人チャンネルで配信していたが、2019年11月より公式動画として配信。2020年1月に参加クリエイターを追加募集し、複数のクリエイターが参加している[241]。 \
にじさんじのハッピーアワー!! \
ニコニコ生放送のにじさんじ公式チャンネルで配信されているWeb番組[242] \
ヤシロ&ササキのレバガチャダイパン \
2020年4月10日より配信の3Dゲーム実況レギュラー番組。メインMCは社築、笹木咲。ナレーションはシェリン・バーガンディ。共同テレビジョン制作[243]。 \
ツキイチ！にじさんじ \
2020年5月23日より毎月23日配信の公式情報バラエティー番組。メインパーソナリティはJK組（月ノ美兎、樋口楓、静凛）[244]。")
