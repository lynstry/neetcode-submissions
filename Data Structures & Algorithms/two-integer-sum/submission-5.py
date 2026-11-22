class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums) - 1):
            for j in range(len(nums) -1 , 0, -1):
                if not i == j and nums[i] + nums[j] == target:
                    return [i,j]