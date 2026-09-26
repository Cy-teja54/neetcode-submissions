class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dici = {}
        for i in range(len(nums)):
            want = target - nums[i]
            if want in dici:
                return [dici[want],i]
            else:
                dici[nums[i]] = i 
        
