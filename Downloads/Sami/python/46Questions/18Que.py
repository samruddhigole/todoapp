def panagram(phrase):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in phrase.lower():
            return False
    return True

if __name__ == "__main__":
    phrase=input("enter a phrase to check that it is a panagram or not")
    if(panagram(phrase)== True):
        print("Yes")
    else:
        print("No")

