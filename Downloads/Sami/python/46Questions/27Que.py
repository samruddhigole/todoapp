def map_for(list1):
    l1=0
    l2=0
    newlist=[]
    for word in list1:
        newlist.append(len(word))

    print(newlist)

def using_map(a):
    newlist=[]
    newlist.append(len(a))
    return newlist

#def list_comprehension(list1):



if __name__ == "__main__":
    list1=["sushil","arati","samruddhi","rt"]
    map_for(["sushil","arati","samruddhi","rt"])
    result=map(using_map,list1)
    print(list(result))



