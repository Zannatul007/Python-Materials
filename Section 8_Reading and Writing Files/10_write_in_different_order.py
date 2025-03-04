ordering = ['Country','Gold','Silver','Bronze','Total','Rank']
import csv

with open ('D:\Python Materials\Reading and Writing Files\OlympicMedals_2020.csv','r',encoding='utf-8',newline='')as read_file,\
open('ModifiedOlympicMedals.csv','w',encoding='utf-8',newline = '') as write_file:

    csv_read_file = csv.DictReader(read_file)
    for row in csv_read_file:
        new_dict = {}
        for key in ordering:
            value = row[key]
            new_dict[key] = value
        print(new_dict)
        print(f"{new_dict}",file=write_file)


    
# for key,index in new_dict.items():
#     print(key,index)