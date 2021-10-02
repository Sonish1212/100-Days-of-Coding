import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D'
CHROME_DRIVER_PATH = "E:/from day 24 python/chromedriver.exe"
FORM_URL = "https://forms.gle/S9G1DzqBcQGunb3H6"
header = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "upgrade-insecure-requests": '1'
}

response = requests.get(url=URL, headers=header)
zillow_page = response.text
# print(zillow_page)

soup = BeautifulSoup(zillow_page, 'html.parser')

house_links = []
house_address = []
link = soup.find_all(name="a", class_="list-card-link list-card-link-top-margin")
for links in link:
    house_links.append(links.get('href'))

for address in link:
    house_address.append(address.text)

# print(house_address)
# print(house_links)
house_price = []
price = soup.find_all(name='div', class_='list-card-price')
for prices in price:
    cost = prices.text
    split_cost = cost.split("/")[0]
    some_other = split_cost.split('+')[0]
    house_price.append(some_other)

print(house_price)
# Selenium part

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(url=FORM_URL)
time.sleep(3)
i = 0
j = 0
for hl in house_links:
    question_one = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    question_one.send_keys(house_address[i])
    i += 1
    question_two = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    question_two.send_keys(house_price[j])
    j += 1
    question_three = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    question_three.send_keys(hl)
    time.sleep(2)
    button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    button.click()
    time.sleep(3)
    again_form = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    again_form.click()
    time.sleep(3)


