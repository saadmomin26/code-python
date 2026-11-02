class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"the value of a is {cls.a}")
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

e = Employee()
e.a = 45  #instance variable, doesn't affect the class variable

e.name="harry code"
print(e.name)
e.show()
# appstraction implemantation detail hide from user
# incapsulation  working componentens are packed in perticuler unit 
#     ex :- in this case is class
