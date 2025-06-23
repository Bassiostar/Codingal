file1 = open('C:/Users/hp/Desktop/Codingal/Python/lesson 13/codingal.txt', 'r')
file2 = open('C:/Users/hp/Desktop/Codingal/Python/lesson 13/codingalUpdated.txt', 'w')

for line in file1.readlines():
	
	if not (line.startswith('Coding')):
		
		print(line)
		
file2.write(line)

file2.close()
file1.close()
