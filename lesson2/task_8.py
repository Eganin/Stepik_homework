from selenium import webdriver
import math
import time

link = 'http://SunInJuly.github.io/execute_script.html'

browser = webdriver.Chrome()

try:
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    calc = lambda X: str(math.log(abs(12 * math.sin(int(X)))))
    y = calc(x)
    print(y)
    inputs = browser.find_element_by_id('answer')
    inputs.send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id('robotsRule')
    # с помощью js кода централизируем кнопку
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    button = browser.find_element_by_tag_name("button")
    # с помощью js кода централизируем кнопку
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

except:
    time.sleep(10)
    browser.quit()

finally:
    time.sleep(10)
    browser.quit()