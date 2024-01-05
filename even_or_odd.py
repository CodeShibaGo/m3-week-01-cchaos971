# 這個題目要求你寫一個函式，該函式接受一個整數作為輸入，
# 然後判斷該整數是偶數還是奇數。
# 如果整數是偶數，則函式應返回 "Even"，
# 如果整數是奇數，則函式應返回 "Odd"。

def even_or_odd(number):
    return "Even" if number%2 == 0 else "Odd"
