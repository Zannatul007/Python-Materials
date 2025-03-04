import csv
with open('OlympicMedals_2020.csv','r') as csv_file:
    csv_file_reader = csv.reader(csv_file)
    with open('EditedOlympicMedals.csv','w',newline='') as write_file:
        csv_write_file= csv.writer(write_file,delimiter="\t")
        for line in csv_file_reader:
            csv_write_file.writerow(line)

with open('D:\Python Materials\Reading and Writing Files\EditedOlympicMedals.csv','r',encoding='utf-8') as csv_file:
    csv_file_reader = csv.reader(csv_file,delimiter='\t')
    for line in csv_file_reader:
        print(line)