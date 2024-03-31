from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from tests.create_auth_user import create_auth_user
from tests_runner import TestRunner


class TestNewFolder(TestRunner):
    def run_test(self):
        create_auth_user(driver=self.driver)
        base_url = self.base_url
        driver = self.driver
        driver.get(url=base_url + 'search')
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Папка')]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='sc-fhzFiK iSustV']"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Новая папка')]"))).click()
        folder_name = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "// input[ @ placeholder = 'Название папки']")))
        folder_name.clear()
        folder_name.send_keys('TEST')
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Создать и добавить')]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Закрыть')]"))).click()
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[@class='sc-dhKdcB sc-lbJcrp gnnHMu gJmCFy']")))
