# f=open('sample.txt',"r")

# data=f.read() #read file
# print(data)

# f.seek(0) #move pointer to start

# data1=f.readline() #readline 
# print(data1)

# # f.seek(10)
# data3=f.readlines() #Reads all remaining lines into a list
# print(data3)

# f=open("sample2.txt","x")
# f.write("\nNew text appended to the file")
# f.close()

# f=open("sample.txt","r+")

# f.write("123")
# print(f.read())
# f.close()

# f1=open("sample.txt","r")
# print(f1.read())
# f1.close() 

with open("sample.txt","w") as f:
    f.write("this is the sample.txt in wrote mode have python written inside")

with open("sample.txt","r") as f:
    print(len(f.read()))


# delete files use OS module
# import os

# try:
#     os.remove("sample.txt")
# except FileNotFoundError:
#     print("Error: File not found")
# except PermissionError:
#     print("Error: NO permission to delete this file")


# else:
#     print("file deleted successfully")