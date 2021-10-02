import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = "E:/from day 24 python/chromedriver.exe"
SIMILAR_ACCOUNT = "Naruto Uzumaki"
USERNAME = "pythonininsta1212"
PASSWORD = "143Sonish"


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        login = self.driver.find_element_by_css_selector("._9GP1n    input")
        login.send_keys(USERNAME)
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        # save_info = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        # save_info.click()
        # time.sleep(3)
        notification = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]')
        notification.click()

    def find_followers(self):
        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(SIMILAR_ACCOUNT)
        search.send_keys(Keys.ENTER)
        time.sleep(3)
        similar_account = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        similar_account.click()
        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

    def follow(self):
        button_follow = self.driver.find_elements_by_css_selector("li button")
        for button in button_follow:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


insta_bot = InstaFollower(CHROME_DRIVER_PATH)
insta_bot.login()
insta_bot.find_followers()
time.sleep(2)
insta_bot.follow()

