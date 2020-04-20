from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
try:

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока текст не станет нужным
    text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = browser.find_element_by_tag_name('button')
    button.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    calc = lambda X: str(math.log(abs(12 * math.sin(int(X)))))
    y = calc(x)
    inputs = browser.find_element_by_id('answer')
    inputs.send_keys(y)

    butt_2 = browser.find_element_by_xpath("//button[@type='submit']")
    butt_2.click()


finally:
    time.sleep(10)
    browser.quit()
