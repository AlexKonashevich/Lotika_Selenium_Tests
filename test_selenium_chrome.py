import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tempmail import EMail

options = webdriver.ChromeOptions()
TEMP_EMAIL = EMail()
DRIVER = webdriver.Chrome(options=options)


def test_registration():
    try:
        DRIVER.get(url='https://dev.lotika.ru/registration?registration_type=1')
        email_input = DRIVER.find_element(By.NAME, 'email')
        email_input.clear()
        email_input.send_keys(TEMP_EMAIL.address)
        name_input = DRIVER.find_element(By.NAME, 'nickname')
        name_input.clear()
        name_input.send_keys('TEST')
        name_input.send_keys(Keys.ENTER)
        time.sleep(3)
        assert DRIVER.find_element(By.XPATH, "//div[@class='sc-dZoequ eWsqKP']")
    except Exception as ex:
        raise ex


def test_authentication():
    try:
        msg = TEMP_EMAIL.wait_for_message(timeout=120)
        pas = msg.body
        pas_input = DRIVER.find_element(By.NAME, 'password')
        pas_input.clear()
        pas_input.send_keys(pas[2028:2036])
        pas_input.send_keys(Keys.ENTER)
        time.sleep(3)
        assert DRIVER.find_element(By.XPATH, "//button[@class='sc-fulCBj iAhrLK']")
    except Exception as ex:
        raise ex


def test_open_search():
    try:
        DRIVER.find_element(By.XPATH, "//button[@class='sc-fulCBj iAhrLK']").click()
        time.sleep(3)
        assert DRIVER.find_element(By.XPATH, "//span[contains(text(),'Показать на карте')]")
    except Exception as ex:
        raise ex


def test_trial_offer():
    try:
        DRIVER.find_element(By.XPATH, "//span[contains(text(),'Показать на карте')]").click()
        time.sleep(3)
        assert DRIVER.find_element(By.XPATH, "//button[@class='sc-fhzFiK iSustV']")
    except Exception as ex:
        raise ex


def test_trial_accept():
    try:
        DRIVER.find_element(By.XPATH, "//button[@class='sc-fhzFiK iSustV']").click()
        time.sleep(3)
        DRIVER.find_element(By.XPATH, "//span[contains(text(),'Показать на карте')]").click()
        time.sleep(3)
        assert DRIVER.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div[2]/div[1]')
    except Exception as ex:
        raise ex
    finally:
        DRIVER.close()
        DRIVER.quit()
