def func2():
    print('func2です')
    
# この状態だとmodule1の方でもfunc3が呼び出されてしまう。
# def func3():
#         print('func3です')
        
# func3()      

# いかに修正すると呼び出されなくなる
def func3():
    print('func3です')
    
if __name__ == '__main__':
    func3()