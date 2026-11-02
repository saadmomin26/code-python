# #Q1)
# try:
#     with open ("1.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:    
#     with open ("2.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:
#     with open ("3.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# print("thank you")

# #q2)
# l=[1,2,3,4,5,6,7,8]

# for i, item in enumerate(l):
#   if i == 2 or i==4 or i==6:
#       print(item)

# #Q3)
# n=(int(input("enter a num")))
# table =[ n*i for i in range (1,11)]
# print(table)

# #Q4)

# try: 
#     a=int(input("enter a:"))
#     b=int(input("enter b:"))
#     print (a/b)
# except ZeroDivisionError as z:
#     print("infinite")
    
#q5)
n=(int(input("enter a num")))
table =[ n*i for i in range (1,11)]
print(table)
with open("table12.txt", "a") as f:
    f.write(str(table)+"\n")

