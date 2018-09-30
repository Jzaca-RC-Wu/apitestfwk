from public.SendRequest import SendRequest as sdrq
import ddt
class Login(object):
    login_in = {"Method": "POST",
                "url": "https://login.longzhu.com/lz/login?version=%(vsn)s&device=%(dvs)s&packageId=%(pid)s&utm_sr=%(usr)s",
                "data": {"account": "13621651634", "password": "123456w"}}
    login_out = ""
    sign_on = ""
    data = ["5.3.0", "4", 1, "chanel_2"]

    def __init__(self, name, pwd):
        self.sign_name = name
        self.sign_pwd = pwd
        self.url = ""
        self.method = "GET"

    # @ddt.data(data)
    def login(self):
        self.url = self.login_in['url'].format(self.data[0], self.data[1], self.data[2], self.data[3])
        self.method = self.login_in['Method']
        resp = sdrq(self.url, self.method).geturlresp()
        return resp

    # @login()
    def get_login_info(self):
        self.login()


