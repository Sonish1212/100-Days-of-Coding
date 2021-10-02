from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "loooksoook@gmail.com"
PASSWORD = "143Sonish"
chrome_driver_path = "E:/from day 24 python/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://tinder.com")

time.sleep(5)
login_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

time.sleep(5)
facebook_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button")
facebook_button.click()


time.sleep(10)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)


time.sleep(5)
email = driver.find_element_by_css_selector("#email_container input")
password = driver.find_element_by_xpath('//*[@id="pass"]')
email.send_keys(EMAIL)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
