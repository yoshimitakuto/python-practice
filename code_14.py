"""
【命名規則について】

変数名
・スネーク型: 小文字 + _
user_name
address

定数名
・アッパースネーク型: 大文字 + _
FILE_NAME

クラス名
・CapWords方式: 単語の先頭だけ大文字
UserClass

関数名・メソッド名
・スネーク型: 小文字 + _
update_password()


<< 命名のコツ >>
・変数や関数名は意味のある命名をする。
例:(bad)
def function(x, y):
    result = y + x + 'さん'
    return result
    
例:(good)
def get_full_name(given_name, surname):
    full_name = surname + given_name + 'さん'
    return full_name
   
    
・対になっている対義語・反対語を使う
=============
・start（動き始める） ⇔ stop（止まる / 止める）
・begin（取りかかる） ⇔ end（完結）, finish（段階的な終わり）
・top（上） ⇔ bottom（下）
・up（上がる） ⇔ down（下がる）
・under（未満） ⇔ over（以上）
・next（次） ⇔ current（今） ⇔ previous（前）
・front, fore（前） ⇔ back, rear（うしろ）
・head（頭） ⇔ tail（尾）, foot（足）
・first（最初） ⇔ last（最後）
・insert（挿入） ⇔ update（更新） ⇔ delete（削除）
・create（作る） ⇔ destroy（壊す / 破棄する）
・add（加える） ⇔ remove（取り除く）
=============  

・Bool型はどちらがTureでFalseかわかるようにする。
例:(bad)
student_flag = Ture

例:(good)
is_student = Ture

1, is + 名詞/形容詞
is_student = True
2, has + 名詞
has_card = True  (カードを持っている)
3, can + 動詞    
can_login = True  （ログインができる）


型情報を持つシステムハンガリアン記法をむやみに使用しない。
(変数名の頭や後ろに型情報をつける方法)
例:(bad)
str_price = '1200円'
error_code_int = 404

※型変換やあえて表現したい時以外は使用しないようにする！
"""