from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def test_folder_new(driver):
    try:
        driver.get(url='https://dev.lotika.ru/search')
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Новая папка')]"))).click()
        folder_name = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "// input[ @ placeholder = 'Название папки']")))
        folder_name.clear()
        folder_name.send_keys('TEST')
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Создать и добавить')]"))).click()
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'Закрыть')]"))).click()
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[@class='sc-dhKdcB sc-lbJcrp gnnHMu gJmCFy']")))
    except Exception as ex:
        return f"Test Folder New Failed: {str(ex)}"
