"""
【例外処理】

実際は外部とデータをやり取りする部分に
例外処理を書くことが多い。
例：ファイルの読み書きやデータベースの読み書き等
"""

x = 1
y = 1

try:
    result = x / y
except ZeroDivisionError as e:
    print('ゼロで割ることはできません')
    print(e)
except NameError as e:
    print('変数が定義されていません')
    print(e)
else:
    print(result)
    print('正常に計算しました')  
finally:
    print('割り算を終了します') 
    

# システム終了以外の全例外を検知
u = 1

try:
    result = u / i
except Exception as w:
    print('例外が発生しました')
    print(w)