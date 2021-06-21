from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

driver = webdriver.Chrome("C:/Users/Lenovo/Desktop/chromedriver.exe")
driver.get("https://linkedin.com")

time.sleep(2)

username = driver.find_element_by_xpath("//input[@name = 'session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys("hashc0d3s@gmail.com")
password.send_keys("H@$hm!t3$")

time.sleep(2)

submit = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)
n_pages = 3
for n in range(1, n_pages):
    driver.get("https://www.linkedin.com/search/results/people/?origin=FACETED_SEARCH&page=" + str(n_pages))
    time.sleep(2)

    all_buttons = driver.find_elements_by_tag_name("button")
    message_buttons = [btn for btn in all_buttons if btn.text == "Message"]
    # message_buttons[0].click()
    for i in range(0, len(message_buttons)):
        driver.execute_script("arguments[0].click();", message_buttons[i])
        main_div = driver.find_element_by_xpath("//div[starts-with(@class, 'msg-form_msg-content-container')]")
        driver.execute_script("arguments[0].click();", main_div)

        paragraphs = driver.find_element_by_tag_name("p")


        all_span = driver.find_element_by_tag_name("span")
        all_span = [s for s in all_span if s.get_attribute("aria-hidden") == "true"]

        index = [*range(3, 23, 2)]

        greetings = ["Hello", "Hi", "Hey", "Ahoy", "Yo yo", "Sup"]
        all_names = []
        for j in index:
            name = all_span[j].text.split(" ")[0]
            all_names.append(name)
        greetings_index = random.randint(0, len(greetings) - 1)
        message = greetings[greetings_index] + " " + all_names[i] + ", nice to meet you"

        paragraphs[-5].send_keys("testing")
        time.sleep(2)
        submit = driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)

        close_button = driver.find_element_by_xpath("//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]").click()
        driver.execute_script("arguments[0].click();", close_button)
        time.sleep(2)


