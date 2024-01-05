# 給定一個布林值的清單，其中True表示羊在睡覺，False表示羊醒著。
# 你的任務是計算清單中有多少只羊在睡覺（True的數量）。返回睡覺的羊的數量。
def count_sheep(sheep):
    sleep_num = 0
    for element in sheep:
        if (element == True):
            sleep_num += 1
    return sleep_num
