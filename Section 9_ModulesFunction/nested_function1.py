def greeting_everyone(items:list):
    greeting_1 = "Hello!!!!!"
    def greeting(people):
        print(f"{greeting_1} {people}")
    for item in items:
        greeting(item)

name_list = ['Zane','Fane','Tane','kane']
greeting_everyone(name_list)