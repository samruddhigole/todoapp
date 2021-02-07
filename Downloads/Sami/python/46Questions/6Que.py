def sum(list1):
    result=0
    for num in list1:
        result=result+num
    return result

def multiply(list1):
    result=1
    for num in list1:
        result=result*num
    return result

if __name__ == "__main__":
    list1=[]
    n = int(input("enter the number of elements"))
    for num in range (0,n):
        element=int(input())
        list1.append(element)
    result=sum(list1)
    result1=multiply(list1)
    print(result,result1)




