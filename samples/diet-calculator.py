# Defining an average price per item for one month (30 days)

# Approximate quantities of each item per month
monthly_quantity = {
    "chicken_breast_kg": 30,    # 1 kg per day
    "eggs_carton_30": 4,        # 1 carton of 30 eggs per week
    "oats_kg": 3,               # 3 kg of oats per month
    "brown_rice_kg": 4,         # 4 kg of brown rice per month
    "sweet_potato_kg": 5,       # 5 kg of sweet potatoes per month
    "greek_yogurt_kg": 4,       # 4 kg of Greek yogurt per month
    "nuts_kg": 1,               # 1 kg of nuts per month
    "apple_kg": 3,              # 3 kg of apples per month
    "lean_meat_kg": 5,          # 5 kg of lean meat per month
    "peanut_butter_kg": 2,      # 2 kg of peanut butter per month
    "whey_protein_kg": 1        # 1 kg of whey protein per month
}

# Average price of each item in BRL
average_price = {
    "chicken_breast_kg": 27.5,
    "eggs_carton_30": 21.5,
    "oats_kg": 8.5,
    "brown_rice_kg": 6.5,
    "sweet_potato_kg": 6,
    "greek_yogurt_kg": 16.5,
    "nuts_kg": 60,
    "apple_kg": 6,
    "lean_meat_kg": 35,
    "peanut_butter_kg": 30,
    "whey_protein_kg": 100
}

# Calculating the total cost per item for the month
monthly_cost = {item: monthly_quantity[item] * average_price[item] for item in monthly_quantity}

# Total cost for all items per month
total_monthly_cost = sum(monthly_cost.values())
print(monthly_cost)
print(total_monthly_cost)
