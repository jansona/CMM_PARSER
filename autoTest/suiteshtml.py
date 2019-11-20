import unittest

import HTMLTestRunner
import os

from Test_assignment import Test_assignment
from Test_if import Test_if
from datetime import date
from Test_while import Test_while
from Test_add import  Test_add
from Test_Wrong import  Test_Wrong
now = date.today()
datestr = now.strftime('%m-%d-%y')

dir = os.getcwd()

search_test = unittest.TestLoader().loadTestsFromTestCase(Test_assignment)
search_test1 = unittest.TestLoader().loadTestsFromTestCase(Test_if)
search_test2 = unittest.TestLoader().loadTestsFromTestCase(Test_while)
search_test3 = unittest.TestLoader().loadTestsFromTestCase(Test_add)
search_test4 = unittest.TestLoader().loadTestsFromTestCase(Test_Wrong)
FanYT_tests = unittest.TestSuite([search_test2])

filepath = dir + "/TestReport{}.html".format(datestr)
with open(filepath, 'wb') as outfile:
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Title:Test Report', description='Des:FanYunTian Tests')
    runner.run(FanYT_tests)
