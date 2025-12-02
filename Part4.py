def order_drink(drink, size="medium", iced=False):
    """Orders a drink with specified size and iced preference."""
    iced_str = "iced" if iced else "hot"
    return f"Your order: {size} {iced_str} {drink}"

# 1. Order a default drink.
print(order_drink("coffee"))

# 2. Order a large hot chocolate (no ice).
print(order_drink("chocolate", size="large"))

# 3. Order a small iced milk tea (iced = True).
print(order_drink("milk tea", size="small", iced=True))
