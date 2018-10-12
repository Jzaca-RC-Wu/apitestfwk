from public.SendRequest import SendRequest as sdq
from lxml import html, etree
from urllib.request import urlopen
import requests

HouseListUrl = "http://www.gzbjfc.com/House/HouseList.aspx"


class HouseList:

    def __init__(self, url):
        self.url = url

    def get_xml(self):
        resp = sdq(self.url).geturlresp()
        # resp = requests.get(self.url)
        # print(resp.text, type(resp.text))
        # tree = html.parse(urlopen(self.url))
        tree = html.parse(resp)
        print(etree.tostring(tree))
        r = tree.xpath("//table")
        # r = tree.xpath('<table * </table>')
        print(len(r))
        print(len(tree.xpath('//tabel/@class="Repeater"')))
        # return r


resp = HouseList(HouseListUrl).get_xml()
# print(resp)