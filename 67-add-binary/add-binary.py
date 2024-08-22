class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        summ = a + b
        summ = str(bin(summ))
        return summ[2:]
