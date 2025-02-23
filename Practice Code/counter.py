if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_arr1 = sorted(arr,reverse=False)
    sorted_arr1_set = set(sorted_arr1)
    print(sorted_arr1_set)
    second_max = list(sorted_arr1_set)[-2]
    print(second_max)