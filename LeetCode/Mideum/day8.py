# 3Sum
# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_set = set(nums)
        num_s = list(num_set)
        if len(nums)<3:
            return []
        elif len(nums) == 3 and sum(nums)!=0:
            return []
        elif len(nums) == 3 and sum(nums)==0:
            return [nums]
        elif len(num_s) ==1 and num_s ==[0]:
            return [[0,0,0]]
        else:
            nums.sort()
            print(nums)
            answer = []
            L = 0
            R = len(nums)-1
            prev_value = 10**6
            base = 0
            for i in range(len(nums)-1):
                if nums[i]*nums[i+1]<=0 and nums[i]!=nums[i+1] and nums[i+1]>0:
                    base = i
                    break
            print(base)
            if base==L or base==R:
                return []
            
            for index, value in enumerate(nums[1:len(nums)-1]):
               # print("{} {}".format(index, value))
                L = index -1+1
                R = index +1+1            
                
                while L>=0 and R<len(nums):
                   # print("ind : {} L: {} R: {}".format(value, L, R))
                    sum3 = nums[L]+nums[R]+value
                    if sum3<0:
                        R = R+1
                    elif sum3>0:
                        L = L-1
                    else:
                        answer.append([nums[L], value, nums[R]])
                        L = L-1
            answer = list(set([tuple(answer) for answer in answer]))

            return answer
