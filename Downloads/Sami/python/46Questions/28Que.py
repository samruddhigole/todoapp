def find_longest_word(words):
    return max(map(len,words))

if __name__ == "__main__":
    print(find_longest_word(["sam","sami","samruddhi"]))
