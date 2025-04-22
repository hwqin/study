'''

Problem statement
You have been given a sorted (lexical order) dictionary of an alien language.



Write a function that returns the order of characters as a string in the alien language. 
This dictionary will be given to you as an array of strings called 'dictionary', of size 'N'.


Example :
If the dictionary consists of the following words:-
["caa", "aaa", "aab"], and 'K' is 3.

Then, the order of the alphabet is -
['c', 'a', 'b']

Note:
If the language consists of four letters, the four letters should be the starting
four letters of the English language. 

However, their order might differ in the alien language.

'''

def getAlienLanguage(dictionary, n) :
    # Write your code here.
    chars=[]
    charset = set()
    if dictionary is None or n <= 0:
        return chars
    i = 0 #scan all chars
    wordcount = 1 # remember how many words left
    while wordcount > 0:
        wordcount = 0

        for word in dictionary:
            length = len(word)
            if i < length:
                wordcount += 1
                char = word[i]
                if not char in charset:
                    charset.add(char)
                    chars.append(char)
        i +=1

    return chars

array = ["caa", "aaa", "aab"]
array2 = ["a", "aa", "aaa",]
# print(getAlienLanguage(array2, 3))


class Solution():
    def getorderdict(self, order):
        chardict={}
        i = 0
        for char in order:
            chardict[char] = i
            i += 1
        return chardict

    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        wordcount = len(words)
        if wordcount <= 1:
            return True

        charorderdict = self.getorderdict(order)
        # check char at each index, and compare
        i = 0
        while wordcount > 0:
            wordcount = 0
            # remember order of char position in order string
            index = -1
            dupchar = False
            
            curlength = -1
            for word in words:
                n = len(word)

                # for word short than i+1, default index is -1
                curindex = -1
                if (n > i):
                    wordcount += 1
                    char = word[i]
                    curindex = charorderdict[char]
                    # print(f"index of char {char} of word {word}: ${curindex}")
                
                if curindex < index:
                    return False
                if curindex == index:
                    dupchar = True # at least two words at index i has same char, continue to compare
                index = curindex

            i += 1
            
            if not dupchar: # if no duplicated char, then break
                break

        return True

words = ["kuvp","q"]
order = "ngxlkthsjuoqcpavbfdermiywz"

solution = Solution()
print(solution.isAlienSorted(words, order))
