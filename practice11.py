# #Q1 creat a class (2-D vector)and use it to create another class representing a3-d vector
# class TwoDvector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
#     def show(self):
#         print(f"The vector is {self.i}+{self.j}j")

# class ThreeDvector(TwoDvector):
#     def __init__(self, i, j,k):
#         super().__init__(i, j)
#         self.k=k  
#     def show(self):
#         print(f"The vectoe is{self.i}+{self.j}+{self.k}k")

# a=TwoDvector(1,2)
# a.show()
# b=ThreeDvector(1,2,3)
# b.show()

#Q2creat a class pet from class animal and further create a class dog from pet add method "bark" to class "dog"
 
# class Animals():
#     pass
# class pets(Animals):
#     pass
# class Dog(pets):
#     @staticmethod
#     def bark():
#         print("Bow Bow")

# d=Dog()
# d.bark()

# #Q3 creat a class employee and add scalary and increment properties to it
# class employee():
#     salaey=234
#     increment=20
    
# e=employee()

# #Q4creat a class Employee and add scalary and increment properties to it.
# # write  amethod sclary afterincrement method with a@property decorated with a setter wich chananges the value of increment base on the sclary.

# class Employee():
#        salary=234
#        increment=20
#        @property
#        def salaryAfterIncrement(self):
#         return self.salary*(1+self.increment/100)
       
#        @salaryAfterIncrement.setter
#        def salaryAfterIncrement(self,salary):
#            self.increment=((salary/self.salary)-1)*100
       


# e=Employee()
# # print(e.salaryAterIncrement)
# e.salaryAfterIncrement=280.8
# print(e.increment)

# #Q5 write a class complex to represent complex number,along with overloaded operator'+' and"*" wich adds and multiplies them.
# class Complex:
#     def __init__(self,r,i):
#         self.r=r
#         self.i=i
#     def __add__(self,c2):
#         return complex(self.r+c2.r,self.i+c2.i)
#     def __add__(self,c2):
#         return complex(self.r+c2.r,self.i+c2.i)
#     def __str__(self):
#         return f"{self.r}+{self.i}i"
    
# c1=complex(2,3)
# c2=complex(4,5)
# c3=c2+c1
# print(c2*c2)

#  ##Q6
# class vector():
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def __add__(self,other):
#         result=vector(self.x+other.x,self.y+other.y,self.z+other.z)
#         return result
    
#     def __mul__(self,other):
#         result=(self.x+other.x,self.y+other.y,self.z+other.z)
#         return result
#     def __str__(self):
#         return f"{self.x}i+{self.y}j+{self.z}k"
  

 #test the implemetation 
# v1=vector(1,2,3)
# v2=vector(4,5,6)
# v3=vector(7,8,9)

# print(v1+v2)
# print(v1+v2)

# print(v1+v3)
# print(v1+v3)

#  #Q7
# class vector:
#     def __init__(self, l):
#         self.l = l

#     def __len__(self):
#         return len(self.l)

# v1 = vector([1,2,3])   # pass a list
# print(len(v1))         # will call __len__

