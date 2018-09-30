import unittest

import ddt
import json
from public import restore_data, SendRequest
from public.comparedata import is_satisfy
from public.panduan import expectJson

file = "E:\\automatic\\apitestfwk\\test_data\\testcase.csv"
xlfile = "E:\\automatic\\apitestfwk\\test_data\\test_case.xlsx"

# cases = restore_data.get_csv_data(file)
cases = restore_data.get_xlxs_data(xlfile)
# print(cases)

@ddt.ddt
class BaseApiTest(unittest.TestCase):
    """数据驱动测试用例"""

    @ddt.data(*cases)
    # @ddt.unpack
    def test_apis(self, cases):
        url, method, paras, data, headers = restore_data.make_request(cases)
        resp = SendRequest.SendRequest(url, method, paras, data, headers).get_jsonresp()
        self.assertEqual(True, is_satisfy(cases['expe_res'], resp), True)
        # self.assertEqual(True, expectJson(cases['expe_res'], resp), True)
