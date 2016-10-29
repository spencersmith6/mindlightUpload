# from collections import OrderedDict
# from xlrd import open_workbook
# import simplejson as json
#
#
# def handle_excel_file(f, clinic):
#     file = open_workbook(f)
#     sheet = file.sheets()[0]
#     print(sheet.nrows, sheet.ncols)
#
#     toJSON = []
#     headers = sheet.row_values(0)
#     print(headers)
#
#     for row in range(1, sheet.nrows):
#         subjectData = OrderedDict()
#         values = sheet.row_values(row)
#
#         for col in range(sheet.ncols):
#             if headers[col] == 'Medical Condition':
#                 conditions = values[col].split(',')
#                 print(conditions)
#                 subjectData[headers[col]] = conditions
#             else:
#                 subjectData[headers[col]] = values[col]
#         toJSON.append(subjectData)
#
#     j = json.dumps(toJSON)
#
#     print(j)
#
#     with open('JSONfiles/%s.json' % clinic, 'w') as w:
#         w.write(j)