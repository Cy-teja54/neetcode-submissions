class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        cnt = {}
        maxlen = 0
        if not s:
            return 0
        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            while cnt[s[r]] > 1:
                cnt[s[l]] -= 1
                l += 1
                if cnt[s[l]] == 0:
                    del cnt[s[l]]
            maxlen = max(maxlen,r - l)
        return maxlen + 1

            

        