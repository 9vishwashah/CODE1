class Employee:

    name = "vishwa" # A class attribute

    marks = 34

    center = "Delhi"

    def printObj(self):

        print(f"The name is {self.name}")

    

    @staticmethod

    def greet():

        print("good day")

Employee.name = "vishwashah" 

vishwa = Employee() 

shyam = Employee() 

print(vishwa.name) 

print(shyam.name)

shyam.name = "Shyam" 

print(shyam.name)

print(vishwa.name)

vishwa.greet()

Employee.greet()

