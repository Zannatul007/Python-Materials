import csv
with open('D:\Python Materials\Reading and Writing Files\OlympicMedals_2020.csv','r',newline='',encoding='utf-8') as csv_file:
    sample_line = ""
    for line in csv_file:
        sample_line+=csv_file.readline()
    csv_dialect = csv.Sniffer().sniff(sample_line)
    csv_file.seek(0)
    csv_reader_file = csv.reader(csv_file,dialect=csv_dialect)
    for line in csv_reader_file:
        print(line)