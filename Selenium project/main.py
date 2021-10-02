from selenium import webdriver
chrome_driver_path = "E:/from day 24 python/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

date = driver.find_elements_by_css_selector(".event-widget time")
date_list = [dates.text for dates in date]
print(date_list)
event = driver.find_elements_by_css_selector(".event-widget li a")
event_list = [events.text for events in event]
print(event_list)
events = {}
for n in range(len(date_list)):
    events[n] = {
        "date": date[n].text,
        "event": event[n].text
    }
print(events)


driver.close()


