if __name__ == '__main__':
    N = int(input())
    new_list = []
    new_dict ={}
    number_list = []
    for i in range(N):
        command= input().strip().split()
        if(command[0] == "insert"):
            new_list.insert(int(command[1]),int(command[2]))
        elif(command[0] == "remove"):
            new_list.remove(int(command[1]))
        elif(command[0] == "append"):
            new_list.append(int(command[1]))
        elif (command[0] == "sort"):
            new_list.sort()
        elif(command[0] == "reverse"):
            new_list = new_list[::-1]
        elif(command[0] == "pop"):
            new_list.pop()
        else:
            print(new_list)


