#multilevel inheritance

class employee:
    a=1

class programmer(employee):
    b=2

class manager(programmer):
   c=3

o=employee()
#print(o.a) #print a
#print (o.b) #show error bzoc b is not in employee
oa=programmer
print(oa.a,o.a,oa.b,end="") #print a

m=manager()
print(m.a,m.b,m.c)