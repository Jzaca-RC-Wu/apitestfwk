import openpyxl

wb = openpyxl.Workbook()
ws = wb.create_sheet()
ws.column_dimensions.group('A', 'D', hidden=True)
ws.row_dimensions.group(1, 10, hidden=True)
wb.save('group.xlsx')
