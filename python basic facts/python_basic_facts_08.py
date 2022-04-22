

#merge dictionaries with {**d1, **d2} (3.5+)

#mege two dictionaries 


d1 = {"name": "aravind" , "age": 23}
d2 = {"name": "anubolu", "age": 22}
merge_dict = {**d1, **d2}  # adding 2 set of dict with extention of value which helps sequence date 
print(merge_dict)