# list=used to store multiple items  in a single variable
food=['pizza','cabbage','carrots','porridge','corn','chapati']

#print(food[2])calls the item at index 2.

food[0]='sushi' #this replaaces the item at index 0 with sushi
# print(food[0])

food.pop()#this will remove the last item on the list
food.insert(0,'cake')#to insert a value at a given index
food.sort()#it will sort a list alphabetically

#remove, is used to remove a value from a list
food.remove('cabbage')
# append, adds an item to a list
food.append('ice cream')
food.clear()#it clears a list of  all of it's elements
#to display all the items found in a list we use a standard for loop
for x in food:
    print(x)
