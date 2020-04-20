from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = ' http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим селекторы и вводим данные
    # находим числа
    num_1 = browser.find_element_by_id('num1')
    num_2 = browser.find_element_by_id('num2')
    calc = lambda X, y: str(int(X) + int(y))
    result = calc(num_1.text, num_2.text)

    # Нажатие на выпадающий список
    select = Select(browser.find_element_by_tag_name("select"))
    # ищем в списке значение чисел
    select.select_by_value(result)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()  # нажатие на атрибут

finally:
    time.sleep(30)
    browser.quit()
