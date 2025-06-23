outputFile = open('UpdatedFile.txt', 'w')

inputFile = open('C:/Users/hp/Desktop/Codingal/Python/lesson 14/repeated.txt', 'r')

lines_seen_so_far = set()
print("Eliminating duplicate lines....")
for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)

inputFile.close()
outputFile.close()