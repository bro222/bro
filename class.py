
# how to handle errors

#try:
#print(3/0)
# except Exception:

# try
# try:
#    num = float(input('Enter a number'))
#    #print(10 / num)
# except ValueError as ex:
#     print("an error occured: ", ex)
# except ZeroDivisionError as ex:
#     print(ex)
# else:
#     print(10 / num)
# finally:
#     print("kristos")


# try:
#     age = int(input("Enter your age:"))

#     match age:

#         case age if age >= 18:
#             print("you are eligible to vote")
#         case age if age < 18:
#             print("you are not eligible to vote")

# except ValueError:
#             print("invalid age entered; Enter a correct age!")


# Inheritance 30/Aug/2025

# class Animal:
#     def __init__(self, name, age, species):
#         self.name = name
#         self.age = age
#         self.species = species

#     def speaks(self, sound):
#         print(f'My {self.name} says {sound}')

#     def eat(self):
#         print('The animal is eating beans')
    
# class Fish(Animal):
#     def swim(self):
#         print('I am swimming')
 
# class Dog(Animal):
#    def speaks(self):
#        print('The dog says woof')
#        super().speaks('Meow')

# tuna = Fish('Evans', 2, 'Onga') 
# tuna.speaks('Prrrr')
# tuna.swim()

# dog = Dog('Obra', 5, 'pomo')
# dog.speaks()


# Polymorphism
# Duck type:

# class Animal:
#  alive = True
    
# def speak(self, sound):
#     pass

# class Dog:
#    def speaks(self):
#       return 'Woof'

# class Car:
#    def speaks(self):
#       return 'Vrooom'
   
# objs = [Car(), Dog()]
# for obj in objs:
#    print(obj.speaks())

# def make_sound(sound):
#    print(sound.speaks())

# a = Dog()
# b = Car()
# make_sound(a)
# make_sound(b)

# # method overloading:

# class Calculator:
#     def sum(self, num1 = None, num2 = None, num3 = None):
#         if num1 != None and num2 != None and num3 != None:
#             print(num1 + num2 + num3)
#         elif num1 != None and num2 != None:
#             print(num1 + num2)
#         elif num1 != None:
#             print(num1)
#         else:
#             print(0)

# calc = Calculator()
# calc.sum(2,3,5)
# calc.sum(2,3)
# calc.sum(2)
# calc.sum(0)

# Operator Overloading:

# class Calculator:

#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def __add__(self, other):
#         return Calculator(self.num1 + other.num1, self.num2 + other.num2)

# calc1 = Calculator(2,3)
# calc2 = Calculator(4,5)

# sum = calc1 + calc2
# print(sum.num2)




        


 
    



    
    


        