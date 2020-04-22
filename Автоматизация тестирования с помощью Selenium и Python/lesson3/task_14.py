import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc():
    answer = math.log(int(time.time()))

    return answer


@pytest.mark.parametrize('params', ['236896', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
class Test_correction(object):
    def test_params(self, browser, params):
        link = f'https://stepik.org/lesson/{params}/step/1'
        browser.get(link)
        time.sleep(5)
        res = browser.find_element_by_tag_name('textarea')
        result = str(calc())
        res.send_keys(result)
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button.click()
        text = WebDriverWait(browser, 5).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, 'smart-hints__hint'), 'Correct!')
        )
        assert text.text == 'Correct!', 'FATAL ERROR'
