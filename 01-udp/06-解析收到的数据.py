import socket


def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定一个本地信息
    localaddr = ("", 7788)  # 必须绑定自己的端口号和ip
    udp_socket.bind(localaddr)
    # 3.接受数据
    recv_data = udp_socket.recvfrom(1024)  # 接受本次接受最大字节数
    # recv_data这个变量存储的是一个元组
    #（接受到的数据,发送方的ip,port）
    recv_msg = recv_data[0]  # 存储接受到的数据
    recv_addr = recv_data[1]  # 存储发送方的地址信息
    # 4.打印接受到的数据
    # print(recv_msg)
    print("%s:%s" % (str(recv_addr), recv_msg.decode("gbk")))  # gbk编码解析中文
    # 5.关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
