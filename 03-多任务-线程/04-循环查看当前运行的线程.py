import threading
import time

def test1():
    for i in range(5):
        print("---test1---%d---"%i)
        time.sleep(1)

def test2():
    for i in range(10):
        print("---test2---%d---"%i)

        time.sleep(1)


def main():
    t1=threading.Thread(target=test1)
    t2=threading.Thread(target=test2)
    
    t1.start()
    t2.start()
    
    while True:
        print(threading.enumerate())
        if len(threading.enumerate())<=1:
                break
        time.sleep(1)
        


    # 查看进程
    # time.sleep()让进程延迟运行
    # 如果创建Thread时，执行的函数运行结束，则这个子线程结束
    # 主线程结束，程序结束

if __name__=="__main__":
    main()
