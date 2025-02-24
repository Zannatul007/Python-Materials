if __name__ == '__main__':
    dict1 = {}
    number_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dict1[name] = score
    
    for key,value in sorted(dict1.items()):
        number_list.append(value)
    
    number_list = list(set(number_list))
    number_list.sort()
    name_list = []
   
    second_highest = number_list[1]
    for key,value in dict1.items():
        if second_highest == value:
            name_list.append(key)
            
    for i in sorted(name_list):
        print(i)