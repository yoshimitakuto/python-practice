last_name = ['鈴木', '斉藤', '田中']
first_name = ['たろう', 'たかし', 'あつひろ']

full_name = list(map(lambda nl, nf: nl + nf  + 'さん', last_name, first_name ))
print(full_name)