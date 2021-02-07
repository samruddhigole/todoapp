def find_longest_word(wordlist):
    longword=0
    secondlongword=0
    for w in range (1,len(wordlist)):

        longword=len(wordlist[w-1])
        secondlongword=len(wordlist[w])

        if longword>secondlongword:
            max_len_word = wordlist[w-1]
        else:
            max_len_word = wordlist[w]
    return max_len_word


if __name__ == "__main__":
    wordlist=["sam", "sami","samruddhi"]
    print(find_longest_word(wordlist))
