a = 1
b = 5
print(a + b)

x = ['a', 'b', 100]
y = ['e', 'f']
x.append('c')
y.remove('f')
z = x + y # もしくはx.extend(y)
print(z)

# 開始：終了インデックスあり
t = ['a', 'b', 'c', 'd', 'e']
print(t[1:4])

# 開始インデックスなし
u = ['a', 'b', 'c', 'd', 'e']
print(u[:4])

# 終了インデックスなし
i = ['a', 'b', 'c', 'd', 'e']
print(i[2:])