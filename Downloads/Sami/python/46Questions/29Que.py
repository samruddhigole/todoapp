def filter_long_words(words,n):
    return filter(lambda x: len(x) > n, words)

result=filter_long_words(["sam","sami","samruddhi"],9)
print(result)
