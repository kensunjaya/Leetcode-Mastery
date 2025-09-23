class Solution:        
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        def findPermute(index, nums, results):
            if len(nums) == index:
                results.append(nums.copy())
                return
            
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                findPermute(index + 1, nums, results)
                nums[i], nums[index] = nums[index], nums[i]
            
        findPermute(0, nums, results)
        return(results)
        