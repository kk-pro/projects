import requests
from bs4 import BeautifulSoup
import smtplib
from smtplib import SMTP


url = 'https://www.amazon.sa/%D9%81%D9%8A%D9%84%D9%8A%D8%A8%D8%B3-%D8%A7%D9%84%D9%8A%D9%88%D9%85%D9%8A%D8%A9-%D9%81%D9%8A%D9%84%D9%8A%D8%A8%D8%B3-%D8%A8%D9%84%D8%A7%D8%B3%D8%AA%D9%8A%D9%83-HD2581/dp/B01N7XJPG7?language=en_AE&pd_rd_r=c6e8ed3d-6670-4841-9bfd-622edffaaed0&pd_rd_w=gWmGj&pd_rd_wg=OV1Mg&pf_rd_p=18437e74-3151-49fe-9e94-6299574c2b88&pf_rd_r=XM4SW3WHHA2BC53W1JQW&ref_=pd_gw_unk'

headers = { "user-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

def price_check():
    page = requests.get(url,headers= headers)

    soup = BeautifulSoup(page.content,"lxml")

    title = soup.find(id = "productTitle").get_text(strip=True)
    price = soup.find(id="priceblock_ourprice").get_text(strip=True)
    converted_price = float(price[4:7])
    if converted_price < 117:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("email@gmail.com", "pass")

    subject = "the price goes down"
    body = "check the link https://www.amazon.sa/%D9%81%D9%8A%D9%84%D9%8A%D8%A8%D8%B3-%D8%A7%D9%84%D9%8A%D9%88%D9%85%D9%8A%D8%A9-%D9%81%D9%8A%D9%84%D9%8A%D8%A8%D8%B3-%D8%A8%D9%84%D8%A7%D8%B3%D8%AA%D9%8A%D9%83-HD2581/dp/B01N7XJPG7?language=en_AE&pd_rd_r=c6e8ed3d-6670-4841-9bfd-622edffaaed0&pd_rd_w=gWmGj&pd_rd_wg=OV1Mg&pf_rd_p=18437e74-3151-49fe-9e94-6299574c2b88&pf_rd_r=XM4SW3WHHA2BC53W1JQW&ref_=pd_gw_unk"

    msg = f"Subject: {subject} \n\n {body}"
    server.sendmail(
        'email@gmail.com',
        'email@gmail.com',
        msg
    )
    print("the massae has been sent")
    server.quit()


price_check()