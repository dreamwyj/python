import threading
import time

def test1():
    for i in range(5):
        print("---test1---%d---"%i)


def test2():
    for i in range(5):
        print("---test2---%d---"%i)



def main():
    t1=threading.Thread(target=test1)
    t2=threading.Thread(target=test2)
    
    t1.start()

    time.sleep(1)
    print("---1---")
    
    time.sleep(1)
    t2.start()
    print("---2---")
    
    
    print(threading.enumerate())
    # 查看进程
    # time.sleep()让进程延迟运行

if __name__=="__main__":
    main()
