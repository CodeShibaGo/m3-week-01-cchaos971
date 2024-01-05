## 詳細說明
# 寫一個函數，它接受一個字串作為輸入，並返回反轉後的字串。

def reverse_string(s):
    str = ""
    for index in range(0, len(s)):
        str = s[index] + str
    return str

# str = "wahaha"
# print(reverse_string(str))