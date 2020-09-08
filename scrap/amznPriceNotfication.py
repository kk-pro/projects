import requests
from bs4 import BeautifulSoup
import time




url = 'https://www.amazon.sa/%D9%81%D9%8A%D9%84%D9%8A%D8%A8%D8%B3-%D8%A7%D9%84%D9%8A%D9%88%D9%85%D9%8A%D8%A9-%D9%81%D9%8A%D9%84%D9%8A%D8%A8%D8%B3-%D8%A8%D9%84%D8%A7%D8%B3%D8%AA%D9%8A%D9%83-HD2581/dp/B01N7XJPG7?language=en_AE&pd_rd_r=c6e8ed3d-6670-4841-9bfd-622edffaaed0&pd_rd_w=gWmGj&pd_rd_wg=OV1Mg&pf_rd_p=18437e74-3151-49fe-9e94-6299574c2b88&pf_rd_r=XM4SW3WHHA2BC53W1JQW&ref_=pd_gw_unk'

headers = { "user-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
fin = True
def price_check():
    global fin
    event = "your event from ifttt"
    key = "your key form ifttt"
    page = requests.get(url,headers= headers)

    soup = BeautifulSoup(page.content,"lxml")

    title = soup.find(id = "productTitle").get_text(strip=True)
    price = soup.find(id="priceblock_ourprice").get_text(strip=True)
    converted_price = float(price[4:7])
    if converted_price < 117:
        send_webhook(event)
        fin = False



def send_webhook(event,key):
    webhook_url = f'https://maker.ifttt.com/trigger/{event}/with/key/{key}'
    requests.post(webhook_url)

try:
    while fin == True:
        price_check()
        time.sleep(10)
        print(fin)
except KeyboardInterrupt:
    exit()
