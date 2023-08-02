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