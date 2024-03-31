from selenium import webdriver
test_calls = []


class TestRunner:

    def __init__(self):
        self.base_url = 'https://dev.lotika.ru/'
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)

    def run_test(self):
        raise Exception('Method should be implemented')

    def run_test_task(self):
        test_calls.append(self.__class__.__name__)
        try:

            self.run_test()
        except Exception as err:
            print(f'error: {err}')
        finally:
            self.driver.close()
            self.driver.quit()
