from csv import reader,DictReader
# with open("employee.csv")as f:
#     data_reader=reader(f)
#     for row in data_reader:
#         print(row)

with open("employee.csv")as f:
    data_reader=DictReader(f)
    for row in data_reader:
        print(row)