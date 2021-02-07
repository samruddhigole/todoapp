def len_of_string(string):
    var=0
    for str1 in string:
        var=var+1
    return var

if __name__ == "__main__":
    string=input("enter a string")
    result=len_of_string(string)
    print(result)
