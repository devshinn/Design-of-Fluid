# -*- coding: cp949 -*-
from openpyxl import load_workbook
SG = {}
viscosity = {}

schedule = {}

material = {}
f = load_workbook("DATA.xlsx", data_only=True)
load_ws = f['Sheet1']
get_cells = load_ws['a2' : 'c25']
for row in get_cells:
    SG.setdefault(row[0].value,row[1].value)

get_cells = load_ws['a2' : 'c25']
for row in get_cells:
    viscosity.setdefault(row[0].value,row[2].value)

get_cells = load_ws['h2' : 'i17']
for row in get_cells:
    material.setdefault(row[0].value,row[1].value)

get_cells = load_ws['e2' : 'f19']
for row in get_cells:
    schedule.setdefault(str(row[0].value),row[1].value)

total=[SG,viscosity,schedule,material]

import pickle
p = open('table_data.bin','wb')

pickle.dump(total, p)
p.close()

# f = open('table.bin','rb')
# data = pickle.load(f)
# p.close()
# print(data)