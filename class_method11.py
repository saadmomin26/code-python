#class method

class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"the value of a is {cls.a}")

e = Employee()
e.a = 45  # instance variable, doesn't affect the class variable
e.show()
