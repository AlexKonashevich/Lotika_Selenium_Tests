from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from main import TestRunner
class TestOpenSearch(TestRunner):
    def run_test(self):
        base_url = TestRunner.base_url
        driver = TestRunner.driver
        driver.get(url=base_url)
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div[1]/div/div/a/button/span'))).click()
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Введите ключевое слово']")))
