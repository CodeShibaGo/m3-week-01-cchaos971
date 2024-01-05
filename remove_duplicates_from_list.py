# 這個題目要求你寫一個函式，該函式接受一個列表作為輸入，
# 然後返回一個新列表，其中移除了原列表中的重複項。
# 新列表應該保留原始順序。

def distinct(seq):
    new_list = []
    for element in seq:
        if element in new_list:
            continue
        else:
            new_list.append(element)
    return new_list