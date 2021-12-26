import openpyxl
class FileOpen:
    def __init__(self, path):
        self.path = path

    def open_workbook(self):
        wb = openpyxl.load_workbook(self.path)
        sheet = wb.active
        data = {}
        for i, row in enumerate(sheet.iter_rows(values_only=True)):
            if i == 0:
                data[row[1]] = []
                data[row[2]] = []
                data[row[3]] = []
                data[row[4]] = []
                data[row[5]] = []
                data[row[6]] = []
                data[row[7]] = []

            else:
                data['First Name'].append(row[1])
                data['Last Name'].append(row[2])
                data['Gender'].append(row[3])
                data['Country'].append(row[4])
                data['Age'].append(row[5])
                data['Date'].append(row[6])
                data['Id'].append(row[7])

        return data

if __name__ == '__main__':
    # file = FileOpen(input("enter absolute path : "))
    file = FileOpen("/Users/rohitdadala/PycharmProjects/data_files/file_example_XLSX_5000.xlsx")
    print(file.open_workbook())
