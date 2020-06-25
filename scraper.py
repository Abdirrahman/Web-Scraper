import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.co.uk/Sony-mirrorless-Real-time-Tracking-movie-shooting/dp/B07MWDP1VD/ref=sr_1_3?dchild=1&keywords=sony+a&qid=1592904644&sr=8-3'

headers = {"User-Agent": "google my user agent here "}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = (price[0:5])

    print(title.strip())
    print(converted_price)
    send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('xxxxxxxxxx@gmail.com', 'password')

    subject = 'Price of ..'
    body = 'Go Buy now.. '

    msg = f"Subject {subject}\n\n{body}"

    server.sendmail(
        'xxxxxxxxxxx@gmail.com',
        'YYYYYYYYYYYY@outlook.com',
        msg
    )
    print('Hey Email Sent')

    server.quit()

check_price()
