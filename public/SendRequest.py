import json
import urllib.error
import urllib.parse
import urllib.request
import urllib.response


class SendRequest(object):

    def __init__(self, url, method='GET', paras={}, data={}, headers={}):
        self.url = url
        self.method = method

        if isinstance(paras, dict):
            self.paras = urllib.parse.urlencode(paras)
        else:
            self.paras = paras

        self.data = data
        self.headers = headers
        # self.request = ''

    def geturlresp(self):
        if self.method.upper() == "GET" or not self.method:
            if self.paras:
                self.url = self.url + self.paras
                # self.url = self.url + "?" + self.fields
            request = urllib.request.Request(self.url, data=None, headers=self.headers)
        elif self.method.upper() == "POST":
            request = urllib.request.Request(self.url, data=self.fields.encode(), headers=self.headers)
        else:
            return

        resp = urllib.request.urlopen(request)
        # resp = json.load(resp)
        # print(resp)
        return resp  # , resp.info()

    def get_jsonresp(self):
        print(json.load(self.geturlresp()))
        return json.load(self.geturlresp())


def getroominfosbyrooms(roomids, keyword):
    url = 'http://houtai.tga.plu.cn/api2/room?domain=&pageIndex=0&pageSize=20&roomId=%s&type=0&userId=0&userTitle=&userqq='
    r_keyword = []
    for roomid in roomids:
        url1 = url % roomid
        res = SendRequest(url1).geturlresp()
        print(res.code)
        res = json.load(res)
        if res['items']:
            print(res['items'])
            r_keyword.append(res['items'][0][keyword])
        else:
            continue
            # uids.append('None')
    # print(list(r_keyword))
    return r_keyword


rooms = [541375, 1578057, 695989, 2075345, 2185, 2103779, 16463, 531250, 360055, 2130089, 340183, 2086654, 2064598,
         1690837, 1529500, 2075343, 2241164, 541375, 2075345, 2339460, 2314481, 2185, 2245356, 16463, 2241444,
         2111564, 1529500, 2054664, 2367879, 2064598, 360055, 2241427, 2109924, 1558132, 2103347, 1668380, 2350726,
         2356746, 2075343, 2130089, 2347725, 2222792, 2245199, 2119082, 16585, 869994, 2291360, 2103779, 2351630,
         918142, 2365980, 789320, 762811, 2306657, 1690837, 1541979, 2351859, 2319173, 2314912, 2115759, 1555518,
         2248345, 2348492, 2366251, 895056, 2120159, 2169291, 470387, 2054118, 1087210, 2305344, 2359900, 2367091,
         2346617, 2139362, 1464996, 2339492, 177682, 2248537, 2127436, 2333817, 2168208, 2365474, 2233598, 585637,
         2297379, 469898, 2342414, 1831790, 2182314, 442308, 2078180, 2070723, 2202770, 547446, 2086556, 2094291,
         206079, 2331449, 2367838, 379563, 393293, 2275846, 1689183, 1053681, 2369168, 1657768, 2194969, 933804,
         2312287, 2367022, 2260886, 2247548, 2368537, 2363588, 541992, 2169291, 470387, 2054118, 1087210, 2305344,
         2359900, 2367091, 2346617, 2139362, 1464996, 2339492, 177682, 2248537, 2127436, 2333817, 2168208, 2365474,
         2233598, 585637, 2297379, 469898, 2342414, 1831790, 2182314, 442308, 2078180, 2070723, 2202770, 547446,
         2086556, 2094291, 206079, 2331449, 2367838, 379563, 393293, 2275846, 1689183, 1053681, 2369168, 1657768,
         2194969, 933804, 2312287, 2367022, 2260886, 2247548, 2368537, 2363588, 541992]

# print(getroominfosbyrooms(rooms, 'userId'))
# print(getroominfosbyrooms(rooms, 'domain'))
