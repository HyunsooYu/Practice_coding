class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		res = {}
		for idx, val in enumerate(nums):
			remn = target-val
			if remn in res:
				return [res[remn], idx]
			res[val] = idx
