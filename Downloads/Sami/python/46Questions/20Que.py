def translate(phrase):
    dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
    newphrase=[]
    for word in phrase:
        for x in dict:
            if(word==x):
                 newphrase.append(dict[x])
    return newphrase

if __name__ == "__main__":
    phrase=input("enter a phrase to translate").split()
    print(translate(phrase))

