# class Animal:
 
#     # name = "Buddy" #attribute

#     def __init__(self, name):
#         self.name = name

#     # method
#     def speak(self, sound):
#         print(f"woff {self.name} says {sound}") 

# # object/instance of the class
# animal1 = Animal("Buddy")
# print(animal1.name)
# animal1.name = "HUSKY"
# animal1.speak("meaaawww") 

# class Car:

#     type = "Toyaota" #attribute

#     def __init__(self, year):
#         self.name = year
         
#     # method
#     def drive(self):
#         print(self, "year")
    
#     # object/instance
#     Car = Car("Toyota")
#     print(Car.type)


# class Calculator:

#     def __init__(self):
#         num1, num2

#     def add(num1 + num2):
#      def subtraction(num1 - num2):
#       def division (num1 ):

class Calculator:
    def _init_(self, num1, num2):
     self.num1 = num1
     self.num2 = num2
      
    def add(self,num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(f"the sum of the two digits is: {self.num1 + self.num2}")

    def multiplication(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(f"the product of the two digits is:{self.num1 * self.num2}")

    def subtraction(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(f"the difference of the two digits is:{self.num1 - self.num2}")

    def division(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(f"the difference of the two digits is:{self.num1 / self.num2}")

result = Calculator()
result.add(2,4)
result.multiplication(2, 4)
result.subtraction(8, 4)
result.division(5, 2)
