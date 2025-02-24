if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum1 = 0
    for key,value in student_marks.items():
        if key ==query_name:
            for i in range(len(value)):
                sum1+=value[i]
    avg = sum1/3
    print("{:.2f}".format(avg))