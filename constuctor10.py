class Employee:
    language = "Py"      # class attribute
    salary = 120000      # class attribute

    def gerInfo(self):   # instance method
        print(f"the name is:{self.name} The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod  #this method will con consider any objet from this code
    def greet():
        print("GOOD MORNING")

    def __init__(self,name,sclary,language):
        self.name=name
        self.salary=sclary 
        self.language=language
        print(" it is an dunder method ") # this met is atomatically called
    

# Creating an instance of Employee
harry = Employee("saad","130000","java")
harry.name = "harry"       # instance attribute
print(harry.salary, harry.language)  # accessing class attributes



# Calling method using correct instance
harry.gerInfo()  # Output: The language is Py. The salary is 120000

