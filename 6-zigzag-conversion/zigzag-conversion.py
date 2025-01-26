class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Если зигзага нет, сразу возвращаем исходную строку
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Массив строк, каждая отвечает за один «ряд» зигзага
        rows = [""] * numRows
        
        # Текущая позиция ряда и направление (идём вниз или вверх)
        cur_row = 0
        going_down = True
        
        # Раскладываем символы по «рядам»
        for char in s:
            rows[cur_row] += char
            # Если достигли нижней границы, меняем направление на «вверх»
            if cur_row == numRows - 1:
                going_down = False
            # Если достигли верхней границы, меняем направление на «вниз»
            elif cur_row == 0:
                going_down = True
            
            # Движемся по рядам в зависимости от направления
            if going_down:
                cur_row += 1
            else:
                cur_row -= 1
        
        # Объединяем все ряды в один результат
        return "".join(rows)