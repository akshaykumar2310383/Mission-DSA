def minimumLoss(prices):
    indexed_prices = sorted((price, year) for year, price in enumerate(prices))
    min_loss = float('inf')   
    for i in range(1, len(indexed_prices)):
        current_price, current_year = indexed_prices[i]
        previous_price, previous_year = indexed_prices[i - 1]    
        if current_year < previous_year:
            min_loss = min(min_loss, current_price - previous_price)
    return min_loss
