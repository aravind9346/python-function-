# sort complex itrerables with sorted()

#sorted()

from pickle import TRUE


data = [3, 5, 1 ,7, 10 , 66]
sorted_data = sorted(data, reverse=True)


print(sorted_data)

#python sorted() function returns a sorted list from the iterable 
#object

#sorted() sorts any sequence (list, tuple ) and always returns a list with the 
#elements in a sorted manner, without modifying the original 
#sequence

data =  [{"name": "max", "age": 6 },
         {"name": "lisa", "age": 14},
         {"name": "ben", "age": 9}]

sorted_data = sorted(data, lambda  x : x["age"])
print(sorted_data)         