class Employee: 

    center = "Not known"

    def __init__(self, name, marks, center): 

        self.name = name 

        self.marks = marks 

        self.center = center 

    def printObj(self):

        print(f"The name is {self.name}")

        print(f"The marks is {self.marks}") 

        print(f"The center is {self.center}") 

    

    @staticmethod

    def greet():

        print("good day")

vishwa = Employee("vishwa", 34, "Delhi")

rohan = Employee("Rohan", 94, "Kolkata")

vishwa.printObj()

rohan.printObj()

