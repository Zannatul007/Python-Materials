countries_info ={}
countries = {}
with open("D:\Python Materials\Reading and Writing Files\country_info.txt","r") as f:
    for row in f:
        data = row.strip("\n").split("|")
        country,capital,cc,cc3,iac,timezone,currency = data
        country_info = {
            "name":country,
            "capital":capital,
            "cc":cc,
            "iac": iac,
            "timezone" :timezone,
            "currency": currency,
        }
        countries[country.casefold()] = country_info
# print(countries)

chosen_country = input()
if chosen_country.casefold() in countries:
    country_infos = countries[chosen_country]
    print(country_infos['capital'])
    