from Exception import InsufficientBudgetError,InsufficientStockError,CostumeNotFoundError

class Customer:
    def __init__(self, name, budget,shopping_list):
        self.name = name
        self.budget = budget
        self.shopping_list = shopping_list

    # checks if customer has enough budget for shopping
    def check_budget(self, costume_price):
        return self.budget >= costume_price

    #buy function firstly sorting all shops by price of specific costume (provided by customer),
    # then if I found cheap shop for my costume , I am checking if they have enough stock for me , if not I am buying how much they have
    # and for other necessary quantity that satisfies me i am going to next shop in sorted shops. and looping this function until
    # I won't buy how much I wanted to. and last , if i will buy enough costumes i am poping its name from my wish list.
    def buy_costume(self, costume_name, quantity, shops):
        total_cost = 0
        remaining_quantity = quantity
        total_bought = 0

        # creates a sorted list of shops by price for the desired costume
        available_shops = [
            shop for shop in shops
            if costume_name in shop.costumes and shop.costumes[costume_name] > 0
        ]

        available_shops.sort(key=lambda shop: shop.prices[costume_name])

        # iterates through shops to buy the costume
        for shop in available_shops:
            stock = shop.costumes[costume_name]
            price = shop.prices[costume_name]

            # if this shop has enough stock for the remaining quantity
            if stock >= remaining_quantity:
                cost = remaining_quantity * price
                if self.budget >= total_cost + cost:
                    # Deduct from the budget
                    self.budget -= cost
                    total_cost += cost
                    shop.sell_costume(costume_name, remaining_quantity)

                    total_bought += remaining_quantity
                    remaining_quantity = 0
                    break  # Stop once the purchase is completed
                else:
                    raise InsufficientBudgetError(
                        f"{self.name} cannot afford the total cost of {quantity} {costume_name}(s).")
            else:
                # buy as much as possible from this shop
                cost = stock * price
                if self.budget >= total_cost + cost:
                    # reduce from the budget and reduce the remaining quantity
                    self.budget -= cost
                    total_cost += cost
                    remaining_quantity -= stock
                    shop.sell_costume(costume_name, stock)

                    total_bought += stock
                else:
                    raise InsufficientBudgetError(
                        f"{self.name} cannot afford the total cost of {quantity} {costume_name}(s).")

        # if after iterating all shops, we still have a remaining quantity to buy
        if remaining_quantity == remaining_quantity:
            raise CostumeNotFoundError(
                f"{self.name} couldn't find {costume_name}(s).")
        elif remaining_quantity > 0:
            raise InsufficientStockError(
                f"{self.name} couldn't find {costume_name}(s). Purchased {total_bought} out of {quantity}.")

        print(
            f"{self.name} bought {total_bought} {costume_name}(s) for a total of ${total_cost:.2f}. Remaining budget: ${self.budget:.2f}.")

        # update the shopping list
        if self.shopping_list[costume_name] <= total_bought:
            self.shopping_list.pop(costume_name)
        else:
            self.shopping_list[costume_name] -= total_bought

    def shop_report(self):
        print(f"Customer: {self.name}, Remaining Budget: {self.budget}")
        print(f"Shopping List: {self.shopping_list}")