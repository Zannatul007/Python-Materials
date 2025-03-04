import csv

def invoice_number_parsing(s:str)->tuple[int,int]:
    year,number = s.split('-')
    return year,number
with open('invoices.csv','r',encoding='utf-8',newline='') as read_file:
    sample_data = ""
    for i in range(3):
        sample_data+=read_file.readline()
    print(sample_data)
    sample_dialect = csv.Sniffer().sniff(sample_data)
    read_file.seek(0)
    keys = ['Invoice Date',"Invoice Type","Invoice Unit"]
    csv_read_file = csv.DictReader(read_file,dialect=sample_dialect,fieldnames=keys)
    for row in csv_read_file:
        # year,number  = tuple(row['Invoice Date'].split('-'))
        # print(year,number)
        year,number = invoice_number_parsing(row['Invoice Date'])
        print(year,number)
