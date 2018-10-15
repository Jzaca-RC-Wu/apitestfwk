from lxml import html, etree

from public.SendRequest import SendRequest as sdq

HouseListUrl = "http://www.gzbjfc.com/House/HouseList.aspx"
HouseListUrl_page = "http://www.gzbjfc.com/House/HouseList.aspx?page={}"


class HouseList:

    def __init__(self, url):
        self.url = url
        self.tree = html.parse(self.url)

    def getitem(self, item):
        return self.tree.xpath(item)

    def get_html(self):
        res = sdq(self.url).geturlresp()
        tree = html.parse(res)
        # print(etree.tostring(tree))
        r = tree.xpath("//table[@class=\"Repeater\"]")
        # print(len(r))
        return tree

    def get_search_pages(self):
        result = self.tree.xpath("//div[@id=\"cph_hl1_pagerTop\"]/a/@href")
        if result:
            pages_nums = result[-1].split("=")[1]
        print(pages_nums)

        print(result)
        print(set(result))
        print(len(result))
        return pages_nums

    def get_house_pros_info(self):
        result = self.tree.xpath('//table[@class=\"Repeater\"]')
        print(type(result[0]))
        print(len(result))
        print(result[0].text_content().strip())
        for i in range(len(result[0])):
            print(result[0][i].text_content().strip())

        pros = {}
        pro_name_list = []
        # result = self.tree.xpath('//div[@align=\"left\"]/a[@class=\"url\"]')
        for pro in self.tree.xpath('//div[@align=\"left\"]/a[@class=\"url\"]'):
            pro_name_list.append(pro.text)
        pros['name'] = pro_name_list
        pros['target'] = self.tree.xpath('//a[@class=\"url\"]/@href')

        sale_list = []
        for sale in self.tree.xpath('//table//td[@width="9%"]'):
            sale_list.append(sale.text)
        pros['pre_sales'] = sale_list

        pros['pre_sale_credit'] = self.tree.xpath('//table//td/div[@align=\"left\"]')
        print(pros['pre_sale_credit'][0].text)


        print(pros)

# resp = HouseList(HouseListUrl).get_html()

# tree = html.parse(HouseListUrl)
# print(tree.tostring())

# print(HouseList(HouseListUrl).get_search_pages())


print(HouseList(HouseListUrl).get_house_pros_info())
# print(resp)
