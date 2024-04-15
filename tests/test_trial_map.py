from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
from tests_runner import TestRunner


class TestTrialMap(TestRunner):
    def run_test(self):
        driver = self.driver
        self.create_auth_user(driver)
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Показать на карте')]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[contains(text(),'Попробовать бесплатно')]"))).click()
        time.sleep(3)
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Показать на карте')]"))).click()
        time.sleep(5)
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[@class='show-full-card']"))), 'Ошибка открытия карты'
