
# reverse words inside string
def reverse_words(A):
    
    # reverse whole string
    reversed = A[::-1]
    words = reversed.split(" ")
    return " ".join(map(lambda w: w[::-1], words))

def reverse_words_2(A):
    words = A.split(" ")
    return " ".join(words[::-1])

print(reverse_words_2("this is a demo applicaton of aws, cool, right"))
