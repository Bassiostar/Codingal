with open('C:/Users/hp/Desktop/Codingal/Python/lesson 13/codingal.txt', 'w') as file:
    file.write("Hi! I am a Penguin and I am 1 yr old")
file.close()

with open('C:/Users/hp/Desktop/Codingal/Python/lesson 13/codingal.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print(word)
file.close()