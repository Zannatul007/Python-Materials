fruits = [
    ("Orange","good for skin"),
    ("Mango","good for sleeping"),
    ("Amlaki","good for hair"),
]

def my_hash(s:str)-> int:
    key = ord(s[0])
    return key%10

for key,value in fruits:
    new_hash = my_hash(key)
    print(key,new_hash)
    print("-"*90)
    print(key , hash(key))

