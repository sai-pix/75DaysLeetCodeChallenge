class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        i=0
        while digits:
            num+=digits.pop()*10**i
            i+=1
        num+=1
        while num:
            digits.append(num%10)
            num//=10
        return digits[::-1]