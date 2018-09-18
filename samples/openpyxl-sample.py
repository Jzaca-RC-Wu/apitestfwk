from openpyxl import load_workbook

file = 'E:\\automatic\\apitestfwk\\test_data\\testcase.xlsx'
wb = load_workbook(filename=file)
sheet_ranges = wb['login']
print(sheet_ranges['A1'].value)
