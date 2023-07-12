"""
リスト：順序○ 重複○ 変更○
集合  : 順序× 重複× 変更○
タプル: 順序○ 重複○ 変更×
"""

x_set = {11, 222, 333}
y_list = [11, 333, 444, 555, 11]
y_set = set(y_list) #setを使用してリストを集合に変換

result = x_set & y_set #積集合(共通部分)を取得
result2 = x_set - y_set #差集合を取得（x_setにあってy_setにないもの）
result3 = x_set | y_set #和集合を取得
print(result)
print(result2)
print(result3)
print(x_set)
print(y_set)


x_tuple = (1, 3, 5)
g_list = [3, 4, 5]
g_tuple = tuple(g_list) #tupleでタプルへ型変換

result4 = x_tuple[2]
result5 = x_tuple + g_tuple
print(result4)
print(result5)


def test_function():
    t = 2 * 2
    u = 3 * 3
    return t, u

# 通常ver
result6, result7 = test_function()
print(result6, result7)

# タプルを表示ver
result8 = test_function()
print(result8)

# タプルで表示
x_dict = {'a': 100, 'b': 200, 'c': 300}
for i in x_dict.items():
    print(i)
