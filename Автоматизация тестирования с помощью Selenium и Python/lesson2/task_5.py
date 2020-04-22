from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим селекторы и вводим данные
    calc = lambda X: str(math.log(abs(12 * math.sin(int(X)))))
    x_element = browser.find_element_by_css_selector('span#input_value.nowrap')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)  # ввод данных
    butt_1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    butt_1.click()
    butt_2 = browser.find_element_by_id('robotsRule')
    butt_2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()  # нажатие на атрибут

finally:
    time.sleep(30)
    browser.quit()
