data = [2,3,4,90,100,110,200,150,170,180,192,12,45,90,500,600,900]
data.sort()
print("Sorted Data {}".format(data))

min_shield = 100
high_shield = 200
stop_min = 0
stop_max = 0
for i in range(len(data)):
    if(data[i]>=min_shield):
        stop_min=i
        break
del data[:stop_min]
print(data)
for i in range(len(data)):
    if(data[i]>=high_shield):
        stop_max=i
        break
del data[stop_max+1:]

print("*"*90)
print(data)

