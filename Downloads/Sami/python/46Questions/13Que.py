def max_in_list(multiinput):
    finalmax=0
    for num in range(1,len(multiinput)):
        max1=multiinput[num-1]
        max2=multiinput[num]
        if(max1>max2):
            if (max1>finalmax):
                finalmax=max1
                continue
        else:
            finalmax=max2
    return finalmax




if __name__=="__main__":
    multiinput=[]
    while True:
        inp=input()
        if inp=="":
            break
        else:
            multiinput.append(int(inp))
    print(max_in_list(multiinput))
