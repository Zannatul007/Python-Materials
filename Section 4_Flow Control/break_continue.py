bucket_list = ["Foundation","Mascara","Blush","Lipliner"]

item_to_find = input("Please enter your bucket item :")
found_at = None

# for i in range(len(bucket_list)):
#     if(bucket_list[i]==item_to_find):
#         found_at=i
#         break

for i in bucket_list:
    if (i == item_to_find):
        found_at = bucket_list.index(i)
        break


# #Without using for loop 
# if item_to_find in bucket_list:
#     found_at = bucket_list.index(item_to_find)

if found_at is not None:
    print("Item found in {}".format(found_at))
else:
    print("{} not found".format(item_to_find))




# l1 = ['a','b','c']
# ip = input()
# f = None
# if ip in l1:
#     f = l1.index(ip)
# if f is not None:
#     print(f'item found at {f}')
# else:
#     print('Not found')

