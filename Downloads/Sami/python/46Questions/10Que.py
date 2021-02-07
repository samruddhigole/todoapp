def overlapping(list1,list2):
    for l1 in list1:
        for l2 in list2:
            if l1==l2:
                return print("True")
    return print("False")

if __name__ == "__main__":
    list1=[]
    list2=[]

    len_list1=int(input("enter length of list1"))
    len_list2=int(input("enter length of list2"))

    for i in range(0,len_list1):
        list1.append(input())

    for i in range(0,len_list2):
        list2.append(input())

    overlapping(list1,list2)




