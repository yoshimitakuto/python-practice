# lambda + map（組み込み）使用
# 繰り返しオブジェクトの中で全ての要素にある処理を実行する関数
last_name = ['鈴木', '斉藤', '田中']
first_name = ['たろう', 'たかし', 'あつひろ']

full_name = list(map(lambda nl, nf: nl + nf  + 'さん', last_name, first_name ))
print(full_name)


# lambda + filter（組み込み）使用
# 繰り返しオブジェクトの中である条件がTrueになる要素だけ抽出する関数
numbers = [4, 5, 6, 7, 8]
result = list(filter(lambda x: x >= 6, numbers))
print(result)