#multiple inheritance
class employee():
     company="ITC"
     name="harry"

     def __init__(self):
          pass
    
     def show(self):
          print(f"The name of the employee is:{self.name}")

class code():
     languagee="python"
     def printlanguage(self):
          print(f"out of the language here is your language:{self.languagee}")





class programmer(employee,code):
      company="ITC Info"
      language="java"
      def __init__(self):
           pass
      
      def showlanguage(self):
           print(f"The language is:{self.language}")


a= employee()
b=programmer()
a.show()
b.printlanguage()
b.showlanguage()
# c=code

print(b.company,b.company)