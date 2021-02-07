import re
def correct(string):
    print(string)
    print(re.sub(' +',' ',string))

if __name__ == "__main__":
    string=input("enter a string")
    correct(string)
