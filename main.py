from City import City
from CostumeShop import CostumeShop
from Customer import Customer

city = City("Halloween Town", 5000)

shop1 = CostumeShop("Pumpkin")
shop1.add_costume("Zombie", 500, 25)
shop1.add_costume("Vampire", 520, 30)
shop1.add_costume("Witch", 530, 20)

shop2 = CostumeShop("Monster")
shop2.add_costume("Zombie", 400, 10)
shop2.add_costume("Vampire", 450, 45)
shop2.add_costume("Witch", 450, 20)

shop3 = CostumeShop("Bat")
shop3.add_costume("Zombie", 300, 21)
shop3.add_costume("Vampire", 350, 17)
shop3.add_costume("Witch", 390, 20)

shop4 = CostumeShop("Hotel Transylvania")
shop4.add_costume("Zombie", 7, 17)
shop4.add_costume("Vampire", 6, 21)
shop4.add_costume("Witch", 3, 20)

shop5 = CostumeShop("Dracula")
shop5.add_costume("Zombie", 240, 18)
shop5.add_costume("Vampire", 250, 13)
shop5.add_costume("Witch", 230, 20)

city.add_shop(shop1)
city.add_shop(shop2)
city.add_shop(shop3)
city.add_shop(shop4)
city.add_shop(shop5)

city.simulate_demand()
print(city.report())


customer1 = Customer("Sandro", 5000, {"Zombie": 21, "Witch": 2,"Vampire": 10})
customer2 = Customer("Ana", 4000, {"Witch": 1})
customer3 = Customer("Liza", 4000, {"Zombie": 19, "Witch": 5})
customer4 = Customer("Davit", 4000, {"Zombie": 11, "Vampire": 13, "Dracula":18})
customer5 = Customer("Erekle", 400000, {"Witch": 1000, "Oracle":1})

customers = [customer1, customer2,customer3,customer4,customer5]

# Simulate shopping
city.simulate_shopping(customers, city.costume_shops)

print(city.report())
