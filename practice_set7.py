
  #Q1
# n = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")
  

# #Q2
# l=["harry","Saad","Sachin","rahul"]

# for name in l:
#     if (name.startswith("S")):

#       print(f"hello {name}")

 #Q3 
# n=int(input("Enter a num:"))
 
# i=1
# while(i<11):
#     print(f"{n}x{i}={i*n}")
#     i+=1

 #Q4
# n=int(input("Enter a num:"))

# for i in range(2,n):
#     if(n%i) ==0:
#         print("Number is not prime")
# else:
#     print("number is prime")

 #Q5
# n=int(input("Enter a num:"))
# i=1
# sum=0
# while(i<=n):
#     sum += i
#     i+=1
# print(sum)

 #Q6
# n=int(input("Enter a num:"))
# product=1
# for i in range(1,n+1):
#     product=product*i
# print(f"The factorial of {n} is {product}")

 #Q7
# n=int(input("Enter a num:"))
# for i in range(1,n+1):
#   print(" "*(n-i),end="")
#   print("*"*(2*i-1),end="")
#   print("")

  #Q8
n=int(input("Enter a num:"))
for i in range(1,n+1):
 # print(" "*(n-i),end="")
  print("*"* i,end="")
  print("")

#  #Q9
# n=int(input("enter a num:"))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n,end="")
#     else:
#      print("*",end="")
#      print(" "*(n-3),end=" ")
#      print("*",end="")
#     print("")
  

#  #Q10
# n=int(input("enter a num:"))
# for i in range(1,11):
#     print(f"{n}x{11-i}= {n*(11-i)}")
#     # 1,10
#     # 2,9
#     # 3,8  #they have a sum 11 so 11-i
#     # 4,7