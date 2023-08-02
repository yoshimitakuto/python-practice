"クロージャー関数"
print('＝＝＝＝クロージャー関数＝＝＝＝')
def outside_area(pi):
    def inside_area(radius):
        return pi * radius * radius
    return inside_area

area1 = outside_area(3.14)
area2 = outside_area(3)

print(area1(2))
print(area2(2))

"関数内関数"
print('＝＝＝＝関数内関数＝＝＝＝')
def outline_area(a, b):
    def inline_area(c, d):
        return c - d
    
    x = inline_area(2, 1)
    y = inline_area(a, b)
    print(x)
    print(y)
    
outline_area(3, 1)

"デコレータ"
print('＝＝＝＝デコレータ＝＝＝＝')

print('＝＝＝＝デコレータ（無使用）＝＝＝＝')
def info(func):
    def wrapper(a, b):
        print('start')
        func(a, b)
        print('finish')
    return wrapper

def add(a, b):
    print(a + b)
    
add_result = info(add)
add_result(1, 2)
add_result(2, 4)

print('＝＝＝＝デコレータ（使用）＝＝＝＝')
def deko(f):
    def w(c, d):
        print('start')
        f(c, d)
        print('finish')
    return w

@deko #デコレータ（関数aにdekoの関数の処理を追加することができるもの）
def a(c, d):
    print(c + d)
    
a(1, 4)
a(2, 5)

print('===可変長位置引数===')
def show_number(*args):
    print(args)
    print(*args)
    for i in args:
        print(i)
    
show_number(1, 2, 3, 4, 5)

print('===可変長キーワード引数===')
def show_number2(**kwargs):
    print(kwargs)
    print(*kwargs)
    for i in kwargs:
        print(i)
        
d = {"n":1, "m":2, "l":3}
    
show_number2(a=1, b=2, c=3)
show_number2(**d)

print('＝＝＝＝デコレータ（使用）可変長位置引数・可変キーワード引数設定（こちらが現場では汎用性が高いためよく使用される）＝＝＝＝')
def out(function):
    def wra(*args, **kwargs): #*args(引数の位置で判断（一つのタプルとして受け取る）), **kwargs(辞書でキーと値が入る)
        print('start')
        function(*args, **kwargs) #再度定義することで値を展開して出力できる
        print('finish')
    return wra

@out
def add_result(e, f):
    print(e + f)

@out
def add_result2(e, f, g):
    print(e + f + g)
    
add_result(3, 5)
add_result2(5, 6, 8)
