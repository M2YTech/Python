prices = [100, 200, 300, 400, 500]

discount = 10 #10% discount

final_price = []

for price in prices:
    final_prices = price - (price * discount/100)
    final_price.append(final_prices)

print(final_price)
