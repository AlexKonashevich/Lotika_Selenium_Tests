import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from tests_runner import TestRunner


class TestAddComment(TestRunner):
    def run_test(self):
        base_url = self.base_url
        driver = self.driver
        self.create_auth_user(driver)
        time.sleep(3)
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//a[@data-hover-off="true"]'))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Добавить команду')]"))).click()
        time.sleep(3)
        team_name = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Введите название']")))
        team_name.send_keys('e2e_test')
        team_name.send_keys(Keys.ENTER)
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//a[contains(text(),'Торги')]"))).click()
        time.sleep(3)
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//a[@data-hover-off="true"]'))).click()
        time.sleep(3)
        write_comment = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")))
        write_comment.send_keys('e2e_test')
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[@data-el='send_btn']"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[contains(text(),'Попробовать бесплатно')]"))).click()
        time.sleep(3)
        write_comment = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")))
        write_comment.send_keys('e2e_test')
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[@data-el='send_btn']"))).click()
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'e2e_test')]")))
