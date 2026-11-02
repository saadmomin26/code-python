##this proram is import in main12.py file
# def myfunc():
#     print("hellow world")
# #if this code is directly executed by running the file its present in
# if __name__=="__main__":
#     print("we are directly running this code")
# myfunc()
# print(__name__)


# ##global keyworld
# a=80
# def fun():
#     global a # global varible is used to change "a" value it will be come 3
#     a=3
#     print(a)
# fun()
# print(a)

##enumerate function
l=[3,445,242,6674]

# index=0
# for item in l:
#     print(f"the iteam num at index {index} is {item}")
#     index+=1
##this can be done by enumerate function

for index, item in enumerate(l):
    print(f"the item number at index {index} is {item}")