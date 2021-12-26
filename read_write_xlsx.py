import xlrd

import xlsxwriter

#code for reading
#code to open a excel sheet using xlrd
wb = xlrd.open_workbook("/Users/rohitdadala/PycharmProjects/databadeex/venv/data_XLS_1000.xls")
# creating a sheet object for the sheet index 0
sh = wb.get_sheet(0)
# sending data to the cell (0,0)
sh.write(0,0,'rohit')
# saving the new workbook after editing
wb.save("/Users/rohitdadala/PycharmProjects/databadeex/venv/data_XLS_1000-1.xls")

#creating and writing to a new excel file

wb = xlsxwriter.Workbook("/Users/rohitdadala/PycharmProjects/databadeex/venv/new_xlsx.xls")#creating a workbook object
sh = wb.add_worksheet("sheet 1")# creating a sheet object
row= 0
col = 0
contents = [['rohit','ddsvsa','sfwqef','sqwew'],['alekya','ddsvsa','sfwqef','sqwew'],['zara','ddsvsa','sfwqef','sqwew']]

for i in contents:
    for j in i:
        sh.write(row,col,j)
        col+=1
    row+=1
    col=0

wb.close()