from selenium import webdriver
from tests import test_registration
from tests import test_authentication
from tests import test_open_search
from tests import test_trial_offer
from tests import test_trial_accept


def all_tests_runner(search_tests=1, reg_auth_tests=1, tr_offer=1, tr_accept=1):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    error_logs = []
    for num in range(search_tests):
        search = test_open_search.test_open_search(driver)
        if search[0] is not None:
            error_logs.append(search[0])
    for num in range(reg_auth_tests):
        reg = test_registration.test_registration(driver)
        if len(reg[0]) > 1:
            email = reg[0][0]
            pas = reg[0][1]
        else:
            error_logs.append(reg[0][0])
    for num in range(reg_auth_tests):
        auth = test_authentication.test_authentication(driver, email, pas)
        if auth[0] is not None:
            error_logs.append(auth[0])

    for num in range(tr_offer):
        trial_offer = test_trial_offer.test_trial_offer(driver)
        if trial_offer[0] is not None:
            error_logs.append(trial_offer[0])
    for num in range(tr_accept):
        trial_accept = test_trial_accept.test_trial_accept(driver)
        if trial_accept[0] is not None:
            error_logs.append(trial_accept[0])

    count_tests = reg[1] + auth[1] + trial_offer[1] + trial_accept[1] + search[1]
    count_errors = len(error_logs)
    return f'Всего проведено {count_tests} тестов, Количество ошибок: {count_errors}, Ошибки: {error_logs}'


print(all_tests_runner(search_tests=1, reg_auth_tests=1, tr_offer=1, tr_accept=1))
