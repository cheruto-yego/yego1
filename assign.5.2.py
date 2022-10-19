hat_list=[1,2,3,4,5]
user_input=int(input('please enter any number of your choice: '))
#allows user to enter a number of his choice
print(hat_list)
hat_list.pop(2)
#removes the  second index on the list=3
print('removes the middle number',hat_list)
hat_list.insert(2,user_input)
#inserts user input in the place of the second index that was removed
print('inserts user input',hat_list)
hat_list.pop(-1)
#removes the last item on the list
print('removes the last item on the list',hat_list)

print('the length of the hat_list ',len(hat_list))
print(hat_list)