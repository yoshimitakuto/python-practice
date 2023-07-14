""""
可変長引数
ある一つの関数で指定した引数が１つであっても、
＊を引数の頭に加えることで、自由な数だけ設定できる引数のこと

例：
def func(*age):
    print(age)
    
func(1) OK!
func(1, 3, 5) OK!


辞書で受け取る可変長引数
**とするだけ

例：
def func(**kwargs):
    print(kwargs)

func(name='斉藤')
func(name='鈴木, id=1, type='02')    
"""

def func(*args):
    print(args)
    
func(1)
func(1, 3, 5)


def func_name(*names):
    result = ', '.join(names)
    print(result)  

func_name('あ')
func_name('あ', 'A', 'a')  


# 通常引数と可変長引数は同時に使える
def func2(*args, x):
    result = ', '.join(args)
    print(f'{x}: {result}')

# キーワード引数（x＝○）    
func2('あ', x=1)
func2('い', 'I', 'i', x=2)    


def func3(x, **kwargs):
    print(f'{x}: {kwargs}')
    
func3(1, name='斉藤', user_id=222)
func3(2, item='牛乳', item_id=111, price=100)    