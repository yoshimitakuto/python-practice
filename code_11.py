"""
ファイルオブジェクト
with open(ファイルパス, モード) as f:
    ファイル操作

〜モード一覧〜
'r': 読み込み（デフォルト）
'w': 書き込み
'a': 追記
'r+': 読み込み + 書き込み
"""



# 既存ファイルの記載内容を取得し、4行目になったら終了文字列表示
# readlineは行の末尾まで来て値がなかった場合から文字を返す
with open('test.text') as f:
    for _ in range(4):
        s_line = f.readline()
        print(s_line)
        if s_line == '':
            print('終了です')
            
            
# 全ての行をリストで取得            
with open('test.text') as g:
    r_line = g.readlines()
    print(r_line)
    

# 新規ファイル作成をして書き込み（w）
with open('test2.txt', 'w') as w:
    w.write('あああ\nいいい\nううう')
    

# 上記で作成したファイルに追記　※末尾に追加される。（a）
with open('test2.txt', 'a') as a:
    a.write('\nえええ\nおおお')
    

# リストのデータを書き込み（繋がって文字列が1行に出力）
x_list = ['apple', 'orange', 'banana']
with open('text3.txt', 'w') as x:
    x.writelines(x_list)
    
# リストデータを改行指定で書き込み    
y_list = ['tea', 'rice', 'ramen']
y = '\n'.join(y_list)
with open('test4.txt', 'w') as u:
    u.write(y)
    
# 自作してみた。
h_list = ['', 'go', 'ruby', 'python']
i = '\n'.join(h_list)
with open('test4.txt', 'r+') as h:
    for _ in range(5):
        h_line = h.readline()
        print(h_line)
        if h_line == 4 and 5:
            print('4行目か5行目に値があります')
            print(h_lien[4])
            print(h_lien[5])
        elif h_line == '':
            print('終了です')
            break
        else:
            print(h_line)
    h.write(i)
            