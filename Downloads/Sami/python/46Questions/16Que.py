def max_len_word(wordlist,number):
    listofword=[]
    for word in wordlist:
        if int(number) < int(len(word)):
            listofword.append(word)
    return listofword

if __name__ == "__main__":
    wordlist=input("enter words with space seperation:").split()
    number=input("enter a number which you want to compare with word")
    print(max_len_word(wordlist,number))
