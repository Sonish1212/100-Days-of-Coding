from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException

EMAIL = "sonishkhanal@gmail.com"
PASSWORD = "143Muller"

chrome_driver_path = "E:/from day 24 python/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(5)

sign_in = driver.find_element_by_class_name("nav__button-secondary")
sign_in.click()

email = driver.find_element_by_id("username")
email.send_keys(EMAIL)
password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)

sign_in = driver.find_element_by_css_selector(".login__form_action_container button")
sign_in.click()

time.sleep(5)

job_listing = driver.find_elements_by_css_selector(".job-card-container--clickable")
jobs = []

for job in job_listing:
    print("called")
    job.click()
    time.sleep(2)

    try:
        apply_for_job = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_for_job.click()
        time.sleep(3)

        mobile_number = driver.find_element_by_class_name("fb-single-line-text__input")
        if mobile_number.text == " ":
            mobile_number.send_keys("9866126473")

        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex Application, Skipped")
            continue
        else:
            submit_button.click()

        time.sleep(5)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        print("Complex Application, Skip")
        continue

time.sleep(5)
driver.quit()












