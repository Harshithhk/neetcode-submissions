class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res, sol  = [] , []
        n = len(nums)
        def backtracking(i):

            if i >= n:
                res.append(sol[:])
                return
            
            # not picking val
            backtracking(i+1)

            # picking val
            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()
        
        backtracking(0)

        return res
