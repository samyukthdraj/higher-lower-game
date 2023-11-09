import random
from datas import data
from art import logo


dictionary={"Sachin":"A cricketer","John Cena":"A wrestler", "Dwayne Johnson":"Actor",}
random_key, random_value=random.choice(list(dictionary.items()))
print(f"The key is: {random_key}")
print(f"The value is: {random_value}")
print("\nWHO IS MORE POPULAR?\n")
print(f"{random_key}: {random_value}\n")

# for key in dictionary:
#     value=dictionary[key]
#     print(key, ":", value)
    