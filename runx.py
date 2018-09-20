import os
import time
import unittest

from libs import BSTestRunner
from testcase.baseapi_testcase import BaseApiTest
from testcase.test_unittestsample import TestSequenceFunctions

if __name__ == '__main__':
    testsuit = unittest.TestSuite()
    # testsuit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestSequenceFunctions))
    testsuit.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions))
    testsuit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(BaseApiTest))
    now = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_dir = os.path.join(basedir, 'test_Report')
    file = os.path.join(file_dir, (now + '-result.html'))
    re_open = open(file, 'wb')
    runner = BSTestRunner.BSTestRunner(stream=re_open, title='接口测试报告', description='测试报告详情')
    # basdir = os.path.abspath(os.path.dirname(__file__))
    # filepath1 = os.path.join(basdir + '/test_Report/%s-result.html' % now)
    testcount = testsuit.countTestCases()
    print('测试用例共：', testcount, '条')
    runner.run(testsuit)

    # discover = unittest.defaultTestLoader.discover('./testcase/', pattern='test_*.py')
    # testcount = discover.countTestCases()
    # print('测试用例共：', testcount, '条')
    # runner.run(discover)
