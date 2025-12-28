nested_list = [1, [2, 3], [4, [5, 6]]]
flat_list = []

def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            flatten(item)
        else:
            flat_list.append(item)

flatten(nested_list)
print("Flattened list:", flat_list)
