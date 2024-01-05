# 這個題目要求你寫一個函式，該函式接受一個整數陣列作為輸入，然後返回陣列中的最小整數。
def find_smallest_int(arr):
    for index in range(0, len(arr)):
        if index == 0:
            smallest = arr[index]
        elif arr[index] < smallest:
            smallest = arr[index]
        else:
            continue
    return smallest

