def count_duplicates(text):
    new_dict = {}
    for index in range(0, len(text)):
        if text[index].lower() not in new_dict:
            new_dict.update({f"{text[index].lower()}": 1})
        else:
            new_dict[text[index].lower()] += 1
    # print(new_dict)
    return len([num for num in new_dict.values() if num > 1])
