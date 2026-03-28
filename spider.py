import requests


# 访问网站？
url = "https://randomuser.me/api/?results=3"
resp = requests.get(url)
# 爬取之后我已经获得了全部的数据，然后是判断网页码和编码数据python
if resp.status_code == 200:
    data_json = resp.json()  # requests库自带的json方法，直接把字符串转换成字典
    n = len(data_json["results"])
    for i in range(n + 1):
        print(
            data_json["results"][i]["name"],
            data_json["results"][i]["email"],
        )
