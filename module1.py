import module2
from sub_folder1 import sub_module1
from sub_folder1.sub_sub_folder import sub_sub_module


def main():
    module2.func2()
    sub_module1.sub_func1()
    sub_sub_module.sub_sub_func()
    
if __name__ == '__main__':
    main()