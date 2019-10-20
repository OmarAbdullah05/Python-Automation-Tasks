import requests
from bs4 import BeautifulSoup

#start program
URL = 'https://www.amazon.com/Apple-MacBook-13-inch-display-dual-core/dp/B07JZYWCV1/ref=sr_1_1?keywords=macbook&qid=1562785624&s=gateway&sr=8-1'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = price[1:6]

    if(converted_price < '2,300'):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price > '2,300'):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', $KEY)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('$EMAIL', '$KEY')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.com/Apple-MacBook-2-5GHz-MGXC2LL-Refurbished/dp/B0784J8FXM/ref=sr_1_1?keywords=macbook+pro+2018+15+inch&qid=1562727744&s=gateway&sr=8-1'


    msg = """Subject: Price fell down!\n\nCheck the amazon

    Via me"""

    server.sendmail(
        '$From_Email',
        '$To_Email',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT')

    server.quit()



check_price()
