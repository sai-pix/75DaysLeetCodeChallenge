class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets={')':'(',']':'[','}':'{'}
        for i in s:
            if i in brackets:
                top=stack.pop() if stack else '#'
                if brackets[i]!=top:
                    return bool(0)
            else:
                stack.append(i)
        return len(stack)==0