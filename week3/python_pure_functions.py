my_list = [1, 2, 3]


def add_to_list(item, list):
    nl = list.copy()
    nl.append(item)
    return nl


print(my_list)
new_list = add_to_list(4, my_list)
print(new_list)
