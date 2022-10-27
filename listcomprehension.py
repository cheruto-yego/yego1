#list comprehension , is a way to create a new list with less code
# example of long code
# list=[expression for item in iterable]

#this is a long for loop for lists
# squares=[]#creates an empty list
# for i in range(1,11):#create a for loop
#     squares.append(i*i)#define what each loop iteration should do
#     print(squares)

# this is how a the code appears after list comprehension
squares=[i*i for i in range(1,11)]
print(squares)

students=[100,90,80,70,60,50,40,30,20,0]
passed_students=list(filter(lambda x: x>=60, students))
passed_students=[i for i in students if i >=60]
print