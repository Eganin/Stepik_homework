from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим селекторы и вводим данные
    calc = lambda X: str(math.log(abs(12 * math.sin(int(X)))))
    x_element = browser.find_element_by_css_selector('img#treasure')
    value = x_element.get_attribute('valuex')
    result = calc(value)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(result)  # ввод данных
    butt_1 = browser.find_element_by_id("robotCheckbox")
    butt_1.click()
    butt_2 = browser.find_element_by_id('robotsRule')
    butt_2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()  # нажатие на атрибут

finally:
    time.sleep(30)
    browser.quit()
