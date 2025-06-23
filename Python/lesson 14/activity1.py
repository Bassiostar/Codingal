new_file = open('Hi.txt', 'x')
new_file.close()

import os
print("Checking if my_file exists or not....")
if os.path.exists('Hi.txt'):
    os.remove('Hi.txt')
else:
    print("File does not exist")


my_file = open('Hi.txt', 'w')
my_file.write("Hi! I am a Penguin and I am 1 yr old")
my_file.close()

os.remove('Hi.txt')
os.rmdir('C:/Users/hp/Desktop/Codingal/Python/lesson 15')