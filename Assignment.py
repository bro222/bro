# try:
#     age = int(input("Enter your age:")) 

#     match age:
 
#         case age if age >= 18:
#             print("you are eligible to vote")
#         case age if age < 18:
#             print("you are not eligible to vote")

# except ValueError:
#             print("invalid age entered; Enter a correct age!")

 

# age = int(input("Enter your age"))

# if (age >= 18):
#     print("Iam eligible to vote")
# else:
#     print("you are not eligible to vote")

# item_price = float(input("Enter the price"))
# discount_amount = float(item_price * 20 / 100)

# match item_price:
#     case item_price if item_price > 100:
#         print(f"your discount is: $ {item_price - discount_amount: .2f}")
#     case _:
#         print("No discount")


# hotel management system
# creat a room

# def creat_room(room_number, price, is_booked=False):
#     room_dict = {"room_number": room_number,"price": price, "is_booked": is_booked}
#     "rooms".append(room_dict)

#     return "rooms"

# # book a room
# def book_room(rooms, room_number):
#     for room in rooms:
#         if room["room_number"] == room_number and room["is_booked"] == True:
#          return "room is booked"
#         elif room["room_number"] == room_number:
#            room["is_booked"] = True
#            return "Room booked successfully"
#         else:
#             return "room does not exist"

            
# # hotel management system
# task = []

# def add_task():

#  title = input("Enter task,title:")
#  description = input("Enter task description:")
#  "task".append["title": "titles", "description:" "description"]
 
#  return "successful"


# # add task
# def add_task(task_name, due_date, priority):
    
#     for task in "tasks":
#         if task["task_name"] == task_name:
#             return "Task already exixt"
        
#     task.append({"task_name":task_name, "due_date": due_date, "priority": priority})

#     return "Task added successfully"

# # remove task
# def remove_task(task_ID):
#     for task in task:
#         if task["task_name"] == "task_id":
#             "tasks".remove(task)

#     return "Task not found"


# # update task
# def update_task(task_id, new_task_name, new_date, new_priority):
#     for task in "tasks":
#         if task["task_name"] == task_id:
#             task["task_name"] == new_task_name
#             task["due_date"] == new_date
#             task["priority"] == new_priority

#             return "Task update successfully"  


# # contact book

# class ContactBook:
#     contact_details = {}
#     def add_contact(self, name, phone):
#         self.contact_details[name] = phone
#         print(self.contact_details) 


#     def remove_contact(self, name):
#          if name in self.contact_details:
#              return self.contact_details.pop(name)

#     def view_contact(self):
#         print(self.contact_details)

# person_details = ContactBook()
# person_details.add_contact('Alice', '123-456-789')
# person_details.add_contact('James', '123-456-789')
# person_details.remove_contact('Alice')
# person_details.view_contact()



# #counter

# class Counter:
#     Counter = 0
#     def increament(self):
#         self.counter += 1
#         return self.counter
    
#     def decreament(self):
#         self.counter -= 1
#         return self.counter
   
#     def reset(self):
#         self.counter = 0

#     def show(self):
#         print(self.counter)


# counter = Counter()
# counter.increament()
# counter.increament()
# counter.decreament()
# counter.reset()
# counter.show()
        




# assigment 30 / 08 / 25
class Books:
    def __init__(self, title, auhtor, isbn, available_copies):
        self.title = title
        self.author = auhtor
        self.isbn = isbn
        self.available_copies = available_copies

    def display_info(self):
        print(f"Title:{self.title}, Author:{self.author}, ISBN:{self.isbn}, Available_Copies:{self.available_copies}")

        

class Member():
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
    
    def borrowed_book(self, book):
        if book.available_copies > 0:
            self.borrowed_books.append(book.title)
            book.available_copies -= 1
        else:
            print("No Book available")
    
    def return_book(self, book):
        if book.title in self.borrowed_books:
            self.borrowed_books.remove(book.title)
            book.available_copies += 1


