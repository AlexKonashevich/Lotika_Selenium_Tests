import time
from decorators import count_calls
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


@count_calls
def test_authentication(driver, email, pas):
    try:
        email_input = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.NAME, 'email')))
        email_input.send_keys(Keys.CONTROL + 'A')
        email_input.send_keys(Keys.BACKSPACE)
        email_input.send_keys(email)
        pas_input = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.NAME, 'password')))
        pas_input.clear()
        pas_input.send_keys(pas)
        pas_input.send_keys(Keys.ENTER)
        # time.sleep(15)
        # WebDriverWait(driver, 30).until(
        #     ec.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/button'))).click()
        # WebDriverWait(driver, 30).until(
        #     ec.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div/button/span'))).click()
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Введите ключевое слово']")))
        # assert WebDriverWait(driver, 30).until(
        #     ec.presence_of_element_located((By.XPATH, "//button[@class='sc-fulCBj iAhrLK']")))
    except Exception as ex:
        return f"Test Auth Failed: {str(ex)}"
