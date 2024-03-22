import time

from decorators import count_calls
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from tempmail import EMail

options = webdriver.ChromeOptions()
TEMP_EMAIL = EMail()
DRIVER = webdriver.Chrome(options=options)


@count_calls
def test_registration():
    try:
        DRIVER.get(url='https://dev.lotika.ru/registration?registration_type=1')
        email_input = WebDriverWait(DRIVER, 30).until(
            ec.presence_of_element_located((By.NAME, 'email')))
        email_input.clear()
        email_input.send_keys(TEMP_EMAIL.address)
        name_input = DRIVER.find_element(By.NAME, 'nickname')
        name_input.clear()
        name_input.send_keys('TEST')
        name_input.send_keys(Keys.ENTER)
        assert WebDriverWait(DRIVER, 30).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='sc-dZoequ eWsqKP']")))
    except Exception as ex:
        return f"Test Auth Failed: {str(ex)}\n"


@count_calls
def test_authentication():
    try:
        msg = TEMP_EMAIL.wait_for_message(timeout=120)
        pas = msg.body
        pas_input = WebDriverWait(DRIVER, 30).until(
            ec.presence_of_element_located((By.NAME, 'password')))
        pas_input.clear()
        pas_input.send_keys(pas[2028:2036])
        pas_input.send_keys(Keys.ENTER)
        time.sleep(15)
        assert WebDriverWait(DRIVER, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='sc-fulCBj iAhrLK']")))
    except Exception as ex:
        return f"Test Auth Failed: {str(ex)}\n"


@count_calls
def test_open_search():
    try:
        WebDriverWait(DRIVER, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='sc-fulCBj iAhrLK']"))).click()
        assert WebDriverWait(DRIVER, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Показать на карте')]")))
    except Exception as ex:
        return f"Test Auth Failed: {str(ex)}\n"


@count_calls
def test_trial_offer():
    try:
        WebDriverWait(DRIVER, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Показать на карте')]"))).click()
        assert WebDriverWait(DRIVER, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='sc-fhzFiK iSustV']")))
    except Exception as ex:
        return f"Test Auth Failed: {str(ex)}\n"


@count_calls
def test_trial_accept():
    try:
        WebDriverWait(DRIVER, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='sc-fhzFiK iSustV']"))).click()
        WebDriverWait(DRIVER, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Показать на карте')]"))).click()
        assert WebDriverWait(DRIVER, 30).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div[2]/div[1]')))
    except Exception as ex:
        return f"Test Auth Failed: {str(ex)}\n"
    finally:
        DRIVER.close()
        DRIVER.quit()
