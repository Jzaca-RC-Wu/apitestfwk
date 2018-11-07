from public import SendRequest
from BJHouseinfo import HouseList
import time
custom_xx_uri = "http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=&issueStart=&issueEnd=&dayStart=2017-10-24&dayEnd={}&pageNo="
dayEnd = time.strftime("%Y-%m-%d", time.localtime())
custom_xx_uri = custom_xx_uri.format(dayEnd)
print(dayEnd)
result = SendRequest.SendRequest(custom_xx_uri, headers={"Referer": "http://www.cwl.gov.cn/kjxx/ssq/kjgg/"}).get_jsonresp()
print(len(result["result"]))
keys = result.keys()
if result["result"]:
    result_keys = max(result["result"][i].keys() for i in range(len(result["result"])))
    HouseList.write_csv_dict("ssq_开奖结果.csv", result["result"])

