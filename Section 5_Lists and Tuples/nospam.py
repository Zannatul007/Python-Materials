menu = [['eggs','bread','bacon','spam'],
         ['eggs','bread','bacon','chicken','spam'],
         ['eggs','bread','bacon','soup','spam'],
         ['eggs','bread','bacon','spam'],
         ['eggs','bread'],
         ['eggs','bread','bacon'],
         ['bacon','spam'],
         ['bacon','bread']
]

for meal in menu:
    for item in range(len(meal)):
        if(meal[item]=='spam'):
            del meal[item]
    print(meal)
     
for meal in menu:
    for item in range(len(meal)):
        if(meal[item]!="spam"):
            print(meal[item],end =', ')
    print()



