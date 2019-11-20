import unittest
from selenium import webdriver
import random

class Test_Wrong(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)

    def test_1(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main)" + 'int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_Wrong_" + str(1) + ".png")

    def test_2(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + 'int ' + 'a' + ' = ' + str(random.randint(0, 25)) + '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_Wrong_" + str(2) + ".png")

    def test_3(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + \
               'int ' + chr(ord('a') + random.randint(0, 25)) + ' = ' + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_Wrong_" + str(3) + ".png")

    def test_4(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + \
               'int ' + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_Wrong_" + str(4) + ".png")

    def test_5(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int mn({" + \
               'int ' + chr(ord('a') + random.randint(0, 25)) + ' = ' + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_Wrong_" + str(5) + ".png")

    """def test(self, i=1):
        while i < 3:
            self.test_1(i)
            i = i + 1
    """
    def tearDown(self):
        self.driver.quit()



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
