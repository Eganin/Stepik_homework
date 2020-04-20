from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()

try:
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    # сообщение от сайта
    alert = browser.switch_to.alert
    # принимаем его
    alert.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    calc = lambda X: str(math.log(abs(12 * math.sin(int(X)))))
    y = calc(x)
    inputs = browser.find_element_by_id('answer')
    inputs.send_keys(y)

    butt_2 = browser.find_element_by_tag_name("button")
    butt_2.click()

except:
    time.sleep(10)
    browser.quit()

finally:
    time.sleep(10)
    browser.quit()
