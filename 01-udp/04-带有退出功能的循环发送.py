import socket


def main():
    # 创建一个udp套字节
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 可以使用套字节收发数据
    # udp_socket.sendto("hahaha",对方的ip以及port
    # b+字符串 二进制
    #udp_socket.sendto(b"hahaha", ("192.168.0.102", 8080))
    #
    while True:
        send_data=input("请输入要发送的数据：")
        if send_data=="exit":
            break
        udp_socket.sendto(send_data.encode("gbk"),("192.168.0.102", 8080))
    udp_socket.close()


if __name__ == "__main__":
    main()
