def max_of_three(varl1,val2,val3):
    if(val1>val2):
        if(val1>val3):
            return val1;
        else:
            return val3
    elif(val2>val3):
        return val2

if __name__ == "__main__":
    val1,val2,val3 = input("Enter any three values").split()
    result=max_of_three(val1,val2,val3)
    print("max value is",result)
