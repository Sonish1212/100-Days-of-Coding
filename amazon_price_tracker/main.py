import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/All-New-Toshiba-43LF421U21-43-inch-Smart/dp/B086VR9J8Q/ref=sr_1_1_sspa?dchild=1&keywords=TV&qid=1627390053&rnid=2661599011&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExVVhST1BNMThBNEJFJmVuY3J5cHRlZElkPUEwNjQ1NTk4OUI1RzlGVTZMQkhZJmVuY3J5cHRlZEFkSWQ9QTAwNTg1MTMyMVoyRlgwVkJGWURSJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

my_email = "loooksoook@gmail.com"
my_pass = "143Muller"

response = requests.get(url=URL, headers=header)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
items = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
item_price = float(items.getText().replace("$", ""))
print(item_price)
title = soup.find(id="productTitle").getText()
print(title)

if item_price < 300:
    message = f"{title} is now {item_price}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs="sonishkhanal@gmail.com",
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}")




