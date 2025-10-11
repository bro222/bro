# Tuple

my_tuple = (1, 2, 3)
for i in my_tuple:
    print(i)

# Set

my_set = {"hello" , 1, 2, 1, False, 0}
print(my_set)
a = "beef"
my_set.add(a)
my_set.add("mutton")
# looping
for i in my_set:
 print(i)



a = {1, 2, 3}
b = {2, 3, 4}

# union
print(a | b)
# intersection
print(a & b)
# difference
print(a - b)
# symmetric difference
print(a ^ b)

# dictionary
person_one = {"name": "Kofi", "age": 26}
person_two = dict(name = "Yaw", age = 56)
print(person_one)
print(person_one["name"])
print(person_one["age"])
print(person_two)
print(person_two.keys())
print(person_two)
person_two["name"] = "Abena"
print(person_two)
person_two["gender"] = "female"
print(person_two)


for key in person_one:
   print(person_one[key])
   
# add items to tuples
my_tuple = (1, 2, 4, 4, 5)
my_list = list(my_tuple)
print(my_tuple)
my_list.append("hello")
print(list)  
my_tuple = tuple(my_list)
print(my_tuple)


#Functions 
def greet():
   print("Welcom Felix")

 #call/invoke
greet()

def sum(num1, num2):
   print(num1 + num2)

sum(2, 3)
sum(25, 30)

def divide(num1 = 10):
   print(num1 / 2)

divide(20)
divide()


def sum_num(numbers):
   sum = 0
   for number in numbers:
      sum += number
    
   print(sum)
   
sum_num([1,2,3,4,5])

def sum(num1, num2):
     print(2 + 4)

     sum()