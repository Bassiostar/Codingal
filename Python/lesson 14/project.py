with open('C:/Users/hp/Desktop/Codingal/Python/lesson 13/sample_file.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print(word)
file.close()