class Library:
 books = []
 def add_book(self, book):
     self.books.append(book)

 def search_book(self, title):
     for book in self.books:
         if book.title == title:
          return book
     
 def display_book(self):
    if self.books == []:
        print('No book available')
    else:
         for books in self.books:
             books.display_info()

lib = Library()

b1 = Books("Python", "Guido Van Russom","123-245", 10 )
b2 = Books("Metcaf", "Gideon", "123-456", 10)
b3 = Books("Foundamentals", "Brown", "123-678", 10)

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

mem1 = Member(123, "Felix")
mem2 = Member(456, "Mark")

borrowed_books = lib.search_book("Metcaf")
if borrowed_books:
    mem1.borrowed_book(borrowed_books)
    mem2.borrowed_book(borrowed_books)
    lib.display_book()
    print("\n")

if borrowed_books:
    mem1.return_book(borrowed_books)
    lib.display_book()
    print("\n")

    print(mem2.borrowed_books)
    print("\n")

    print(mem1.borrowed_books)

    b1.display_info()
    b2.display_info()
    b3.display_info()


class Jokes:
 
    jokes=["- Why don’t exam papers ever get lonely? They always have multiple choices.",
           "- Why did the biology student bring a ladder to class? Because they heard the grades were at a higher level.",
           "- What’s a chemist’s favorite type of joke? A reaction that gets a good laugh.",
           "- I asked the librarian if the library had books on paranoia.She whispered, “They’re right behind you…"]
    def return_joke(self,index):
        return self.jokes[index]
class BirthdayWishes:
    birth_wish=["I wish for peace","I wish for good health","I wish for joy","I wish for Wisdom"]
    def return_wish(self,index):
        return self.birth_wish[index]
class BirthdaySuprise:
    # Jokes.jokes
    # BirthdayWishes.birth_wish
   def return_joke_or_wish(self,your_choice,index):
        if your_choice.lower()=="wish" and index<=3:
            return BirthdayWishes.birth_wish[index]
        elif your_choice.lower()=="joke" and index<=3:
            return Jokes.jokes[index]
        elif your_choice.lower()!="wish" and your_choice.lower()!="jokes":
            return "invalid choice ,type wish or jokes"
        else:
            return "index out of range"

choice=input("enter wish or joke :")
try:
    want=int(input("enter your index from 0 to 3 :"))     
except Exception :
    print("numbers only,")



joke1=Jokes()
b=BirthdayWishes()
# print(b.return_wish(1))
# print(joke1.return_joke(1))
suprise=BirthdaySuprise()
try:
    print(suprise.return_joke_or_wish(choice,want))
except Exception as v:
    print(" something is wrong ==",v)



    class Student:
     def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        
     def __str__(self):
        return f"{self.name} (ID: {self.student_id})"
    
class Course:
    students = []
    count = 0
    def __init__(self, course_name, course_code, max_capacity = 10):
        self.course_name = course_name
        self.course_code = course_code
        self.max_capacity = max_capacity
        
    def add_student(self, student):
        for i in self.students:
            if i.student_id == student.student_id:
                return "Student already exist"            
        else:
            
            self.students.append(student)
            self.count += 1
            print("student added successfully")
        return self.students
    
    def get_student_count(self):
        return self.count

    def is_full(self):
        if self.count == self.max_capacity:
            return True
        
    def list_students(self):
        print(self.students)
    
    def __str__(self):
        return f"{self.course_name} ({self.course_code}) - Enrolled: {self.count}/{self.max_capacity}"
        
                
st1 = Student("Alice", "S001")
st2 = Student("Jose", "S002")
print(st1.__str__())
cous = Course("Maths", "MATH101")
cous = Course("Algebra", "MATH102")
cous.add_student(st1)
cous.add_student(st2)
print(cous.get_student_count())
print(cous.__str__())