def histogram(list1):
    for num in list1:
        for asterick in range(0,num):
            print("*",end="")
        print("\n")

if __name__ == "__main__":
    inputlist=[]
    num=int(input("enter length of list"))
    for i in range (0,num):
        inputlist.append(int(input()))
    histogram(inputlist)
