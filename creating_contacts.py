from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/Lenovo/Desktop/chromedriver.exe")
driver.get('https://www.linkedin.com')
time.sleep(2)

username = driver.find_element_by_xpath("//input[@name = 'session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys("hashc0d3s@gmail.com")
password.send_keys("H@$hm!t3$")

submit = driver.find_element_by_xpath("//button[@type = 'submit']").click()
n_pages = 10
for n in range(1, n_pages):
    driver.get("https://www.linkedin.com/search/results/people/?origin=FACETED_SEARCH&page=" + str(n_pages))

    all_buttons = driver.find_elements_by_tag_name("button")
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

    for btn in connect_buttons:
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(2)
        send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
        driver.execute_script("arguments[0].click();", send)
        time.sleep(2)
        close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
        driver.execute_script("arguments[0].click();", close)
        time.sleep(2)