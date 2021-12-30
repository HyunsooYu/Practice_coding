# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set0 = set(s)
        ss = list(set0)
        num = len(ss)              
        mx = 0  
        mx_prev = 0
        for n in range(num, -1, -1):
            print(n)
            for i in range(len(s)-n+1):
                if len(s[i:i+n])==len(list(set(s[i:i+n]))) and len(s[i:i+n])>mx:
                    mx = len(list(set(s[i:i+n])))
            if mx_prev>mx:
                return mx_prev
            else:
                mx_prev = mx
            
        return mx    
