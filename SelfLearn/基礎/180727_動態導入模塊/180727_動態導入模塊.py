# from module import t  # module/t.py，不想這麼導入
# module_t = __import__('module.t')
# print(module_t)  # => <module 'module' (namespace)>，最終返回的都是最頂層的模塊(此時為module)
#
# # module_t.test1()  # => error
# module_t.t.test1()  # => test1

# import importlib
# m = importlib.import_module("module.t")  # 直接返回需要的模塊
# print(m)  # => <module 'module.t' from 'D:\\PythonWork\\SelfLearn\\基礎\\180727_動態導入模塊\\module\\t.py'>
# m.test1()  # => test1
# m._test2()  # => test2



# from module.t import *
#
# test1()  # => test1
# # _test2()  # => error，_變量

# from module.t import test1,_test2
#
# test1()  # => test1
# _test2()  # => test2，這只是種約定還是可以被調用，只有import*時會被隱藏


