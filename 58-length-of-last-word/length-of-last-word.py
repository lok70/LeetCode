class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().replace(" ", "@")
        ar = s.split("@")
        return len(ar[-1])

        