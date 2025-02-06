# declare tuple 
fruits = ('mango','apple','banana')
print(fruits)
print(type(fruits))

single_fruit = ('apple')
print(type(single_fruit))

single_fruit_tuple = ('apple',)
print(type(single_fruit_tuple))

str_tuple = ("a","b","c")
bool_tuple = (True,False,True)
int_tuple = (1,2,3,4,5)
mixed_tuple = ("a",1,0,True)
print(str_tuple,mixed_tuple,int_tuple,bool_tuple)


#Tuple constructor 
print("Tuple Constructor")
list_1 = ['a','b','c','d']
tuple_list_1 = tuple(list_1)
print(tuple_list_1)
print(type(tuple_list_1))
print("-"*90)


#Changing Tuple values - At first convert it to list then change the list then change the list to tuple
original_tuple = (1,2,3,4,5,'zannatul')
list_2 = list(original_tuple)
list_2[0] = "Apple"
changed_tuple = tuple(list_2)
print(changed_tuple)
# same method for append 
list_2.append("Fardaush")
changed_tuple_2 = tuple(list_2)
print(changed_tuple_2)

#alternative approach to add new values in tuple
new_tuple = ("apple","banana","orange")
original_tuple+=new_tuple
extended_tuple = original_tuple
print(extended_tuple)

#delete one item from tuple 
extended_tuple=list(extended_tuple)
extended_tuple.remove(extended_tuple[1])
print(extended_tuple)