with open("names.txt","w",encoding="utf-8") as f:
    print('Enter 5 names  :')
    for i in range(0,5):
        name=input(f"{i+1} : ")
        f.write(f"{name}\n")

with open("names.txt" , "r",encoding="utf-8") as f:
    data=f.read()
    print(data)    