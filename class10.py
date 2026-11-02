class Employee:
 
    language="Py" # class atteibute
    salary=120000 
harry=Employee
harry.name="harry"# it is an instance attribute
print(harry.salary,harry.language)


rohan=Employee()
rohan.language="java"  # it is an instance attribute
rohan.name="rohan"# it is an instance attribute
print(rohan.language,rohan.salary,rohan.name)