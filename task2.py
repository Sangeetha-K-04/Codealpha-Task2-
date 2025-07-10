# 📊 Stock Portfolio Tracker
# Created as part of the CodeAlpha Internship Program
# This script helps users calculate their total investment value based on hardcoded stock prices.

# Dictionary of available stocks and their current prices (in INR)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2750,
    "AMZN": 3300,
    "MSFT": 310,
    "INFY": 1550,
    "TCS": 3500
}

# This will store the user's stock selections and quantities
portfolio = {}

print("\n📈 Welcome to the Stock Portfolio Tracker!")
print("Here are the stocks you can choose from:\n")

# Display all available stocks with their prices
for symbol, price in stock_prices.items():
    print(f"{symbol} - ₹{price}")

print("\nLet's start building your portfolio!")
print(" Type the stock symbol you want to invest in (or type 'done' to finish):")

# Taking user input for stocks and quantities
while True:
    stock = input("Enter stock symbol: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Sorry, that stock isn't available. Please try again.")
        continue

    try:
        quantity = int(input(f"How many shares of {stock} do you own? "))
        if quantity <= 0:
            print(" Quantity must be greater than zero.")
            continue
        # Add to portfolio (accumulate if already entered)
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print(" Please enter a valid number.")

# If the user hasn't added any stocks
if not portfolio:
    print("\n️ No stocks entered. Portfolio is empty.")
else:
    # Display the investment summary
    print("\n Portfolio Summary:")
    print("-------------------------------------")
    total_value = 0

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = quantity * price
        total_value += value
        print(f"{stock}: {quantity} shares × ₹{price} = ₹{value}")

    print("-------------------------------------")
    print(f"Total Investment Value: ₹{total_value}")

    # Option to save results in a CSV file
    save = input("\nWould you like to save this summary to a CSV file? (yes/no): ").lower()
    if save == "yes":
        import csv
        from datetime import datetime

        filename = f"stock_portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price per Share (INR)", "Total Value (INR)"])
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                value = price * quantity
                writer.writerow([stock, quantity, price, value])
            writer.writerow(["", "", "Total", total_value])

        print(f"✅ Portfolio saved successfully as '{filename}'")

print("\n✅ Thank you for using the Stock Portfolio Tracker!")
