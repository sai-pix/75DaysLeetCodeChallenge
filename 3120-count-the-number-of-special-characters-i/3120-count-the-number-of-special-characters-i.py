class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        for i in set(word):
            if i.islower():
                if i and i.upper() in word:
                    c+=1
            elif i.isupper():
                if i and i.lower() in word:
                    c+=1
        return c//2
