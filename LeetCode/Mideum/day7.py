# 11. Container With Most Water 
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int: # Time complexity O(n)
        mxArea = 0
        L, R = 0, len(height)-1
        while L<R:
            area = min(height[L], height[R])*abs(R-L)
            mxArea = max(mxArea, area)
            if height[L]>height[R]:
                R = R-1
            else:
                L = L+1
        return mxArea
                    
#    def maxArea2(self, height: List[int]) -> int: # Time complexity O(n^2)
#        mxArea=0
#        for index, value in enumerate(height):
#            index = index+1
#            for index2, value2 in enumerate(height[index:]):
#                index2 = index + index2+1
#            area = min([value, value2])*abs(index-index2)
#            if area>mxArea:
#                mxArea = area
#        return mxArea        
