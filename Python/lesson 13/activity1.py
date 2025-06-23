file_read = open('C:/Users/hp/Desktop/Codingal/Python/lesson 13/codingal.txt', 'r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_write = open('C:/Users/hp/Desktop/Codingal/Python/lesson 13/codingal.txt', 'w')
file_write.write("File in Write Mode ......")
file_write.write("Hi! I am a Penguin. I am 1 yr. old")
file_write.close()

file_append = open('C:/Users/hp/Desktop/Codingal/Python/lesson 13/codingal.txt', 'a')
file_append.write("\nFile in Append Mode ......")
file_append.write("Hi! I am a Penguin. I am 1 yr. old")
file_append.close()
