# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, money):
    shop["admin"]["total_cash"] += money
    # return shop["admin"]["total_cash"]

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, number_pets_sold):
    shop["admin"]["pets_sold"] += number_pets_sold
    return shop["admin"]["pets_sold"]

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    pets_by_breed = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)
    return pets_by_breed

def find_pet_by_name(shop, pet_name):
    pet_by_name = None
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            pet_by_name = pet
    return pet_by_name

def remove_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            shop["pets"].remove(pet)

def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash_amount):
    customer["cash"] -= cash_amount
    return customer["cash"]

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    return len(customer["pets"])

def customer_can_afford_pet(customer, new_pet):
    if customer['cash'] >= new_pet["price"]:
        return True
    else:
        return False
    
def sell_pet_to_customer(shop, pet, customer):
    if pet != None:
        can_buy_pet = customer_can_afford_pet(customer, pet)
        if can_buy_pet == True:
            add_pet_to_customer(customer, pet)
            increase_pets_sold(shop, len([pet]))
            remove_customer_cash(customer, pet["price"])
            add_or_remove_cash(shop, pet["price"])
            remove_pet_by_name(shop, pet["name"])