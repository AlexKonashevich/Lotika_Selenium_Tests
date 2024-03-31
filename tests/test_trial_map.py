from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
from create_auth_user import create_auth_user
from tests_runner import TestRunner


class TestTrialMap(TestRunner):
    def run_test(self):
        create_auth_user(driver=self.driver)
        base_url = self.base_url
        driver = self.driver
        driver.get(url=base_url + 'search')
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Показать на карте')]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='sc-fhzFiK iSustV']"))).click()
        time.sleep(5)
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Показать на карте')]"))).click()
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div[2]')))
