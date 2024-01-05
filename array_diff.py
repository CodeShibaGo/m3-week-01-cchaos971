# 這個題目要求你寫一個函式，該函式接受兩個列表作為輸入，
# 然後返回一個新的列表，
# 其中包含了第一個列表中存在但不在第二個列表中的元素。
# 換句話說，你需要找出兩個列表之間的差異。

def array_diff(a, b):
    new_list = []
    set_b = set(b)
    for element in a:
        if element not in set_b:
            new_list.append(element)
    return  new_list



print(array_diff([1,2,2], [1]))