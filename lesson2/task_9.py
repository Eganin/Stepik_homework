import os
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/file_input.html'

browser = webdriver.Chrome()

try:
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'README.md')  # добавляем к этому пути имя файла

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('Eganin')  # ввод данных

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys('Ken')

    input3 = browser.find_element_by_name("email")
    input3.send_keys('KenEganin@gmail.com')

    file_button = browser.find_element_by_id("file")
    file_button.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()  # нажатие на атрибут

except:
    time.sleep(10)
    browser.quit()

finally:
    time.sleep(10)
    browser.quit()
