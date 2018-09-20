import unittest

import ddt

from public import restore_data, SendRequest
from public.panduan import expectJson, cmp_dict

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
        # print(type(cases))
        url, method, paras, data, headers = restore_data.make_request(cases)
        resp = SendRequest.SendRequest(url, method, paras, data, headers).get_jsonresp()
        # print(resp)
        # self.assertEqual(True, expectJson(cases['expe_res'], resp))
        self.assertEqual(True, cmp_dict(eval(cases['expe_res']), resp))
