x = 'apple'
result = x == 'apple'
print(result)

y = 'apple'
z = ['apple', 'banana']
result_str = y in z
print(result_str)

age = 20
gender = '女性'
result_human = (age >= 20) and (gender == '女性')
print(result_human)

age2 = 20
gender2 = '女性'
result_human2 = (age2 >= 20) or (gender2 == '男性')
print(result_human2)

age3 = 19
result_human3 = not (age3 >= 20)
print(result_human3)