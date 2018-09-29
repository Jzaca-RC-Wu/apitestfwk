import csv

import pandas as pd
import xlrd


class RestoreData(object):

    def __init__(self, xlxs, sheet_name=None):
        self.xlxs = xlxs
        self.sheet_name = sheet_name
        self._fieldnames = None

    def get_sheet_data_by_pandas(self):
        sheet_data = pd.read_excel(self.xlxs, self.sheet_name)
        return sheet_data


def get_xlxs_data(f, *args):
    wb = xlrd.open_workbook(f)

    if list(*args):
        sh_names = list(*args)
    else:
        sh_names = wb.sheet_names()
    headers = wb.sheet_by_index(0).row_values(0)

    data_s = []
    for arg in sh_names:
        for i in range(1, wb.sheet_by_name(arg).nrows):
            data = {}
            for j in range(wb.sheet_by_name(arg).ncols):
                data[headers[j]] = wb.sheet_by_name(arg).cell(i, j).value
            data_s.append(data)
    return data_s


def get_csv_data(csvfile):
    """
    read csv file as dict
    :param csvfile: csv file
    :param fieldnames:
    :return: return file as dict
    """
    f = open(csvfile, 'r')
    dic_reader = csv.DictReader(f, dialect='excel', delimiter=',')
    data_s = []
    for row in dic_reader:
        new_dict = {}
        for key in row.keys():
            new_dict[key] = row[key]
        print(new_dict)
        data_s.append(new_dict)
    return data_s


def make_request(case):
    url = case['host'] + case['api']
    method = case['method'].upper()
    paras = case['paras']
    data = case['data']
    if case['headers']:
        headers = eval(case['headers'])
    else:
        headers = {}
    return url, method, paras, data, headers

# print(RestoreDataFromCSV().get_test_fieldnames())

# file = "E:\\automatic\\apitestfwk\\test_data\\testcase.csv"
# xlsxfile = "E:\\automatic\\apitestfwk\\test_data\\test_case.xlsx"
#
# # print(get_csv_data(file))
# # dict_data = get_csv_data(file)
#
# dict_data = get_xlxs_data(xlsxfile)
# print(dict_data)
# make_request(dict_data)
# print(make_request(dict_data[0]))
# for i in len(dict_data):
#     print(dict_data[i])
