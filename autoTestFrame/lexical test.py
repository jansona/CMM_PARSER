# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def test_search_by_category(self, i=0):
        while i < 20:
            self.driver.get('http://127.0.0.1:8000/')
            self.search_field = self.driver.find_element_by_id("code")
            self.search_field.clear()
            self.search_field.send_keys('int main(){ while(' + chr(ord('a') + i * 5 % 26) + '< 10 ) int ' + chr(
                ord('a') + i * 3 % 26) + ' = ' + str(i) + ';}')
            self.search_field.submit()
            products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")
            self.driver.save_screenshot("while循环" + str(i) + ".png")
            i = i + 1

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
