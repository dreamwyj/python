# 生成器是一种特殊的迭代器
# yield 会让程序暂停，并且下次继续从这里开始执行

def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
       # print(a)
        yield a # 如果一个函数中有yield语句，那么这个就不再是函数，而是一个生成器的模板
        a, b = b, a+b
        current_num += 1
    return "---ok---"


# 如果在调用create_num的时候，发现这个函数中有yield，那么此时不是调用函数，而是创建一个生成器对象
obj2 = create_num(20)

while True:
    try:
        ret = next(obj2)
        print("obj2:",ret)
    except StopIteration as wrong:
        print(wrong.value)
        break

