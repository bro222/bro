#  # Files opening with open function
# file = 'data.txt'
# content = open(file, 'r')
# print(content.read())
# content.close()


 # Files - error handling
 
# file = None
# try:
#  file = open('data.txt', 'r')
#  print(file.read())

# except FileNotFoundError:
#     print('File not found')

# finally:
#  if file:
#    file .close()


# # with open
# with open('data.txt', 'r') as file:
#     print(file.read())

# writing to a file
with open('data.txt', 'w') as file: 
    file.write('Hello world\n')
    file.write('Hello world again')