ordering = ['Country','Gold','Silver','Bronze','Total','Rank']
import csv
with open('OlympicMedals_2020.csv','r',encoding='utf-8',newline='') as read_file, open('modified_OlympicMedals_2020.csv','w',encoding='utf-8',newline='') as write_file:
    csv_read_file = csv.DictReader(read_file,delimiter="|")
    for row_dict in read_file:
        new_dict = {}
        for key in ordering:
            value = row_dict[key]

