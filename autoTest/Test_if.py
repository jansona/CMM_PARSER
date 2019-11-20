import unittest
from selenium import webdriver
import random



class Test_if(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)

    def test_1(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(1) + ".png")

    def test_2(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(2) + ".png")

    def test_3(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(3) + ".png")

    def test_4(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(4) + ".png")

    def test_5(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(5) + ".png")

    def test_6(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(6) + ".png")

    def test_7(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(7) + ".png")

    def test_8(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(8) + ".png")

    def test_9(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(9) + ".png")

    def test_10(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(10) + ".png")

    def test_11(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(11) + ".png")

    def test_12(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(12) + ".png")

    def test_13(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(13) + ".png")

    def test_14(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(14) + ".png")

    def test_15(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(15) + ".png")

    def test_16(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(16) + ".png")

    def test_17(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(17) + ".png")

    def test_18(self, i=0):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.maximize_window()
        self.search_field = self.driver.find_element_by_id("code")
        self.search_field.clear()
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        name = "int main(){" + "if(" + str(random.randint(0, 25)) + " > " + str(random.randint(0, 25)) + \
               ') int ' + \
               chr(ord('a') + random.randint(0, 25)) + ' = ' + str(random.randint(0, 25)) + ';' + \
               '}'
        # 在这里调整测试代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        self.search_field.send_keys(name)
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
        self.driver.save_screenshot("test_if_" + str(18) + ".png")

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
