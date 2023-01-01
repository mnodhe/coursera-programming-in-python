menu = ["espersso", "mocha", "latte", "cappuccino", "cortado", "americano"]


def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee


# map_coffee = map(find_coffee, menu)
# print(map_coffee)
# for item in map_coffee:
#     print(item)

filter_coffee=filter(find_coffee, menu)
print(filter_coffee)
for item in filter_coffee:
    print(item)