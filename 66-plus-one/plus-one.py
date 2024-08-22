class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k = 1
        num = 0
        i = len(digits) - 1
        while i >= 0:
            num += digits[i] * k
            k *= 10
            i -= 1
        num += 1
        if len(str(num)) > len(digits):
            digits.append(0)
        for j in range(len(str(num))):
            digits[j] = num % 10
            num //= 10
        digits = digits[::-1]
        return digits