x = {'りんご': 120, 'バナナ': 300, 'いちご': 450}
y = {'マンゴー': 600, '梨': 180}
# キーと値を追加
x['トマト'] = 340
# キーの値を変更
x['りんご'] = 150
banana = x['バナナ']
# 結合（3.9ver以上でのみ使用可能）
z = x | y #x.update(y)でも同様
# 要素数を取得
z_len = len(z)

print(banana)
print(z)
print(z_len)