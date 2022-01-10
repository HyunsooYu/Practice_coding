# 18. 4Sum
# https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        num_set = set(nums)
        num_s = list(num_set)
        if len(nums)<4:
            return []
        elif len(nums) == 4 and sum(nums)!=target:
            return []
        elif len(nums) == 4 and sum(nums)==target:
            return [nums]
        elif len(num_s) ==1 and num_s*4 ==target:
            return [nums]
        else:
            nums.sort()
            print(nums)
            answer = []
            L = 0
            R = len(nums)-1
            prev_value = 10**9
               
            for a in range(len(nums)-3):
                for b in range(len(nums)-2):
                    c, d = b+1, len(nums)-1
                    while c<d :
                        s = nums[a] + nums[b] + nums[c] + nums[d]
                        if s<target:
                            c = c+1
                        elif s>target:
                            d = d-1
                        else:
                            #print([nums[a], nums[b], nums[c], nums[d]])
                            if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
                                ans = [nums[a], nums[b], nums[c], nums[d]]
                                ans.sort()
                                #print(ans)
                                ans = list(ans)
                                answer.append(ans)                       
                                c=c+1
                            else:
                                c=c+1
                            

            answer = list(set([tuple(answer) for answer in answer]))

            return answer
