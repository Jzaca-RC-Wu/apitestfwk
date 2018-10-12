from public.SendRequest import SendRequest as sdq
from lxml import html, etree
from urllib.request import urlopen
import requests

HouseListUrl = "http://www.gzbjfc.com/House/HouseList.aspx"


class HouseList:

    def __init__(self, url):
        self.url = url

    def get_xml(self):
        res = sdq(self.url).geturlresp()
        tree = html.parse(res)
        # print(etree.tostring(tree))
        r = tree.xpath("//table[@class=\"Repeater\"]")
        print(len(r))
        return tree

    def get_house_list(self):
        # Todo
        # for
        pass

resp = HouseList(HouseListUrl).get_xml()
# print(resp)