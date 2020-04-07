import threading
import time

# 在哪里创建线
def test1():
    for i in range(5):
        print("---test1---%d---"%i)
        time.sleep(1)

def main():
    # 在调用Thread之前先打印当前线程信息
    print(threading.enumerate())
    t1=threading.Thread(target=test1)
   
    # 在调用Thread之后打印当前线程信息   
    print(threading.enumerate())

    t1.start()
    
    print(threading.enumerate())


if __name__=="__main__":
    main()
