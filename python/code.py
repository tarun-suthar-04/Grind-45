f=open('sample.txt',"r")

data=f.read() #read file
print(data)

f.seek(0) #move pointer to start

data1=f.readline() #readline 
print(data1)

# f.seek(10)
data3=f.readlines() #Reads all remaining lines into a list
print(data3)

