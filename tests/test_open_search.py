from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from decorators import count_calls


@count_calls
def test_open_search(driver):
    driver.get(url='https://dev.lotika.ru')
    try:
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div[1]/div/div/a/button/span'))).click()
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Введите ключевое слово']")))
    except Exception as ex:
        return f"Test Search Failed: {str(ex)}"
