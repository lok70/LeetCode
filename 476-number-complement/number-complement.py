class Solution:
    def findComplement(self, num: int) -> int:
        new_num = str(bin(num))
        new_num = new_num[2:]
        bin_num = ""
        for i in range(len(new_num)):
            if new_num[i] == "0":
                bin_num += "1"
            else:
                bin_num += "0"
        return int(bin_num, 2)

        