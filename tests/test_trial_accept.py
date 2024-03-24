from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from decorators import count_calls
import time

@count_calls
def test_trial_accept(driver):
    try:
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='sc-fhzFiK iSustV']"))).click()
        time.sleep(5)
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Показать на карте')]"))).click()
        time.sleep(5)
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div[2]')))
    except Exception as ex:
        return f"Test Tr Acc Failed: {str(ex)}"
