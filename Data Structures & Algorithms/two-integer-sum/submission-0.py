class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exists = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if diff in exists:
                return [exists[diff],i]

            exists[num] = i

        return []
