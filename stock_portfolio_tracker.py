import requests

class PortfolioManager:
    def __init__(self, api_key):
        self.api_key = api_key
        self.stocks = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol]['quantity'] += quantity
        else:
            current_price = self.fetch_stock_price(symbol)
            if current_price is not None:
                self.stocks[symbol] = {'quantity': quantity, 'price': current_price}
        print(f"Added {quantity} shares of {symbol}.")

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            if self.stocks[symbol]['quantity'] >= quantity:
                self.stocks[symbol]['quantity'] -= quantity
                if self.stocks[symbol]['quantity'] == 0:
                    del self.stocks[symbol]
                print(f"Removed {quantity} shares of {symbol}.")
            else:
                print("Insufficient shares to remove.")
        else:
            print("Stock not found in portfolio.")

    def fetch_stock_price(self, symbol):
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        try:
            price = float(data['Global Quote']['05. price'])
            return price
        except KeyError:
            print(f"Error retrieving data for {symbol}.")
            return None

    def display_portfolio(self):
        total_value = 0
        for symbol, info in self.stocks.items():
            current_price = self.fetch_stock_price(symbol)
            if current_price is not None:
                value = current_price * info['quantity']
                total_value += value
                print(f"{symbol}: {info['quantity']} shares at ${current_price:.2f}, Total: ${value:.2f}")

        print(f"Total Portfolio Value: ${total_value:.2f}")

# Example usage
if __name__ == "__main__":
    API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
    portfolio = PortfolioManager(API_KEY)

    while True:
        print("\n1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        option = input("Select an option: ")

        if option == '1':
            stock_symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(stock_symbol, shares)
        elif option == '2':
            stock_symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(stock_symbol, shares)
        elif option == '3':
            portfolio.display_portfolio()
        elif option == '4':
            break
        else:
            print("Invalid option. Please try again.")