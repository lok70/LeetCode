class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        one = 0
        zero = 0
        for std in students:
            if std == 1:
                one += 1
            elif std == 0:
                zero += 1
        
        for snd in sandwiches:
            if snd == 0:
                zero -= 1
            elif snd == 1:
                one -= 1
            if one < 0:
                return zero
            if zero < 0:
                return one
        
        return 0