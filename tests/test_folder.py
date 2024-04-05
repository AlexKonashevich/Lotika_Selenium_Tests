import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from tests_runner import TestRunner

# Need to add id to buttons edit folder and delete folder
class TestFolder(TestRunner):
    def run_test(self):
        driver = self.driver
        self.create_auth_user(driver)
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button//span[contains(text(),'Папка')]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Новая папка')]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[contains(text(),'Попробовать бесплатно')]"))).click()
        time.sleep(3)
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button//span[contains(text(),'Папка')]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Новая папка')]"))).click()
        folder_name = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "// input[ @ placeholder = 'Название папки']")))
        folder_name.clear()
        folder_name.send_keys('TEST')
        folder_name.send_keys(Keys.ENTER)
        time.sleep(3)
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button//span[contains(text(),'TEST')]")))
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button//span[contains(text(),'TEST')]"))).click()
        # Need to add id to buttons edit folder and delete folder
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "svg"))).click()
        time.sleep(3)
        folder_rename = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//input[@name='folderName']")))
        folder_rename.send_keys('e2e_test')
        folder_rename.send_keys(Keys.ENTER)
        time.sleep(3)
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//h3[@class='sc-eqUAAy sc-fhOrUh jlFgkF jpxXZK']")))
        print('hhhh')
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[contains(text(),'Удалить все лоты')]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Да')]"))).click()
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[@class='sc-gsFSXq sc-jDGquE cTMarb cIjfas']")))
        # Need to add id to buttons edit folder and delete folder
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[2]//*[name()='svg']//*[name()='path' and contains(@d,'m11.055 6.')]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Да')]"))).click()
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Введите ключевое слово']")))
