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

""
print('＝＝＝＝関数内関数＝＝＝＝')