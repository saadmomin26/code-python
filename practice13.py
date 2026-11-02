# name=input("enter a name")
# marks=int(input("enter a marks"))
# phn=int(input("enter a pn no."))

# s="The name is { }, his marks is{ }, and phn no. is{ }".format
# (name,marks,phn)
# print(s)

# #Q3
# def divsible5(n):
#     if(n%5==0):
#         return True
#     return False
# a=[11,3,5,67,0,7,77,865,89,5,47,54,8778,0,34,68]

# f=list(filter(divsible5,a))
# print(f)

# #q4  grater num from list
# from functools import reduce
# l=[11,23,34,434,555,64,68,96,98,999]

# def grater(a,b):
#     if (a>b):
#         return a
#     return b
# print(reduce(grater,l))


#q7

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()