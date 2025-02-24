if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_set = set(arr)
    arr_set_list = list(arr_set)
    arr_set_list.sort()
    print(arr_set_list)
    print(arr_set_list[-2])
