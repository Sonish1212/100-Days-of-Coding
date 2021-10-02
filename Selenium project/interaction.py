from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "E:/from day 24 python/chromedriver.exe"
F_NAME = "Sonish"
L_NAME = "Khanal"
EMAIL = "loooksoook@gmail.com"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element_by_name("fName")
f_name.send_keys(F_NAME)
f_name.send_keys(Keys.TAB)
l_name = driver.find_element_by_name("lName")
l_name.send_keys(L_NAME)
l_name.send_keys(Keys.TAB)
e_mail = driver.find_element_by_name("email")
e_mail.send_keys(EMAIL)
e_mail.send_keys(Keys.TAB)
button = driver.find_element_by_css_selector(".btn-block")
button.send_keys(Keys.ENTER)

