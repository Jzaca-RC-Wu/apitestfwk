import csv

import pandas as pd


class RestoreData(object):

    def __init__(self, xlxs, sheet_name=None):
        self.xlxs = xlxs
        self.sheet_name = sheet_name
        self._fieldnames = None

    def get_sheet_data_by_pandas(self):
        sheet_data = pd.read_excel(self.xlxs, self.sheet_name)
        return sheet_data


def make_test_from_csv(csvfile, fieldnames=None):
    """
    read csv file as dict
    :param csvfile: csv file
    :param fieldnames:
    :return: return file as dict
    """
    f = open(csvfile, 'r')
    dic_reader = csv.DictReader(f, fieldnames, dialect='excel')
    return dic_reader

def make_request(case):
    url = case['hose'] + case['api'] + "?" + case['parameters']
    data_s = case['data']
    header = case['Headers']
    return url, header, data_s


# print(RestoreDataFromCSV().make_test_from_csv("E:\\automatic\\apitestfwk\\test_data\\testcase.csv"))
# # print(RestoreDataFromCSV().get_test_fieldnames())

file = "E:\\automatic\\apitestfwk\\test_data\\testcase.csv"
reader = make_test_from_csv(file)
for data in reader:
    print(data)
    # for k in reader.fieldnames:
    #     print(data[k])
