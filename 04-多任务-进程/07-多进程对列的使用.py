from multiprocessing import Queue

if __name__=='__main__':
    q=Queue(3)
    q.put("消息1")
    q.put("消息2")
    print(q.full())
    q.put("消息3")
    print(q.full())

    # 因为消息列队已满，下面的try都会抛出异常，
    # 第一个try会等待2秒再抛出异常

    try:
        q.put("消息4",True,2)
    except:
        print("消息队列已满，现有消息数量:%s"%q.qsize())

    try:
        q.put_nowait("消息4")
    except:
        print("消息队列已满，现有消息数量:%s"%q.qsize())

    #读取消息，先判断消息队列是否为空,再读取
    if not q.empty():
        print("----从队列中获取消息---")
        for i in range(q.qsize()):
            print(q.get_nowait())
    # 先判断消息队列是否已满，再写入
    if not q.full():
        q.put_nowait("消息4")
