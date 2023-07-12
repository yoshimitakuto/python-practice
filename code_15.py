"""
【リスト内包表記】
リストを簡単に生成するための表記（forを使って1行で書ける）


リスト内表表記でない書き方 => 1~10までを繰り返しでリストを作成する。
x = []
for i in range(11):
    x.append(i)
    
リスト内包表記
[式 for 変数 in 繰り返しオブジェクト]    
[i for i in range(11)]    

条件付きリスト内包表記 => 0〜10までの数値の中で偶数のみリスト化
[式 for 変数 in 繰り返しオブジェクト 条件式]    
[i for i in range(11) if i % 2 == 0] Trueの時だけ新しいリストの要素となる

三項演算子付きのリスト内包表記 => 0〜10までの数値の中で偶数だけ「ぐ」になるリスト
[Trueの時の値 if 条件式 else Flaseの時の値 for 変数 in 繰り返しオブジェクト]
['ぐ' if i%2 == 0 else i for i in range(11)]
"""

x = [i + 1000 for i in range(6)]
print(x)

names = ['斉藤', '山田', '田中']
y = [i + 'さん' for i in names]
print(y)

# 奇数のみ表示
g = [i for i in range(11) if i % 2 == 1]
print(g)

foods = ['apple', 'banana', 'lemon']
s = [i for i in foods if 'a' in i]
print(s)

x1 = [i for i in range(6)]
x2 = ['ぐ' if i % 2 == 0 else i for i in range(6)]
print(x1)
print(x2)

kanto = ['千葉', '栃木', '東京', '埼玉', '茨城', '群馬', '神奈川']
x3 = [i + '都' if i == '東京' else i + '県' for i in kanto]
print(x3)