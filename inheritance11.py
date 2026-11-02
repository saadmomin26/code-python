#inheritance
class employee():
     company="ITC"
     name="harry"

     def __init__(self):
          pass
    
     def show(self):
          print(f"The name of the employee is:{self.name}")

class programmer(employee):
      
    
      company="ITC Info"
      language="java"
      def __init__(self):
           pass
      
      def showlanguage(self):
           print(f"The language is:{self.language}")


#a= employee()
b=programmer()
#a.show()
b.showlanguage()

print(b.company,b.company)
