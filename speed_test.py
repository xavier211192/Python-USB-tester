
import os
import time
filesize = int(raw_input("Enter Size of file to copy(1,2,5) in MB "))
numberofFiles = int(raw_input("Enter number of files you would like to make"))
#print filesize
bsize = filesize *1024000 #convert mb to bytes( each character is one byte)



'''This code below creates empty string list and appends letters into it until the desired size is reached'''
a=[]  #empty list
for i in range(bsize):    
    a.append('KX')
    #print a[i]


''' This code starts recording time and for the number of files specified
creates new text file and writes each character in list to this text file.
Finally subtracts the time and prints time taken for whole execution'''
start_time = time.time()
for x in range(numberofFiles):
    filename = str(x+1)+'karishma.txt'
    #print filename
    f = open(filename,'w')
    for item in a:
        f.write(item)
    f.close()
    size = os.stat(filename).st_size  #Change this path to
    #size = os.stat('C:\\Users\\Prashanth\\Desktop\\Python\\'+filename).st_size  #Change this path to
    print "Size of file",x+1," written is",size/1000,"KB" # get size of this file
elapsed_time = time.time() - start_time
print "Total Time to write",elapsed_time,"seconds."



