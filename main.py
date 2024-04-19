from tests.test_registration_and_login import TestUserRegistrationAndLogin
from tests.test_search import TestSearch
from tests.test_trial_map import TestTrialMap
from tests.test_folder import TestFolder
from tests.test_add_comment import TestAddComment
from tests.test_search_sample import TestSearchSample
from tests.test_team import TestTeam

if __name__ == '__main__':
    tests = [
        TestSearch,
        TestUserRegistrationAndLogin,
        TestTrialMap,
        TestFolder,
        TestAddComment,
        TestSearchSample,
        TestTeam,
    ]

    for TestClass in tests:
        test = TestClass()
        test.run_test_task()
    print('all test calls')
    for i in tests:
        print(i.__name__)
