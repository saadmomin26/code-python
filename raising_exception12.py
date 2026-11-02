
#rasing exception
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

if (b==0):
    raise ZeroDivisionError("hey our program is not allow to division number by zero")
else:
    print(f"the division a/b{a/b}")