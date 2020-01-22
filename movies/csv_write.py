# from csv import writer,DictWriter
# with open("employee1.csv","w")as f:
#     csv_reader=writer(f)
#     csv_reader.writerow(["name","contact"])
#     csv_reader.writerow(["manisha","985124562"])
#     csv_reader.writerow(["khimmaya","9845612323"])

from csv import writer,DictWriter
with open("employee1.csv","w")as f:
    fieldnames=["firstname","lastname"]
    csv_reader = DictWriter(f,fieldnames=fieldnames)
    csv_reader.writeheader()
    csv_reader.writerow({"firstname":"khimmaya","lastname":"ghimire"})

