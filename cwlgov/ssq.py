from lxml import html

xx_uri = "http://www.cwl.gov.cn/kjxx/ssq/kjgg/"
data_uri = "http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=200"
custom_xx_uri = "http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=&issueStart=&issueEnd=&dayStart=2017-10-24&dayEnd=2018-10-24&pageNo="
class SSQ:

    def __init__(self):
        self.url = xx_uri
        self.html = html.parse(self.url)

    def getitem(self, path, *args):
        return self.tree.xpath(path.format(*args))

    # def get