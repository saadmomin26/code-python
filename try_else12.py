# try:
#     a=int(input("hey,Enter a number: "))
#     print(a)


# except Exception as e:
#     print(e)

# else:
#     print('i am inside else') #if try block run then it will come inside else block

#finally
def main():
 try:
    a=int(input("hey,Enter a number: "))
    print(a)


 except Exception as e:
    print(e)

 finally:
    print('i am inside finally') #finally will run always it is used in function
main()