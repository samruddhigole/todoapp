def make_ing_form(string):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    vowels=["a","e","i","o","u"]
    if string.endswith("e") and string[-2]!='i':
        newstring=string[:-1]
        newstring=newstring+"ing"
        print(string,newstring)


    if string.endswith("ie"):
        newstring=string[:-1]
        newstring=newstring+"ying"
        print(string,newstring)
        print(string[:-3])
        print(string[:-2])
        print(string[:-1])
    if string[:-3] in vowels and string[:-2] not in vowels and string[:-1] in vowels:
        newstring=string+string[:-1]+"ing"
        print("in vowel thing",newstring)


if __name__ == "__main__":
    make_ing_form('be')
    make_ing_form('see')
    make_ing_form('lie')
    make_ing_form('move')
