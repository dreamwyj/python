import threading
import time
import multiprocessing

def test1():
    while True:
        print("1.-----")
        time.sleep(1)



def test2():
    while True:
        print("2.-----")
        time.sleep(1)

def main():

 #    t1 = threading.Thread(target=test1)
 #    t2 = threading.Thread(target=test2)
 #    t1.start()
 #    t2.start()

     t1 = multiprocessing.Process(target=test1)
     t2 = multiprocessing.Process(target=test2)
     t1.start()
     # 对主进程的代码复制一份，代码不会改变，数据会复制改变，写时拷贝
     t2.start()
        

if __name__ == "__main__":
    main()

