data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]


import os 
file_name = "flowers.txt"
directory_file= os.path.join("D:\Python Materials\Reading and Writing Files",file_name)

with open(directory_file,"w") as f:
    for plant in data:
        print(plant)
        print(plant,file=f)

new_list = []

with open(directory_file) as f:
    for data in f:
        new_list.append(data.rstrip())


