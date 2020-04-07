# 在一个函数中对全局变量进行修改的时候，查看到底是否修改对全局变量的指向进行修改。
# 如果修改了指向，即让执行变量指向一个新的地方，那么必须用global。如果仅仅修改指向空间的数据，此时不用必须使用global

num=100
nums=[11,22]

def test():
    global num
    num+=100


def test2():
    nums.append(33)



print(num)
print(nums)

test()
test2()


print(num)
print(nums)
