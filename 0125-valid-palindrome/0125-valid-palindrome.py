class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string=""
        for ch in s:
            if ch.isalnum():
                new_string+=ch.lower()
        return new_string == new_string[::-1]