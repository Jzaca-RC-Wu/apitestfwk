import unittest


from public import restore_data,SendRequest

file = "E:\\automatic\\apitestfwk\\test_data\\testcase.csv"


class BaseApiTest(unittest.TestCase):
    cases = restore_data.make_test_from_csv(file)

    def test_apis(self,case):
        request = restore_data.make_request(case)
        resp = SendRequest.geturlresp(request)



