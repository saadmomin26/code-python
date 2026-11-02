#multilevel inheritance

class employee:
    def __init__(self):
        print("constructor of employee")
    a=1

class programmer(employee):
    def __init__(self):
        print("constructor of programmer")
    b=2

class manager(programmer):
   def __init__(self):
        super(). __init__ () # it is super it will prin programmer constructor
        print("constructor of manager")
   c=3

# o=employee()
# #print(o.a) #print a
# #print (o.b) #show error bzoc b is not in employee
# oa=programmer
# print(oa.a,o.a,oa.b,end="") #print a

m=manager()
print(m.a,m.b,m.c)
