# 這個題目要求你寫一個函式，該函式接受一個包含字母或數字的輸入字串，
# 然後返回一個新的字串或列表，其中相鄰的相同字元只保留一個。
# 換句話說，如果有連續的相同字元，只保留一個，其餘刪除。請保持原始輸入的相對順序。

def unique_in_order(iterable):
    new_list = []
    previous_char = None
    for index in range(0, len(iterable)):
        if previous_char != iterable[index]:
            previous_char = iterable[index]
            new_list.append(iterable[index])
    return new_list