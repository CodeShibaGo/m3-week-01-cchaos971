# 你需要寫一個函數，用於分類新的社交網絡成員。每位成員都有兩個屬性：
# 年齡（整數）和貢獻度分數（浮點數）。為了分類成員，你的函數需要滿足以下條件：
#
# 1. 如果成員的年齡大於等於 55，且貢獻度分數大於 7，則分類為 "Senior"。
# 2. 如果成員的年齡小於 55，且貢獻度分數大於 7，則分類為 "Senior"。
# 3. 其他情況，分類為 "Open"。
#
# 你需要返回一個列表，列表中包含每位成員的分類。
def categorize_new_member(data):
    check_senior = lambda member : "Senior" if member[0] >= 55 and member[1] > 7 else "Open"
    return list(map(check_senior, data))