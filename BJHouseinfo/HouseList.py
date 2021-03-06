import csv
import urllib.request

from bs4 import BeautifulSoup
from lxml import html

HouseListUrl = "http://www.gzbjfc.com/House/HouseList.aspx"
HouseListUrl_page = "http://www.gzbjfc.com/House.aspx?page={}"


class HouseList:

    def __init__(self, url):
        self.url = url
        self.tree = html.parse(self.url)

    def getitem(self, path, *args):
        return self.tree.xpath(path.format(*args))

    def get_search_pages(self):
        result = self.getitem("//div[@id=\"cph_hl1_pagerTop\"]/a/@href")
        if result:
            pages_nums = result[-1].split("=")[1]
        return pages_nums

    def get_house_pros_info(self):
        pros = []
        content = self.tree.xpath('//table[@class=\"Repeater\"]')
        pro_name = self.tree.xpath('//table[@class=\"Repeater\"]//table//tr[{}]/td[{}]'.format(1, 2))
        pro_target = self.tree.xpath('//table[@class=\"Repeater\"]//table//tr[{}]/td[{}]//a/@href'.format(1, 2))
        pro_attrs = self.tree.xpath('//table[@class=\"Repeater\"]//table//tr[{}]/td[{}]'.format(1, 4))
        pro_presale = self.getitem('//table[@class=\"Repeater\"]//table//tr[{}]/td[{}]', 1, 6)
        pro_preid = self.getitem('//table[@class=\"Repeater\"]//table//tr[{}]/td[{}]', 2, 2)
        pro_price = self.getitem('//table[@class=\"Repeater\"]//table//tr[{}]/td[{}]', 2, 4)
        pro_prenum = self.getitem('//table[@class=\"Repeater\"]//table//tr[{}]/td[{}]', 2, 6)
        pro_address = self.getitem('//table[@class=\"Repeater\"]//table//tr[{}]/td[{}]', 3, 2)
        pro_avrprice = self.getitem('//table[@class=\"Repeater\"]//table//tr[{}]/td[{}]', 3, 4)
        pro_sale_url = self.getitem('//table[@class=\"Repeater\"]//table//tr[{}]/td[{}]//a/@href', 3, 5)
        pro_manufactor = self.getitem('//table[@class=\"Repeater\"]//table//tr[{}]/td[{}]', 4, 2)

        for i in range(len(content)):
            pro = {}
            pro['项目名称'] = pro_name[i].text_content()
            pro['项目简介地址'] = pro_target[i]
            pro['项目性质'] = pro_attrs[i].text_content()
            pro['预售套数'] = pro_presale[i].text_content()
            pro['预售证号'] = pro_preid[i].text_content()
            pro['媒体报价'] = pro_price[i].text_content()
            pro['可售套数'] = pro_prenum[i].text_content()
            pro['项目地址'] = pro_address[i].text_content()
            pro['成交均价'] = pro_avrprice[i].text_content()
            pro['销售情况连接'] = pro_sale_url[i]
            pro['开发商'] = pro_manufactor[i].text_content()
            pros.append(pro)
            # print(pro)
        return pros

    def getitembyBS4(self, path):
        # todo
        html = urllib.request.urlopen(self.url).read()
        soup = BeautifulSoup(html, 'lxml-xml')
        print(type(soup), soup.body)
        print(soup.body.form.div.div.table.contents[0])
        # content = soup.find_all(path)
        # items = []
        # for child in content.children:
        #     print(child.contents)
        #     items.append(child.contents)
        # return items


def get_all_pros():
    pages = HouseList(HouseListUrl).get_search_pages()
    projects = []
    if pages:
        for i in range(int(pages)):
            url = HouseListUrl_page.format(i)
            page = HouseList(url).get_house_pros_info()
            for pro in page:
                projects.append(pro)
    return projects


def write_csv_dict(file, dict_x):
    with open(file, 'w+', newline='', encoding='GBK') as f:
        headers = [k for k in dict_x[0]]
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(dict_x)


# write_csv_dict("E:\\automatic\\apitestfwk\\BJHouseinfo\\BJHouse.csv", get_all_pros())
# HouseList(HouseListUrl).show()
# HouseList(HouseListUrl).getitembyBS4("'//table[@class=\"Repeater\"]//table//tr[{}]/td[{}]")
