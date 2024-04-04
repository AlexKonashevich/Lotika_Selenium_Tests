from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from tempmail import EMail
import time

test_calls = []


class TestRunner:

    def __init__(self):
        self.base_url = 'https://dev.lotika.ru/'
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)

    def create_auth_user(self, driver):
        temp_email = EMail()
        base_url = self.base_url
        driver.get(url=f'{base_url}registration?registration_type=1')
        email_input = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.NAME, 'email')))
        email_input.clear()
        email_input.send_keys(temp_email.address)
        region_input = driver.find_element(By.ID, 'regionIds')
        region_input.clear()
        region_input.send_keys('Москва')
        time.sleep(3)
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((
            By.XPATH, "// li[ @ id = 'regionIds-option-0'] // div // div[1]"))).click()
        name_input = driver.find_element(By.NAME, 'nickname')
        name_input.clear()
        name_input.send_keys('e2e_test')
        name_input.send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='sc-dZoequ eWsqKP']")))
        msg = temp_email.wait_for_message(timeout=120)
        pas = msg.body
        pas_input = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.NAME, 'password')))
        pas_input.clear()
        pas_input.send_keys(pas[2028:2036])
        pas_input.send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Введите ключевое слово']")))

    def run_test(self):
        raise Exception('Method should be implemented')

    def run_test_task(self):
        test_calls.append(self.__class__.__name__)
        try:

            self.run_test()
        except Exception as err:
            print(f'error: {err}')
        finally:
            self.driver.close()
            self.driver.quit()
