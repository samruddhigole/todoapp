def vowel_or_not(character):
    charlist=["a","e","i","o","u"]
    if character == "":
        print("please enter a valid character")
    else:
        for char1 in charlist:
            if char1 == character:
                print ("Its a vowel")
            #print("Its not a vowel")

if __name__ == "__main__":
    character=input("enter a character")
    vowel_or_not(character)
