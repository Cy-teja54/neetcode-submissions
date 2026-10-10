class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        window = {}
        maxlen = 0
        mf = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0) + 1
            mf = max(mf, window[s[r]])
            while r - l + 1 > k + mf:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen

            





