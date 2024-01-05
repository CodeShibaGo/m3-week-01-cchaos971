# ## 詳細說明
# 這個題目要求你寫一個函數，將一個字串中的所有母音字元（a、e、i、o、u）都移除，並返回新的字串。這是一個簡單的字串處理任務。

def disemvowel(s):
    vowel_char = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    str = ""
    for char in s:
        if char in vowel_char:
            continue
        else:
            str += char
    return str
