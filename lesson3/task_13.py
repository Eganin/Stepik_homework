import time
import unittest
from selenium import webdriver


class TestAbs(unittest.TestCase):

    def main(self, base_url):
        link = base_url
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('div.first_block input.first')
        input1.send_keys('Ivan')

        input3 = browser.find_element_by_css_selector('div.first_block input.third')
        input3.send_keys('Petrov@mail.ru')

        input2 = browser.find_element_by_css_selector('div.first_block input.second')
        input2.send_keys('Petrov')

        # Отправляем заполненную форму
        time.sleep(5)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        return welcome_text

    def test_register1(self):
        url = 'http://suninjuly.github.io/registration1.html'
        result = self.main(url)
        self.assertEqual('Поздравляем! Вы успешно зарегистировались!', result)

    def test_register2(self):
        url = 'http://suninjuly.github.io/registration2.html'
        result = self.main(url)
        self.assertEqual('Поздравляем! Вы успешно зарегистировались!', result)


if __name__ == '__main__':
    unittest.main()
