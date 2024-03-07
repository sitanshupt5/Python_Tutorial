"""
The following program replicates a shopping cart where the user can add the available parts
to the shopping cart. If the selected part is already in the shopping cart then it must be
removed from the shopping cart. If in case the part is not in the available list then the
list is redisplayed to the user for reference. User can exit from the cart anytime he or she
wishes. This can be achieved through dictionaries and lists:
"""
available_parts = {
    "1": "monitor",
    "2": "keyboard",
    "3": "mouse",
    "4": "printer",
    "5": "hdmi cable",
    "6": "dvd drive"
}

cart = []

current_choice = None
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part in cart:
            print(f"Removing {chosen_part}")
            cart.remove(chosen_part)
        else:
            print(f"Adding {chosen_part} to cart")
            cart.append(chosen_part)
        print(f"Your cart now contains: {cart}")
    else:
        print("Please add options from the list.")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: exit")

    current_choice = input("> ")