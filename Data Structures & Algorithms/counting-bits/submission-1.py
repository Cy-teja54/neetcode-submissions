class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            if i:
                res.append(res[i >> 1] + (i & 1))
            else:
                res.append(0)
        return res


        