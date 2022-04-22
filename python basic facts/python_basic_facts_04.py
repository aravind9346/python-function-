

#define default values in dictionaries with .get() and .setdefault()


my_dict = {"item": "football", "price": 10.00}
count = my_dict.get("count", 0)


count = my_dict.setdefault("count", 0)
print(count)
print(my_dict)