file = open("list.txt",'w')
#open file to write

for index in range (10):
#For loop 10 times

    obj = input("Enter " + str(index+1) + "th object : ")
    #Prompt user for input
    
    file.write(str(index+1) + " " + obj +"\n")
    #Write input to file

file.close()
#Close file