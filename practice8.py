 #Q1
 # a=int(input("Enter a num:"))
# b=int(input("Enter a num:"))
# c=int(input("Enter a num:"))

# def gretest(a,b,c):
#     if (a>b and a>c):
#         return a
#     elif (b>a and b>c):
#         return b
#     elif (c>a and c>b):
#         return c
# print(gretest(a,b,c))
   #Q2
# def f_to_C(f):
#     return 5*(f-32)/9
# f=int(input("enter temperatuer in F:"))
# c=f_to_C(f)
# print(f"{round(c,2)}°c")
  #Q3
# print("a")
# print("b")
# print("c",end="")
# print("d",end="") #it will avoid new line
 #Q4
# def natural(n):
#     if(n==1):
#         return sum(n-1)+n
# print(sum(4))
  

 #Q5  
# def pattern(n):
#     if n == 0:
#         return
#     print("*" * n)
#     pattern(n - 1)
# pattern(3)

 #Q6
# def inc_to_cm(inch):
#     return inch *2.54
# n=int(input("Enter value in inches:"))
# print(f"THE correspondin value in cms is:{inc_to_cm(n)}")

    #Q7
# def rem(l,word):
#     n=[]
#     for item in l:
#         if not(item ==word):
#             n.append(item.strip(word))

#     return n
# l=["saad","rohan","subham","an"]
# print(rem(l,"an"))

 #Q8
def muliply(n):
    for i in range(1,11):
        print(f"{n}x {i}={n*i}")
muliply(5)
