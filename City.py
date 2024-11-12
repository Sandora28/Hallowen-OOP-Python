import random
from Exception import  InsufficientStockError,InsufficientBudgetError,CostumeNotFoundError


class City:
    def __init__(self, name, population):
        self._name = name
        self.population = population
        self.costume_shops = []
        self.customers =[]

    # appends shop specific CostumeShop object to the costume_shops list
    def add_shop(self, shop):
        self.costume_shops.append(shop)


    # returns all the info about city, shops , costumes and quantity(stock) of them , it uses report_stock method for
    # CostumeShop objects in order to show full data
    def report(self):
        report = f"City: {self._name}, Population: {self.population}\n"
        report += "Costume Shops:\n"
        for shop in self.costume_shops:
            report += shop.report_stock()
        return report

    # firstly , it resets all data about demands , so it is not reusable method , should be appropriate to use one time.
    # then it takes unique names of costumes from the shop
    # with random choice , every person is choosing one preferred costume with quantity
    def simulate_demand(self):
        # resets demand for all costumes in each shop
        for shop in self.costume_shops:
            for costume_name in shop.costumes.keys():
                shop.demand[costume_name] = 0

        # collects all unique costume names from the shops
        all_costumes = set()
        for shop in self.costume_shops:
            all_costumes.update(shop.costumes.keys())

        # simulates demand based on each person preferences
        for _ in range(self.population):
            # each person randomly chooses a costume from the available costumes
            preferred_costume = random.choice(list(all_costumes))
            preferred_number = random.randint(1,3)
            for shop in self.costume_shops:
                if preferred_costume in shop.costumes:
                    shop.demand[preferred_costume] += preferred_number



    def add_customer(self, customer):
        self.customers.append(customer)

    @staticmethod
    def simulate_shopping(customers, shops):
        for customer in customers:
            print(f"\n{customer.name}'s Shopping Journey:")

            for costume_name, quantity in customer.shopping_list.copy().items():
                try:
                    customer.buy_costume(costume_name, quantity, shops)
                except InsufficientStockError as e:
                    print(f"Error: {e}")
                except InsufficientBudgetError as e:
                    print(f"Error: {e}")
                except CostumeNotFoundError as e:
                    print(f"Error: {e}")