import requests
import time
import json
from lxml import html

#ここは部員がIDとパスワードを入力するところ
with open("credidential.json", "r") as f:
    credidential = json.load(f)
params = {"mode":"login","id":credidential["id"],"pw":credidential["pass"]}

from lxml import html
with open("value.json", "r") as f:
    values = json.load(f)
r = requests.post("http://meidaifolk.sub.jp/domain/forum/patio.cgi",data=params)
html = html.fromstring(str(r.text))
topics = html.xpath('//table[@class="bbs-item"]/tr/td/a/text()')
topic = str(topics[0])
writers = html.xpath('//table[@class="bbs-item"]/tr/td[@class="td-b w12e"]/text()')
writer = str(writers[1])
urls = html.xpath('//table[@class="bbs-item"]/tr/td/a/@href')
url = str('http://meidaifolk.sub.jp/domain/forum/'+urls[0])
temp_values = {"value1": topic, "value2": writer, "value3": url}
if temp_values != values:
    file = open("value.json","w")
    json.dump(temp_values,file,ensure_ascii=False)
    requests.post(credidential["twitter_url"], data=temp_values)#twitter用
