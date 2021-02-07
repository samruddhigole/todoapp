def generate_n_chars(count,char):
    for num in range(0,count):
        print(char,end="")

def generate_n_chars_other(count,char):
    print(count*char)





if __name__=="__main__":
    count=int(input("enter count"))
    char=input("enter character to print")
    generate_n_chars(count,char)
    #generate_n_chars_other(count,char)
