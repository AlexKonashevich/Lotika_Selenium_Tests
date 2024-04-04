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
            ec.presence_of_element_located((By.XPATH, "//button[@class='sc-kjNGdX fxavll']//*[name()='svg']"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='sc-fhzFiK iSustV']"))).click()
        time.sleep(5)
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Показать на карте')]"))).click()
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div[2]')))
