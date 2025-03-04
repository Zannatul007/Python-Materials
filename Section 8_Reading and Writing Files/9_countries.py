import csv
input_filename = 'country_info.txt'

countries = {}
with open(input_filename,'r',encoding='utf-8',newline='') as country_file:
    csv_read_file = csv.DictReader(country_file,delimiter='|')
    for row in csv_read_file:
        print(row['Country'])
        countries[row['Country'].casefold()] = row
        countries[row['CC'].casefold] = row
     

# print(countries)

while True:
    chosen_country = input('Please enter the name of a country: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['Capital']}")
    elif chosen_country == 'quit':
        break
