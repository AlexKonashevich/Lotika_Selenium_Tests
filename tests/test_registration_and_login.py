from tests_runner import TestRunner
from tests.create_auth_user import create_auth_user


class TestUserRegistrationAndLogin(TestRunner):
    def run_test(self):
        create_auth_user(driver=self.driver)
