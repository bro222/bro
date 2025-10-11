# Looping

name = "kofi"

for i in name:
    print(i)

for i in range(10):
    print("i wont talk in class again")

    # while loop

    count = 1
    while count <= 10:
        print(f"{count}: Hey")
        count += 1 


# nested for loop
for i in range(5):
     print(i)
     for j in range(5):
      print(j)


# breaking the loop program    
      program = "python"

      for i in program:
          if i == "h":
              break
          print(i)

program = "python"

for i in program:
    if i == "h":
        continue
    print(i)


# password checker

password = " "

while password != "secret":
    password = input("Enter password: \n")
print("Access granted")

#print vowels

word = "kofi"

for i in word:
    vowels = "aieouAIEOU"
    if i in vowels:
       print(i)



# data structures (List)

fruits = ["apple","banana","cherry"]
numbers = [1, 2, 3]
mixed = ["hrllo", 42, True]

# accessing the values 
print(fruits[0]) # element
print(fruits[-1]) # element

# add
print(fruits)
fruits.append("Orange")
fruits.append
print(fruits)

# using insert/remove/pop
print(fruits)
fruits.append("Orange")
print(fruits)
fruits.insert(1, "Mango")
print(fruits)


for i in fruits:
    print(i)


print(len(fruits))

i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

fruits = ["apple","banana","cherry"]
numbers = [1, 2, 3]
print(fruits)
fruits.append("potatoes")
numbers.append(4)
for i in fruits, numbers:
    print(i)

# example on list
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = []
[sum == 0]
for i in num:
    if i % 2 == 0:
     my_list.append(i)
     sum += i


print(my_list)
print((sum))

        




    


