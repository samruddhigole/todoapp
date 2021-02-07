def translate(string):
    not_consonant=["a","e","i","o","u"]
    double_string=""
    for str1 in string:
        for vowel in not_consonant:
            if str1 == vowel:
                double_string=double_string+str1
                #break
                #continue
            else:
                double_string=double_string+str1+"o"+str1
                break
    print(double_string)

if __name__ == "__main__":
    string = input("Enter a string")
    translate(string)

