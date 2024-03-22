from selenium import webdriver
from tests import test_registration
from tests import test_authentication
from tests import test_open_search
from tests import test_trial_offer
from tests import test_trial_accept


def tests_runner(reg_tests=1, auth_tests=1, search_tests=1, tr_offer=1, tr_accept=1):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    email = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    pas = 'AAAAAAAAAAAAAAAAAAAA'
    error_logs = ''
    for num in range(reg_tests):
        reg = test_registration.test_registration(driver)
        if len(reg) > 2:
            email = reg[0][0]
            pas = reg[0][1]
        else:
            error_logs += reg[0][0] + '\n'
    for num in range(auth_tests):
        auth = test_authentication.test_authentication(driver, email, pas)
        if len(auth) > 1:
            error_logs += auth[0][0] + '\n'
    for num in range(search_tests):
        search = test_open_search.test_open_search(driver)
        if len(search) > 1:
            error_logs += search[0][0] + '\n'
    for num in range(tr_offer):
        trial_offer = test_trial_offer.test_trial_offer(driver)
        if len(trial_offer) > 1:
            error_logs += trial_offer[0][0] + '\n'
    for num in range(tr_accept):
        trial_accept = test_trial_accept.test_trial_accept(driver)
        if len(trial_accept) > 1:
            error_logs += trial_accept[0][0] + '\n'

    count_tests = reg[1] + auth[1] + search[1] + trial_offer[1] + trial_accept[1]
    count_errors = error_logs.count("\n")

    return f'Всего проведено {count_tests} тестов, Количество ошибок: {count_errors}, Ошибки: {error_logs}'


print(tests_runner(reg_tests=1, auth_tests=1, search_tests=1, tr_offer=1, tr_accept=1))
