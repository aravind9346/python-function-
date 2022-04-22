squares = []
for i in range(10):
    squares.append(i*i)


print(squares)

#append = add an a item to the end of the list .
#the append() method in python adds a signal item to the existing list. it doesn't return
#a new list of items but wll modify the original list by adding
#the item to the end of the list.

#after executing th emethod append on the list the size of the list
#increases by one


#squares.append(i)


squares = [i*i for i in range(10)]
print(squares)
