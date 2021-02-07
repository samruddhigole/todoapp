def is_member(character,list1):
    for char1 in list1:
        if character == char1:
             return "present"
    return("not")

if __name__=="__main__":
    list1=[]
    len_list1=int(input("enter length of list"))
    for i in range(0,len_list1+1):
        list1.append(input())
    print(is_member(input("enter a character to find"),list1))
