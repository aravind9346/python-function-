#defining the a functio to calculate HCF 

def calculate_hcf(x,y):

    #selecting the smaller number

    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1,smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

#taking input from user


num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

#printing the result for the users
print("the hcf of ", num1 , "and", num2, "is", calculate_hcf(num1,num2))