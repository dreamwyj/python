""" 1.终端输入ipython3
    2.from collections import Iterable
      isinstance([11,22,33],Iterable)
      True

      isinstance("abc",Iterable)
      True

      isinstance(100,Iterable)100是否是迭代器Iterable的子类
      False
"""
"""
for temp in xxx:
    pass

1.判断xxx是否可以迭代
2.在第1步成立的前提下,调用iter函数
 得到xxx对象的__iter__方法的返回值
3.__iter__方法的返回值是一个迭代器
"""
# 实现自己

from collections.abc import Iterable
from collections.abc import Iterator
import time


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self): # 使创建的对象可以迭代
        """如果想要一个对象称为一个 可以迭代的对象，即可以使用for,
        那么必须使用__iter__方法"""
        return ClassIterator(self) # 调用自己


class ClassIterator(object):
    def __init__(self, obj): 
        self.obj = obj
        self.current_num=0 
    
    def __iter__(self):
        pass

    def __next__(self):
        if self.current_num < len(self.obj.names):
            ret = self.obj.names[self.current_num]
            self.current_num += 1

            return ret
        else:
            raise StopIteration


classmate = Classmate()

classmate.add("老王")
classmate.add("王二")
classmate.add("张三")


# ,表示元组
#print("判断classmate是否是可以迭代的对象:", isinstance(classmate, Iterable))
#classmate_iterator = iter(classmate)
#print("判断classmate_iterator是否是迭代器:", isinstance(classmate_iterator, Iterator))
#print(next(classmate_iterator))


for name in classmate:
    print(name)
    time.sleep(1)

