from tests.test_registration_and_login import TestUserRegistrationAndLogin
from tests.test_open_search import TestOpenSearch
from tests.test_trial_map import TestTrialMap


if __name__ == '__main__':
    tests = [TestOpenSearch, TestUserRegistrationAndLogin, TestTrialMap]

    for TestClass in tests:
        test = TestClass()
        test.run_test_task()
    print('all test calls')
    for i in tests:
        print(i.__name__)
