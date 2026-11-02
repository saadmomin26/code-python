
#    #Q1
# class programmer():
#      company="microsoft"
#      def __init__(self,name,sclary,pin):
#           self.name=name
#           self.sclary=sclary
#           self.pin=pin
        
         
# p=programmer("harry",12000,415515)
# print(p.name,p.sclary,p.pin,p.company)

# s=programmer("saad",12000,415515)
# print(s.name,s.sclary,s.pin,s.company)
    
  #Q2
# class claculater():
#     def __init__(self,n):
#         self.n=n

#     def square(self):
#         print(f"the square is{self.n*self.n}")
#     def cube(self):
#         print(f"the cube is{self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"the cuberoot is{self.n**1/2}")
    
    
# a= claculater(4)
# a.square()   
# a.cube()
# a.squareroot()

  #Q3
# class demo():
#     a=4
# o =demo()
# print(o.a)
# o.a=0
# print(o.a)
# print(demo.a)
# class demo():          # Define a class named 'demo'
#     a = 4              # 'a' is a class variable (shared among all objects unless overridden)

# o = demo()             # Create an object 'o' of class demo

# print(o.a)             # Step 1: This will print 4
#                        # It first looks for 'a' in the object 'o'
#                        # If not found, it uses the class variable demo.a

# o.a = 0                # Step 2: This creates an **instance variable** 'a' for object 'o' only
#                        # Now 'o' has its own 'a' = 0, separate from demo.a

# print(o.a)             # Step 3: This prints 0
#                        # Because now object 'o' has its own 'a'

# print(demo.a)          # Step 4: This still prints 4
#                        # The class variable 'a' is unchanged

  #Q4
# @staticmethod
# class greed():
#     print("hellow everyone")
# greed()

  #Q5

# from random import randint  
# class train:
    
#     def __init__(self, trainNo):       # Constructor to initialize train number
#         self.trainNo = trainNo         # Storing train number in object

#     def book(self, fro, to):           # Method to book a ticket
#         print(f"ticket is booked in train no:{self.trainNo} from {fro} to {to}")

#     def getStatus(self):               # Method to show train status
#         print(f"train no: {self.trainNo} is on time")

#     def getfare(self, fro, to):        # Method to calculate and show fare
#         print(f"Ticket fare in train no:{self.trainNo} from {fro} to {to} is {randint(222,555)}")

# # Creating an object of the train class with train number 2345
# t = train(2345)

# # Calling methods using the object
# t.book("satara", "sangli")
# t.getStatus()
# t.getfare("satara", "sangli")

   #Q6
# from random import randint  
# class train:
    
#     def __init__(sel, trainNo):       # Constructor to initialize train number
#         sel.trainNo = trainNo         # Storing train number in object

#     def book(self, fro, to):           # Method to book a ticket
#         print(f"ticket is booked in train no:{self.trainNo} from {fro} to {to}")

#     def getStatus(self):               # Method to show train status
#         print(f"train no: {self.trainNo} is on time")

#     def getfare(self, fro, to):        # Method to calculate and show fare
#         print(f"Ticket fare in train no:{self.trainNo} from {fro} to {to} is {randint(222,555)}")

# # Creating an object of the train class with train number 2345
# t = train(2345)

# # Calling methods using the object
# t.book("satara", "sangli")
# t.getStatus()
# t.getfare("satara", "sangli")


n= int(input("emter a num"))

for i in range(1, n+1):
    
  print(" " * (n-i),end="")
  print("*"*(2*i-1))