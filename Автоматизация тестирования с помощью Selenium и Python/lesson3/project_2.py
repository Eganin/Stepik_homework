import time
from selenium.webdriver.support import expected_conditions as EC


class Test_button(object):
    def test_button_localization(self, browser):
        link = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        result = browser.find_element_by_xpath("//button[@type='submit']")
        # проверка кнопки
        assert EC.visibility_of(result), 'missing'
        print('Result:' + str(result.text))
        time.sleep(10)
