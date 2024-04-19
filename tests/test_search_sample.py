import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from tests_runner import TestRunner


class TestSearchSample(TestRunner):
    def run_test(self):
        base_url = self.base_url
        driver = self.driver
        self.create_auth_user(driver)
        num = '1000000'
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Расширенный поиск')]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//div[@id='mui-component-select-categoryIds']"))).click()
        lot_type = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//li[contains(text(),'Недвижимость')]")))
        lot_type.click()
        lot_type.send_keys(Keys.ESCAPE)
        time.sleep(3)
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Стоимость')]"))).click()
        time.sleep(3)
        cost = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='до']")))
        cost.send_keys(num)
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Начать поиск')]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//div[@data-el='search_patterns']"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Сохранить текущий поиск')]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[contains(text(),'Попробовать бесплатно')]"))).click()
        time.sleep(3)
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//div[@data-el='search_patterns']"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Сохранить текущий поиск')]"))).click()
        sample = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//input[@name='selectedTemplate.name']")))
        sample.send_keys('e2e_test')
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Сохранить')]"))).click()
        res = WebDriverWait(driver, 30).until(ec.presence_of_element_located((
            By.XPATH, "//h4[@class='sc-dcJsrY sc-eTTeRg iQFFuG hOgSpT']"))).text
        driver.get(url=f'{base_url}/search')
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//div[@data-el='search_patterns']"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//li[@tabindex='-1']"))).click()
        assert WebDriverWait(driver, 30).until(ec.presence_of_element_located((
            By.XPATH, "//h4[@class='sc-dcJsrY sc-eTTeRg iQFFuG hOgSpT']"))).text == res, 'Ошибка шаблона поиска'
