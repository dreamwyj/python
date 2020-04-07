import socket


def main():
    # 1.创建一个udp套字节
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 可以使用套字节收发数据

    # 请输入对方ip和端口号
    dest_ip = input("请输入对方ip:")
    dest_port = int(input("请输入对方port:"))

    # 2.获取数据
    send_data = input("请输入要发送的数据：")
    # udp_socket.sendto("hahaha",对方的ip以及port)
    # udp_socket.sendto(b"hahaha", ("192.168.0.102", 8080))
   # udp_socket.sendto(send_data.encode("utf-8"),("192.168.0.102", 8080))
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

    # 接受回过来的数据
    recev_data = udp_socket.recvfrom(1024)
    print(recev_data)
    # 套接字可以同时收发数据

    # 3.关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
