import unittest
import ddt


from public import restore_data,SendRequest

file = "E:\\automatic\\apitestfwk\\test_data\\testcase.csv"

cases = restore_data.get_csv_data(file)


class BaseApiTest(unittest.TestCase):

    @ddt.data(*cases)
    @ddt.unpack
    def test_apis(self, case):
        #TODO case 还未创建
        request = restore_data.make_request(case)
        resp = SendRequest.geturlresp(request)



