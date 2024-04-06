import requests
import pandas as pd


# プロキシが必要なら以下を追加
## START
proxies = {
    "http": "http://wwwproxy.kanazawa-it.ac.jp:8080",
    "https": "http://wwwproxy.kanazawa-it.ac.jp:8080",
}
## END

# データのロード
url = "https://www.statlab.co.jp/seminar/winequality-red2.csv"

urlData = requests.get(url, proxies=proxies).content

## いったん保存
with open("winequality-red2.csv", "wb") as f:
    f.write(urlData)

## データフレームとして読み込む
df = pd.read_csv("winequality-red2.csv")

# 前処理
