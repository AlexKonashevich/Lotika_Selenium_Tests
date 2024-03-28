from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from main import TestRunner


class TestTrialOffer(TestRunner):
    base_url = TestRunner.base_url
    driver = TestRunner.driver
    driver.get(url=base_url + 'search')
    WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Показать на карте')]"))).click()
    assert WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "//button[@class='sc-fhzFiK iSustV']")))
