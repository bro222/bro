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