from functools import reduce
def max_in_list(list1):
    maximum=0
    for num in range(0,len(list1)):
        if int(list1[num])>int(maximum):
            maximum=list1[num]
    return maximum

def max_int(a,b):
    if (a>b):
        return a
    else:
        return b




if __name__ == "__main__":
    list1=input("enter a list").split()
    print(max_in_list(list1))
    result = reduce(max_int,list1)
    print(result)
    print(reduce(max,list1))
