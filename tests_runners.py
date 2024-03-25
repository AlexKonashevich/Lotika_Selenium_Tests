from selenium import webdriver
from tests import test_registration
from tests import test_authentication
from tests import test_open_search
from tests import test_trial_offer
from tests import test_trial_accept


def all_tests_runner(repeat_tests=1):
    options = webdriver.ChromeOptions()
    error_logs = []
    for num in range(repeat_tests):
        driver = webdriver.Chrome(options=options)
        search = test_open_search.test_open_search(driver)
        if search[0] is not None:
            error_logs.append(search[0])
        reg = test_registration.test_registration(driver)
        if len(reg[0]) > 1:
            email = reg[0][0]
            pas = reg[0][1]
        else:
            error_logs.append(reg[0][0])
        auth = test_authentication.test_authentication(driver, email, pas)
        if auth[0] is not None:
            error_logs.append(auth[0])
        trial_offer = test_trial_offer.test_trial_offer(driver)
        if trial_offer[0] is not None:
            error_logs.append(trial_offer[0])
        trial_accept = test_trial_accept.test_trial_accept(driver)
        if trial_accept[0] is not None:
            error_logs.append(trial_accept[0])
        driver.close()
        driver.quit()
    count_tests = reg[1] + auth[1] + trial_offer[1] + trial_accept[1] + search[1]
    count_errors = len(error_logs)
    return f'Всего проведено {count_tests} тестов, Количество ошибок: {count_errors}, Ошибки: {error_logs}'


def search_test_runner(repeat_test=1):
    options = webdriver.ChromeOptions()
    error_logs = []
    for num in range(repeat_test):
        driver = webdriver.Chrome(options=options)
        search = test_open_search.test_open_search(driver)
        if search[0] is not None:
            error_logs.append(search[0])
        driver.close()
        driver.quit()
    count_errors = len(error_logs)
    return f'Всего проведено {repeat_test} тестов, Количество ошибок: {count_errors}, Ошибки: {error_logs}'


def registration_test_runner(repeat_test=1):
    options = webdriver.ChromeOptions()
    error_logs = []
    for num in range(repeat_test):
        driver = webdriver.Chrome(options=options)
        reg = test_registration.test_registration(driver)
        if len(reg[0]) == 1:
            error_logs.append(reg[0][0])
        driver.close()
        driver.quit()
    count_errors = len(error_logs)
    return f'Всего проведено {repeat_test} тестов, Количество ошибок: {count_errors}, Ошибки: {error_logs}'


def auth_test_runner(repeat_test=1):
    options = webdriver.ChromeOptions()
    error_logs = []
    for num in range(repeat_test):
        driver = webdriver.Chrome(options=options)
        reg = test_registration.test_registration(driver)
        if len(reg[0]) > 1:
            email = reg[0][0]
            pas = reg[0][1]
        else:
            error_logs.append(reg[0][0])
        auth = test_authentication.test_authentication(driver, email, pas)
        if auth[0] is not None:
            error_logs.append(auth[0])
        driver.close()
        driver.quit()
    count_tests = reg[1] + auth[1]
    count_errors = len(error_logs)
    return f'Всего проведено {count_tests} тестов, Количество ошибок: {count_errors}, Ошибки: {error_logs}'

def trial_offer_test_runner(repeat_test=1):
    options = webdriver.ChromeOptions()
    error_logs = []
    for num in range(repeat_test):
        driver = webdriver.Chrome(options=options)
        reg = test_registration.test_registration(driver)
        if len(reg[0]) > 1:
            email = reg[0][0]
            pas = reg[0][1]
        else:
            error_logs.append(reg[0][0])
        auth = test_authentication.test_authentication(driver, email, pas)
        if auth[0] is not None:
            error_logs.append(auth[0])
        trial_offer = test_trial_offer.test_trial_offer(driver)
        if trial_offer[0] is not None:
            error_logs.append(trial_offer[0])
        driver.close()
        driver.quit()
    count_tests = reg[1] + auth[1] + trial_offer[1]
    count_errors = len(error_logs)
    return f'Всего проведено {count_tests} тестов, Количество ошибок: {count_errors}, Ошибки: {error_logs}'


def trial_accept_test_runner(repeat_test=1):
    options = webdriver.ChromeOptions()
    error_logs = []
    for num in range(repeat_test):
        driver = webdriver.Chrome(options=options)
        reg = test_registration.test_registration(driver)
        if len(reg[0]) > 1:
            email = reg[0][0]
            pas = reg[0][1]
        else:
            error_logs.append(reg[0][0])
        auth = test_authentication.test_authentication(driver, email, pas)
        if auth[0] is not None:
            error_logs.append(auth[0])
        trial_offer = test_trial_offer.test_trial_offer(driver)
        if trial_offer[0] is not None:
            error_logs.append(trial_offer[0])
        trial_accept = test_trial_accept.test_trial_accept(driver)
        if trial_accept[0] is not None:
            error_logs.append(trial_accept[0])
        driver.close()
        driver.quit()
    count_tests = reg[1] + auth[1] + trial_offer[1] + trial_accept[1]
    count_errors = len(error_logs)
    return f'Всего проведено {count_tests} тестов, Количество ошибок: {count_errors}, Ошибки: {error_logs}'


print(all_tests_runner(repeat_tests=2))
# print(search_test_runner(repeat_test=1))
# print(registration_test_runner(repeat_test=1))
# print(trial_offer_test_runner(repeat_test=1))
# print(trial_accept_test_runner(repeat_test=1))
