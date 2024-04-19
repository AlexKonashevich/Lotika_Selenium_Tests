import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from tests_runner import TestRunner


# Need ID rename button

class TestTeam(TestRunner):
    def run_test(self):
        driver = self.driver
        self.create_auth_user(driver)
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'e2e_test')]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Команда')]"))).click()
        team_name = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Введите название']")))
        team_name.send_keys('TEST')
        team_name.send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//h3[contains(text(),'TEST')]"))), 'Ошибка создания команды'
        time.sleep(3)
        # Need ID rename button
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, ""))).click()
        team_rename = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Введите название']")))
        team_rename.send_keys(Keys.CONTROL + "a")
        team_rename.send_keys(Keys.DELETE)
        team_rename.send_keys('e2e_test')
        team_rename.send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 30).until(ec.presence_of_element_located((
            By.XPATH, "//h3[contains(text(),'e2e_test')]"))), 'Ошибка переименования команды'
