class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        return self.Util(0, n - 1, s, dp)
        
    def Util(self, i: int, j: int, s:str, dp: list) -> int:
        if i > j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]

        first_let = s[i]
        ans = 1 + self.Util(i+1, j, s, dp)
        for k in range(i + 1, j + 1):
            if s[k] == first_let:
                better_ans = self.Util(i, k - 1, s, dp) + self.Util(k + 1, j, s, dp)
                ans = min(ans, better_ans)
        dp[i][j] = ans
        return ans