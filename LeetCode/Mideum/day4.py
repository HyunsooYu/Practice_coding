#  Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = s[0]
        final = []
        if len(s)==1:
            return s
        else:
            for i in range(len(s)):
                for j in range(len(s)-1, -1, -1):
                    if s[i]==s[j] and i<j :
                        if CheckEndRepeat(s[i:j+1]):
                            if len(out)<len(s[i:j+1]):
                                out = s[i:j+1]
                        else:
                            continue
            return out
            
def CheckEndRepeat(s: str) -> bool:
    new_s = s[::-1]
    if s==new_s:
        return 1
    else:
        return 0
