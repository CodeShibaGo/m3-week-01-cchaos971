# 給定一個家庭成員的年齡清單，你需要找出家庭成員中最年輕和最年長的成員之間的年齡差。
# 你將會得到一個包含多個正整數的清單，其中每個整數代表一個家庭成員的年齡。
# 你需要寫一個函數來計算並返回最年長成員和最年輕成員的年齡差。
def age_difference(ages):
    for index in range(0, len(ages)):
        if index == 0:
            youngest_age = ages[index]
            oldest_age = ages[index]
        elif ages[index] > oldest_age:
            oldest_age = ages[index]
        elif ages[index] < youngest_age:
            youngest_age = ages[index]
        else:
            continue
    return oldest_age - youngest_age
# print(age_difference([10, 5, 8, 20, 15, 25]))