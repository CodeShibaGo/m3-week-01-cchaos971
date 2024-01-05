# 實現一個函數，該函數接受兩個單詞的名字，並返回它們的縮寫，
# 縮寫應該是兩個單詞的首字母大寫並用句點分隔。
def abbrev_name(name):
  name_list = name.split()
  return name_list[0][0].upper() + "." + name_list[1][0].upper()
