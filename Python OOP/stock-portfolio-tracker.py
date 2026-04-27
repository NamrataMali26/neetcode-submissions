from dataclasses import dataclass
from os import name

class Portfolio: #Holds all stocks owned by the user
    def __init__(self, owner_name: str):
        self.owner_name = owner_name
        self.holdings = {}
        self.transactions = []
        self.realized_profit = 0


    def buy_stock(self, stock_name, quantity, price):
        symbol = stock_name.upper()
        if symbol not in self.holdings:
            self.holdings[symbol] = Holding(symbol, quantity, price)
        else:
            self.holdings[symbol].add_shares(quantity, price)

        transaction = Transaction('BUY', stock_name, quantity, price)
        self.transactions.append(transaction)


    def sell_stock(self, stock_name, quantity, market):
        symbol = stock_name.upper()
        market_price = market.get_price(symbol)
        holding = self.holdings[symbol]

        if market_price == 0:
            print(f"Price not available for {symbol}. Update price first.")
        
        elif quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        elif holding and holding.quantity >= quantity and quantity > 0:
            sell_price = market_price
            holding.remove_shares(quantity)
            self.realized_profit += ((sell_price - holding.avg_price) * quantity)

            if holding.quantity == 0:
                del self.holdings[symbol]

            transaction = Transaction('SELL', symbol, quantity, sell_price)
            self.transactions.append(transaction)

        elif not holding:
            raise StockNotFoundError(f"You do not own this stock")
            
        else:
            print(f"Not enough {symbol} shares to sell")


    def profit_loss_calculations(self, market):
        
        total_gain_loss = 0
       
        for symbol, holding in self.holdings.items():

            market_price = market.get_price(symbol)
            if market_price != 0:
                curr_price = market_price
                curr_total = curr_price * holding.quantity

                actual_total = holding.quantity  * holding.avg_price
                total_gain_loss += (curr_total - actual_total)
            else:
                print(f"Price not available for {symbol}")
        if total_gain_loss > 0:
            print(f"current account value is ${curr_total}, gain of ${total_gain_loss}")
        else:
            print(f"current account value is ${curr_total}, loss of ${total_gain_loss}")


    def view_transactions(self):
        for transaction in self.transactions:
            print(transaction)

    def top_performing_stock(self):
        top_stock = ""
        top_value = 0
        for symbol, holding in self.holdings.items():
            buy_total = holding.avg_price * holding.quantity
            curr_total = market.get_price(symbol) * holding.quantity
            if (curr_total - buy_total) > top_value:
                top_value = (curr_total - buy_total)
                top_stock = symbol
        print(f"top performing stock is: {top_stock} with potential profit: {top_value}. ")


    def view_portfolio(self, market):
        print(f"Portfolio Owner: {self.owner_name}")
        print(f"Holdings:")
        for symbol, holding in self.holdings.items():
            print(symbol, holding.quantity, holding.avg_price)
        print(f"total realized profit/loss: ${self.realized_profit}")
        self.profit_loss_calculations(market)
        self.top_performing_stock()
        self.view_transactions()
        
class StockNotFoundError(Exception):
    pass

@dataclass
class Transaction:
    type: str
    stock_name: str
    quantity: int
    price: float

    def __str__(self):
        return f"{self.type} {self.quantity} {self.stock_name.upper()} @ {self.price}"


class Market:
    def __init__(self):
        self.market_prices = {}
   
    def get_price(self, stock_name):
        return self.market_prices.get(stock_name.upper(), 0)

    def update_price(self, stock_name, price):
        if price <= 0:
            print("Please check the price.")
        else:
            self.market_prices[stock_name.upper()] = price

class User:
    def __init__(self, name):
        self.name = name
        self.portfolio = Portfolio(name)


class Holding:
    def __init__(self, stock_name, quantity, avg_price):
        self.stock_name = stock_name
        self.quantity = quantity
        self.avg_price = avg_price
    
    def add_shares(self, quantity, price):
        old_quantity = self.quantity
        new_quantity = self.quantity + quantity
        new_avg = ((old_quantity * self.avg_price) + (quantity * price)) / new_quantity
        self.quantity = new_quantity
        self.avg_price = new_avg  
    
    def remove_shares(self, quantity):
        self.quantity = self.quantity - quantity





market = Market()
market.update_price("APPL", 500)
market.update_price("TSLA", 200)
market.update_price("NVDA", 200)

user = User("Namrata")
user.portfolio.buy_stock("APPL", 20, 100)
user.portfolio.buy_stock("TSLA", 50, 200)
user.portfolio.buy_stock("TSLA", 10, 50)

user.portfolio.sell_stock("TSLA", 10, market)
user.portfolio.view_portfolio(market)


