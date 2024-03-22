from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from decorators import count_calls


@count_calls
def test_open_search(driver):
    try:
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='sc-fulCBj iAhrLK']"))).click()
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Показать на карте')]")))
    except Exception as ex:
        return f"Test Auth Failed: {str(ex)}\n"
