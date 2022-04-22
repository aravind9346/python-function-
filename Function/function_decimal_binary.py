def decimal_into_binary(decimal_1):
    decimal = int(decimal_1)

    print("the given decimal number", decimal, "in binary number is : ", bin(decimal))

def decimal_into_octal(decimal_1):
    decimal = int(decimal_1)

    print(oct(decimal))

def decimal_into_hexadecimal(decimal_1):
    decimal = int(decimal_1)

    print(hex(decimal))

#driver code

decimal_1 = int(input("enter decimal num: "))
decimal_into_binary(decimal_1)
decimal_into_octal(decimal_1)
decimal_into_hexadecimal(decimal_1)                