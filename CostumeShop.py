import math
from Exception import CostumeNotFoundError, InsufficientStockError

class CostumeShop:
    def __init__(self, name):
        self.name = name
        self.prices = {}
        self.costumes = {}
        self.demand = {}

    # adds specific costume to the shop with stock and price
    def add_costume(self, costume_name, stock, price):
        self.costumes[costume_name] = stock
        self.prices[costume_name] = price
        self.demand[costume_name] = 0

    # adjusts the price of a costume based on its demand
    def adjust_price(self, costume_name):
        if costume_name in self.prices:
            base_price = self.prices[costume_name]
            demand = self.demand[costume_name]

            # Linear scaling: For every increase in demand, increase price by a fixed amount.
            # You can adjust the increment factor as needed.
            increment_factor = 0.005  # Adjust this to control how much the price increases with demand
            new_price = base_price + (demand * increment_factor)

            max_price = base_price * 3  # Maximum price cap
            self.prices[costume_name] = min(new_price, max_price)

            print(f"Adjusted price for {costume_name} in shop '{self.name}' to ${self.prices[costume_name]:.2f}.")

    # adjusts demand directly
    def adjust_demand(self, costume_name, new_demand):
        if costume_name in self.demand:
            self.demand[costume_name] = new_demand
            print(f"Costume Shop adjusted demand for {costume_name}: {self.demand[costume_name]}")
        else:
            raise CostumeNotFoundError(f"{costume_name} is not available in shop '{self.name}'.")

    # adjusts stock for a specific costume
    def adjust_stock(self, costume_name, new_stock):
        if costume_name in self.costumes:
            self.costumes[costume_name] = new_stock
            print(f"Costume Shop adjusted stock for {costume_name}")
        else:
            raise CostumeNotFoundError(f"{costume_name} is not available in shop '{self.name}'.")

    # this function sells costumes by its name if quantity is available , and after selling it increasing demand and price accordingly
    def sell_costume(self, costume_name, quantity):
        if costume_name in self.costumes:
            if self.costumes[costume_name] >= quantity:
                # reduces quantity
                self.costumes[costume_name] -= quantity

                # increase demand by a percentage of the quantity sold (110% here)
                base_demand_increase = 1.1  # 110% increase in demand for each sale
                demand_increase = quantity * base_demand_increase

                # updates demand using the adjust_demand method
                new_demand = self.demand[costume_name] + int(demand_increase)
                self.adjust_demand(costume_name, new_demand)

                # increases the price based on logic that if costume is sold so its demand will be increased so shop will increase price also
                self.adjust_price(costume_name)

                print(
                    f"Costume Shop '{self.name}' sold {quantity} {costume_name}(s). Demand increased by {int(demand_increase)}.")
            else:
                raise InsufficientStockError(
                    f"Not enough stock of {costume_name} in shop '{self.name}'. Available: {self.costumes[costume_name]}.")
        else:
            raise CostumeNotFoundError(f"{costume_name} is not available in shop '{self.name}'.")

    # it goes through shop and shows whole data(costumes, their prices, their demand) about it.
    def report_stock(self):
        report = f"Costume Shop: {self.name}\n"
        for costume_name in self.costumes:
            report += (
                f"{costume_name}: {self.costumes[costume_name]} in stock, "
                f"Price: ${self.prices[costume_name]:.2f}, "
                f"Demand: {self.demand[costume_name]}\n"
            )
        return report
