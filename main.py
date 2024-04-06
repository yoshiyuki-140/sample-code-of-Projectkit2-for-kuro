import requests


# プロキシが必要なら以下を追加
## START
proxies = {
    "http": "http://wwwproxy.kanazawa-it.ac.jp:8080",
    "https": "http://wwwproxy.kanazawa-it.ac.jp:8080",
}
## END

url = "https://www.statlab.co.jp/seminar/winequality-red2.csv"

urlData = requests.get(url, proxies=proxies).content

with open("winequality-red2.csv", "wb") as f:
    f.write(urlData)
