my_list = [1, 6]

for i in my_list:
    first_neg_num = my_list
    if i in first_neg_num:
        print(i)
else:
    print("none")

 
# print words greater than five in length

list = ["Orange", "Apple", "Banana",]

for i in list:
  if(len(list))>5:
      print(list)
      

# add items to a list Q4

items = []
options = ""

while options != "4":
    print("select from options 1 - 4")
    print("1. Add item")
    print("2. Remove item")
    print("3. Show item")
    print("4. Quit application")

    options = input("select an option \n")

    match options:
        case "1":
             item = input("Enter the item \n")
             items.append(item)
        case "2":
             item = input("Enter item to remove from the list \n")
             items.remove(item)
        case "3":
             print(items)
        case "4":
            break

        
    
    
                       






