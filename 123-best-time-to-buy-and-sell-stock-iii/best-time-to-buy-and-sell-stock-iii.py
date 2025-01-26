
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Если массив пуст или имеет одну цену, прибыли не будет
        if not prices or len(prices) < 2:
            return 0
        
        # buy1, sell1 отвечают за покупку/продажу первого пакета акций
        # buy2, sell2 отвечают за покупку/продажу второго пакета акций
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for price in prices:
            # Лучшее завершение второй продажи на данный момент
            sell2 = max(sell2, buy2 + price)
            # Лучшая вторая покупка (с учётом того, что после sell1 можно снова купить)
            buy2 = max(buy2, sell1 - price)
            # Лучшее завершение первой продажи
            sell1 = max(sell1, buy1 + price)
            # Лучшая первая покупка (можно купить только в самом начале или «дешевле»)
            buy1 = max(buy1, -price)

        return sell2
