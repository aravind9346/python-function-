

#count hashable objects cith collections.counter

from collections import Counter

my_list = [10,10,10, 22,22,33,4,5,5,66]
counter = Counter(my_list)

most_common = counter.most_common(1)
print(most_common)

print(counter)


#counter is help to count number elements in a list to count to count help 
#the list cont