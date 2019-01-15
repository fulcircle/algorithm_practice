def string_permutes(string):

    if len(string) == 1:
        return [string]

    permutes = []
    lst_string = list(string)
    for i in range(0, len(lst_string)):
        lst_string[0], lst_string[i] = lst_string[i], lst_string[0]
        swapped = ''.join(lst_string)
        substring_permutes = string_permutes(swapped[1:])
        for permute in substring_permutes:
            permutes.append(swapped[0] + permute)
        lst_string[i], lst_string[0] = lst_string[0], lst_string[i]

    return permutes


permutes = string_permutes("abcd")
print(permutes)
print(len(permutes))