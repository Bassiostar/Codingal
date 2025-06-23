file = open('C:/Users/hp/Desktop/Codingal/Python/lesson 13/codingal.txt', 'r')
print(file.read())
file.close()

file = open('C:/Users/hp/Desktop/Codingal/Python/lesson 13/codingal.txt', 'r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open('C:/Users/hp/Desktop/Codingal/Python/lesson 13/codingal.txt', 'a')
file.write("Hi! I am a Penguin. I am 1 yr. old")
file.close()