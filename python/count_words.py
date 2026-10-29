def count_words(path):
    try:
        with open(path, "r" , encoding="utf-8" ) as f:
            text=f.read()
            return len(text.split())
    except FileNotFoundError:
        print(f"Error : File not found :{path}")
        return None

    except PermissionError:
        print(f"Error : permission Denied : {path}")
        return None

    except UnicodeDecodeError:
        print(f"Error : File is not valid UTF-8 text : {path}")
        return None



    
# # test 1
# print("valid File : ", count_words("sample.txt") , "words") 
# #  test 2
# print("Missing File : ", count_words("samples.txt"))
# #test 3
# print("Binary File : ", count_words("binary.bin"))
# #test
# print("Binary File : ", count_words("samples.png"))

def search_words(path,word):
    line = 1
    found = False

    try: 
        with open(path, "r", encoding="utf-8") as f:
            data = f.readline()

            while data:
                if word.lower() in data.lower(): 
                    print(f"Found '{word}' on line {line}")
                    found=True

                line+=1 
                data=f.readline()

            if not found:
                print("word not found")
            
    except FileNotFoundError :
        print(f"Error: File not found: {path}")

# search_words("sampe.txt","python")


# with open("numbers.txt" , "w") as f:
#     f.write("10\n 25 \n abc \n 7 \n 3.5 \n 40 \n hello \n15")

def sum_numbers(path):
    total=0
    ln=0

    try:
        with open(path,"r",encoding="utf-8") as f:
            for line in f:
                ln+=1

                try:
                    num=int(line.strip())
                    total+=num

                except ValueError:
                    print(f"Invalid number on line {ln} : {line.strip()!r}")

            print(f"sum of valid numbers : {total}")

    except FileNotFoundError:
        print(f"file not dfound {path}")

sum_numbers("numbers.txt")
