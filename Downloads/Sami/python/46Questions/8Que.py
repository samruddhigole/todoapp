def palindrom(string):
    return string == string[::-1]

if __name__ == "__main__":
    string=input("enter a string")
    result=palindrom(string)
    if result:
        print ("Its an palindrom")
    else:
        print("Not a palindrom")
