import socket
import time

def main():

    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setblocking(False)
    client_socket_list = list()
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # 2.绑定本地信息
    tcp_server_socket.bind(("127.0.0.1",8080))

    # 3.让默认套接字由主动变为被动
    tcp_server_socket.listen(128)
    
    while True:
        #        time.sleep(0.5)

        print("等待客户端的到来...")
        # 4.等待新客户端的链接
        try:
            new_client_socket, client_addr = tcp_server_socket.accept()
            print("客户端已经到来%s"%str(client_addr))
        except Exception as ret:
            print(ret)
            print("---没有新的客户端到来---")
        else:
            print("---只要没异常，意味着来了一个新的客户端---")
            new_client_socket.setblocking(False) # 设置套接字为非堵塞方式
            client_socket_list.append(new_client_socket)

        # 5.为这个客户端服务
        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                print("----这个客户端没有发送过来数据----")
            else:
                if recv_data:
                    # 对方发送过来数据
                    print("----这个客户端发送过来数据----")
                    print(recv_data)
                else:
                    # 对方调用close 导致recv返回
                    client_socket_list.remove(client_socket)
                    client_socket.close()
                    print("---客户端已经关闭---")
    # 关闭服务器
    tcp_server_socket.close()



if __name__ == "__main__" :
    main()
