def encoder_decoder(phrase):
    key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u','i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c','q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k','y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S','G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A','O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
    marks = ["?","!","@","#","$","%","&","*","|",",",".","(",")"]
    newphrase=""
    for word in phrase:
        print(word,len(word))
        for char in range(0,int(len(word))):
            for alpha in key:
                if word[char]==alpha:
                    newphrase=newphrase+key[alpha]
                if word[char] in marks:
                    newphrase=newphrase+word[char]
                    break
        newphrase=newphrase+" "
    print(newphrase,end=" ")




if __name__ == "__main__":
    phrase=input("enter a phrase for encode or decode").split()
    encoder_decoder(phrase)
