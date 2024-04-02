from tests_runner import TestRunner


class TestUserRegistrationAndLogin(TestRunner):
    def run_test(self):
        self.create_auth_user()
