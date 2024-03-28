from tests.test_registration_and_login import TestUserRegistrationAndLogin
from tests.test_open_search import TestOpenSearch
from main import TestRunner
from tests.test_trial_offer import TestTrialOffer


if __name__ == '__main__':
    tests = [TestOpenSearch(), TestUserRegistrationAndLogin(), TestTrialOffer()]

    for TestClass in tests:
        print(TestClass)
        test = TestClass()
        test.run_test_task()

    TestRunner.driver.close()
    TestRunner.driver.quit()

    print('all test calls')
    for i in tests:
        print(i.__name__)
