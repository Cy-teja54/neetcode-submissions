class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                sumn = nums[i] + nums[l] + nums[r]
                if sumn > 0:
                    r -= 1
                elif sumn < 0:
                    l += 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
        return res