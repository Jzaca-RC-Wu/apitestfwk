from lxml import html

from public.SendRequest import SendRequest as sdq

HouseListUrl = "http://www.gzbjfc.com/House/HouseList.aspx"
HouseListUrl_page = "http://www.gzbjfc.com/House/HouseList.aspx?page={}"


class HouseList:

    def __init__(self, url):
        self.url = url

    def get_html(self):
        res = sdq(self.url).geturlresp()
        tree = html.parse(res)
        # print(etree.tostring(tree))
        r = tree.xpath("//table[@class=\"Repeater\"]")
        # print(len(r))
        return tree

    html = get_html

    def get_search_pages(self):
        tree = self.get_html()
        result = tree.xpath("//div[@id=\"cph_hl1_pagerTop\"]/a/@href")
        pages_nums = result[-1].split("=")[1]
        print(pages_nums)

        print(result)
        print(len(result))
        # print(result[1].text)
        return pages_nums

    def get_house_pros_info(self):
        tree = self.get_html()
        result = tree.xpath('//table[@class=\"Repeater\"]')
        print(type(result[0]))

        house_pros = []
        for i in range(len(result)):
            house = {}
            house["houseimg"] = result[i].xpath['//div[@class="houseImg"]']
            house["housename"] = result[i].xpath['//a[@class="url"]']
            house["pre_num"] = result[i].xpath['//table[@]']
            print(house)


# resp = HouseList(HouseListUrl).get_html()
print(HouseList(HouseListUrl).get_search_pages())
# print(resp)
