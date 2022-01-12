# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        leng_min = 250
        leng_max = 0
        strs = list(set(strs))
        for ind, value in enumerate(strs):
            if len(value)<leng_min:
                leng_min = len(value)
            if len(value)>leng_max:
                leng_max = len(value)
        stack = ""
        
        
        if len(strs)==1:
            return strs[0]
        print(leng_min)
        trig = 0
        if leng_min==0:
            return ""
        elif leng_min==1 and len(strs)>2:
            for ind0 in range(1, len(strs)):
                if strs[ind0][0] != strs[ind0-1][0]:
                    trig = 1    
            if trig == 1:
                return ""
            else:
                stack = stack + strs[ind0][0]                       
                return stack
            
        elif leng_min==1 and len(strs)==1:
            return strs[0]
        
        for i in range(leng_min):
            for ind0 in range(1, len(strs)):
                if strs[ind0][i] != strs[ind0-1][i]:
                    return stack
            stack = stack + strs[ind0][i]
        return stack
            
