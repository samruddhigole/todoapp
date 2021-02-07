def make_3sg_form(string):
    #print(string)
    newstring=""
    flag=0
    list1=["o","ch","s","sh","x","z"]
    if string.endswith("y"):
        newstring=string[:-1]
        newstring=newstring+'ies'
        print(string, newstring)
    else:
        for x in list1:
            if string.endswith(x):
                flag=1
                newstring=string+"es"
                print(string,newstring)
                break
        if(flag==0):
                newstring=string+"s"
                print(string,newstring)



if __name__ == "__main__":
    #string=input("enter an string")
    #make_3sg_form(string)
    make_3sg_form("try")
    make_3sg_form("fox")
    make_3sg_form("run")
