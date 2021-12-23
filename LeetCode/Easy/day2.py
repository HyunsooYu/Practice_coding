# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x);
        for idx, value in enumerate(num):
            idxn = len(num)-1-idx
            if num[idx]!=num[idxn]:
                return False
            elif idx>=len(num)/2:
                return True
            elif len(num)==1:
                return True
