x = 9
if x >= 10:
    print('10以上')
elif x >= 0:
    print('10以上0未満')
else:
    print('0未満')
    

x_list = [100, 190, 2980]
for x in x_list:
    x_yen = str(x) + "円"
    print(x_yen)
    

x_dict = {'apple': 100, 'banana': 350}
for key, value in x_dict.items():
    text = key + 'は' + str(value) + '円です'
    print(text)