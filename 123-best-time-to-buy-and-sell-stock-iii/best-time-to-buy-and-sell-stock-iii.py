from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        buy1 = -prices[0]  # Максимальная прибыль после первой покупки
        sell1 = 0          # Максимальная прибыль после первой продажи
        buy2 = -prices[0]  # Максимальная прибыль после второй покупки
        sell2 = 0          # Максимальная прибыль после второй продажи
        
        for price in prices[1:]:
            # Обновляем состояния в порядке, предотвращающем использование обновленных значений в одном шаге
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        
        return sell2


        