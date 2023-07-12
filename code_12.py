"""
三項演算子の書き方
True時に返す値 if 条件 else False時に返す値
    ①          ②          ③

例: ageが20以上は成人、それ以外は子供（通常ver）
result = '成人' if age >= 20 else '子供'

例: ageが20以上は成人、1以上は子供、それ以外は赤ちゃん（ネストver）
result = '成人' if age >= 20 else '子供' if age >= 1 else '赤ちゃん'

メリット
・スッキリした構文が書ける。
・ネスト構造でも1行で書ける。

デメリット
・elifは使えない（しかしネスト構造で実現はできる）
"""


age = 0.5
result = '成人' if age >= 20 else '子供' if age >= 1 else '赤ちゃん'
print(result)