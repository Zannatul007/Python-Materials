import csv
albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]


key = ['Album','Artist','Release Data']

with open("EditedAlbums.csv",'w',encoding='utf-8',newline='') as write_file:
    csv_write_file = csv.DictWriter(write_file,fieldnames=key)
    csv_write_file.writeheader()
    for row in albums:
        zip_object =dict(zip(key,row))
        print(zip_object)
        csv_write_file.writerow(zip_object)

        # print(zip_object)
        # for thing in zip(key,row):
        #     print("\t",thing)
