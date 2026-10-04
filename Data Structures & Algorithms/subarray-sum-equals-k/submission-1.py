class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = {}
        res = 0
        csum = 0
        for i in range(len(nums)):
            csum += nums[i]
            if csum == k:
                res += 1
            if csum - k in cnt:
                res += cnt[csum - k]
            if csum in cnt:
                cnt[csum] += 1
            else:
                cnt[csum] = 1
        return res
            
        