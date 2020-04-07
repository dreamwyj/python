def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a # 首先执行yield暂停,等再次调用时，进行 赋值
        print(">>>ret>>>",ret)
        a, b = b, a+b
        current_num += 1


obj2 = create_num(20)

ret = next(obj2) # 调用的yield后面 a的值
print("obj2:",ret)

ret2 = obj2.send(None) # 启动send时，从暂停的地方开始执行。这里的None传给 yield a,也就是说是yield a的返回结果。send里面的数据会传递给赋值的ret
# 第二次yield的值传入ret2中
# send的结果是下一次调用yield时，yield后面的值
print(ret2)
