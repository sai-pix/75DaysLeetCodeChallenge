class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        sign = -1 if (dividend<0) ^ (divisor < 0) else 1
        dividend=abs(dividend)
        divisor=abs(divisor)
        res=0
        while divisor <= dividend:
            temp=divisor
            mul=1
            while dividend >= (temp<<1):
                temp<<=1
                mul<<=1
            dividend-=temp
            res+=mul
        return sign*res