import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from tests_runner import TestRunner


class TestBoards(TestRunner):
    def run_test(self):
        base_url = self.base_url
        driver = self.driver
        self.create_auth_user(driver)
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//a[contains(text(),'Задачи')]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//div[@tabindex='0']"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[contains(text(),'Попробовать бесплатно')]"))).click()
        time.sleep(3)
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//div[@tabindex='0']"))).click()
        board_name = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Имя новой доски']")))
        board_name.send_keys('e2e_test')
        board_name.send_keys(Keys.ENTER)
        driver.get(f'{base_url}/boards')
        assert WebDriverWait(driver, 30).until(ec.presence_of_element_located((
            By.XPATH, "//h4[contains(text(),'e2e_test')]"))), 'Ошибка создания доски'
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//h4[contains(text(),'e2e_test')]"))).click()
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]"))).click()
        column_name = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Имя колонки']")))
        column_name.send_keys('test')
        column_name.send_keys(Keys.ENTER)
        driver.get(f'{base_url}/boards')
        assert WebDriverWait(driver, 30).until(ec.presence_of_element_located((
            By.XPATH, "//h4[normalize-space()='e2e_test']"))), 'Ошибка создания колонки'
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((
            By.XPATH, "//h4[normalize-space()='e2e_test']"))).click()
        print('h')
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/*[name()='svg'][1]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//div[contains(text(),'Редактировать')]"))).click()
        column_rename = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Имя колонки']")))
        column_rename.send_keys(Keys.CONTROL + "a")
        column_rename.send_keys(Keys.DELETE)
        column_rename.send_keys('e2e_test')
        column_rename.send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 30).until(ec.presence_of_element_located((
            By.XPATH, "//h4[@title='e2e_test']"))), 'Ошибка переименования колонки'
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//div[contains(text(),'+ Добавить задачу')]"))).click()
        card_name = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Заголовок карточки']")))
        card_name.send_keys('TEST')
        card_name.send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 30).until(ec.presence_of_element_located((
            By.XPATH, "//div[@title='TEST']"))), 'Ошибка добавления задачи'
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/*[name()='svg'][1]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//div[contains(text(),'Удалить')]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Да')]"))).click()
        assert WebDriverWait(driver, 30).until(ec.presence_of_element_located((
            By.XPATH, "//*[name()='path' and contains(@d,'M8.6 3.8a.')]"))), 'Ошибка добавления задачи'
