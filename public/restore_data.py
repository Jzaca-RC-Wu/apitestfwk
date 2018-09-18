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
    # print(headers)

    data_s = []
    for arg in sh_names:
        # if not wb.sheet_by_name(arg):
        #     print('%(arg)s is not exsit!!'.format(arg=arg))
        #     pass
        for i in range(1, wb.sheet_by_name(arg).nrows):
            data = {}
            for j in range(wb.sheet_by_name(arg).ncols):
                data[headers[j]] = wb.sheet_by_name(arg).cell(i, j).value
            data_s.append(data)
    # print(data_s)
    return data_s


def get_csv_data(csvfile, fieldnames=None):
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
    url = case['host'] + case['api'] + "?" + case['parameters']
    data_s = case['data']
    header = case['Headers']
    return url, header, data_s


# print(RestoreDataFromCSV().get_csv_data("E:\\automatic\\apitestfwk\\test_data\\testcase.csv"))
# # print(RestoreDataFromCSV().get_test_fieldnames())

file = "E:\\automatic\\apitestfwk\\test_data\\testcase.csv"
xlsxfile = "E:\\automatic\\apitestfwk\\test_data\\testcase1.xlsx"

# sheets = get_xlxs_sheets(xlsxfile, ['login'])
# print()

sheets_data = get_xlxs_data(xlsxfile)
# sheets_data = get_xlxs_data(xlsxfile, ['login', 'empty', 'register', 'Sheet1'])
print(sheets_data)
