#defining a function to calculate lcm

def calculate_lcm(x,y):
    #selecting the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0)and(greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm
# taking input from users

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

#printing the result for the users

print("the lcm of", num1,"and", num2,"is", calculate_lcm(num1,num2))
    