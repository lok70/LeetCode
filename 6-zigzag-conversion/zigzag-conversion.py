class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [''] * numRows
        current_row = 0
        direction = 1  # 1 для движения вниз, -1 для движения вверх
        
        for char in s:
            rows[current_row] += char
            # Определение направления движения
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1
            current_row += direction
        
        return ''.join(rows)