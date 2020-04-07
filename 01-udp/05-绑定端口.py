import socket

def main():
    #1.创建套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #2.绑定一个本地信息
    localaddr=("",7788)
    udp_socket.bind(localaddr)
    #3.接受数据
    recv_data=udp_socket.recvfrom(1024) #接受本次接受最大字节数
    #4.打印接受到的数据
    print(recv_data)
    #5.关闭套接字
    udp_socket.close()

if __name__=="__main__":
    main()
