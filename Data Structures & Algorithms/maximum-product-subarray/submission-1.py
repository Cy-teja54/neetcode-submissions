class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi, mini = 1,1
        res = max(nums)
        for n in nums:
            tmp = n* maxi
            maxi = max(tmp,n*mini,n)
            mini = min(tmp,n*mini,n)
            res = max(res,maxi)
        return res          
            

        