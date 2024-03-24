from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from tempmail import EMail
from decorators import count_calls


@count_calls
def test_registration(driver):
    try:
        temp_email = EMail()
        driver.get(url='https://dev.lotika.ru/registration?registration_type=1')
        email_input = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.NAME, 'email')))
        email_input.clear()
        email_input.send_keys(temp_email.address)
        name_input = driver.find_element(By.NAME, 'nickname')
        name_input.clear()
        name_input.send_keys('TEST')
        name_input.send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='sc-dZoequ eWsqKP']")))
    except Exception as ex:
        return f"Test Reg Failed: {str(ex)}"
    else:
        msg = temp_email.wait_for_message(timeout=120)
        pas = msg.body
        return temp_email.address, pas[2028:2036]
