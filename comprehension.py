# flowers = ["Roses", "Daisies", "Tulips", "Roses"]
# bees = ["Honeybee", "Bumblebee", "Sweatbee"]

# flowers_quotes = [f"{flower} make me sneeze." for flower in flowers]
# print(flowers_quotes)

# flowers_quotes_set = {f"{flower} make me sneeze." for flower in flowers}
# print(flowers_quotes_set)

# large_flowers = []

# for flower in flowers:
#   for bee in bees:
#     large_flowers.append(f"The {bee} pollinates the {flower}.")

# print(large_flowers)

# larger_flowers = [
#   f"The {bee} pollinatesthe {flower}."
#   for flower in flowers
#   for bee in bees]

# print(larger_flowers)


my_family = {
  "sister": {
    "name": "Suzy",
    "age": 32
  },
  "father": {
    "name": "John",
    "age": 55
  },
  "brother": {
    "name": "Billy",
    "age": 21
  }
}

family_stuff = set()

for family_member, member_values in my_family.items():
  family_stuff.add(f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old.')

print(family_stuff)

more_family_stuff = {f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old.'
  for (family_member, member_values) in my_family.items()
  }

print(more_family_stuff)