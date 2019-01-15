def string_combos(string):

    if len(string) == 1:
        return [string]

    combos = []
    lst_string = list(string)
    for i in range(0, len(lst_string)):
        char = lst_string[i]
        del lst_string[i]
        substring = "".join(lst_string)
        combos.append(substring)
        substring_combos = string_combos(substring)
        combos.extend(substring_combos)
        lst_string.insert(i, char)

    return combos

print(string_combos("abc"))