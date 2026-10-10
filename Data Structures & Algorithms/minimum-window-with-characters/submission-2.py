class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tfreq = Counter(t)
        start = 0
        minlen = 10**6
        l = 0 
        window = {}
        have = 0
        need = len(tfreq)

        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0) + 1
            if window[s[r]] == tfreq[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    start = l
                if s[l] in tfreq and window[s[l]] == tfreq[s[l]]:
                    have -= 1
                if window[s[l]] == 1:
                    del window[s[l]]
                else:
                    window[s[l]] -= 1
                
                l += 1
                
            
        return '' if minlen == 10**6 else s[start: start + minlen]                         