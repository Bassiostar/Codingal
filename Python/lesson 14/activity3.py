with open('C:/Users/hp/Desktop/Codingal/Python/lesson 13/codingal.txt') as fp:
    data1 = fp.read()

with open('C:/Users/hp/Desktop/Codingal/Python/lesson 14/sample_doc.txt') as fp:
    data2 = fp.read()
data1 += "\n"
data1 += data2
print("Merging two files....")
with open('C:/Users/hp/Desktop/Codingal/Python/lesson 14/merged_file.txt', 'w') as fp:
    fp.write(data1)