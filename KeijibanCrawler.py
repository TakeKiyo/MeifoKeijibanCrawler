import requests
import schedule
import time
import json

params = {"mode":"login","id":"","pw":""}

def job():
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
        requests.post("https://maker.ifttt.com/trigger/IFTTTのプロジェクト名/with/key/    ",data=temp_values)

schedule.every(10).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)







