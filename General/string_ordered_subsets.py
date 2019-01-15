def ordered_subsets_bottom_up(available_characters, curr_string="", ordered_subsets=None):

    if not ordered_subsets:
        ordered_subsets = []

    if not isinstance(available_characters, list):
        available_characters = list(available_characters)

    for i in range(0, len(available_characters)):
        char = available_characters[i]
        new_string = curr_string + char
        ordered_subsets.append(new_string)
        del available_characters[i]
        ordered_subsets_bottom_up(available_characters, new_string, ordered_subsets)
        available_characters.insert(i, char) # backtrack

    return ordered_subsets


ordered_subsets = ordered_subsets_bottom_up("abc")
print(ordered_subsets)
print(len(ordered_subsets))