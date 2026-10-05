class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        l = 0
        ml = 0
        maxf = 0
        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            maxf = max(maxf, cnt[s[r]])
            while (r - l + 1) - maxf > k:
                cnt[s[l]] -= 1
                l += 1
            ml = max(r - l + 1, ml)
        return ml
            





