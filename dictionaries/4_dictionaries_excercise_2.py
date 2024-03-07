"""
In the following example, the program imports data for the `program_data.py` module,
which contains 2 dictionaries namely `pantry` and `recipes`. The aim of this program is to
use the concept of multiple dictionaries working together. Based on the user's choice of
dish, the ingredient required are checked for availability in the pantry. The additional
ingredients required and their quantities are then added to another dictionary.
"""

from program_data import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """
    Adds `items` and their `amounts` or updates quantities of existing
        items in the dictionary `data`.
    :param data: List containing items and the quantities.
    :param item: Name of the different items.
    :param amount: Quantity of the items
    """
    data[item] = data.setdefault(item, 0) + amount


display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_list = {}
while True:
    print("Please choose your recipe:-")
    print("==========================")
    for key, value in display_dict.items():
        print(f"{key}: {value}")

    choice = input(":")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("Checking for ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if quantity <= quantity_in_pantry:
                print(f"\t{food_item} is available.")
            else:
                quantity_to_buy = quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

for things in shopping_list.items():
    print(things)
