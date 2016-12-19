st = open('sampletext.txt', 'r+')
words = open('words.txt', 'r+')

#print(words.read())
#words.seek(0)
#print(words.read())

#for line in st:
#    print(line, end=" ")

#st.seek(0)
#print(st.read())

newfile = open('write.txt','w')
newfile.write("new lines much")
newfile.close()