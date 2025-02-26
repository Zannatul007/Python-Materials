import csv
with open('OlympicMedals_2020.csv','r',encoding='utf-8',newline='') as csv_file:
    csv_file_dict_reader = csv.DictReader(csv_file)
    with open('EditedOlympicMedals.csv','w',newline='',encoding='utf-8') as csv_file_new:
        field_names = ["Rank","Country","Gold","Silver","Bronze","Total"]
        csv_file_dict_writer = csv.DictWriter(csv_file_new,fieldnames=field_names)
        csv_file_dict_writer.writeheader()
        for line in csv_file_dict_reader:
            csv_file_dict_writer.writerow(line)

with open('EditedOlympicMedals.csv','r',encoding='utf-8',newline='') as csv_file:
    csv_file_dict_reader = csv.DictReader(csv_file)
    for line in csv_file_dict_reader:
            print(line)