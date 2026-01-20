stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_investment = 0

print("Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        value = stock_prices[stock] * quantity
        total_investment += value
        print("Added value:", value)
    else:
        print("Stock not found!")

print("Total Investment Value:", total_investment)
