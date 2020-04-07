import socket
def main():

    # 1.买手机（创建套接字 socket）
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    # 2.插入手机卡（绑定本地信息 bind ip,port）
    tcp_server_socket.bind(("",7890))
    
    # 3.将手机设为正常，响铃模式（让默认套接字由主动变为被动 listen ）
    # 最大连接数量
    tcp_server_socket.listen(128)
    
    # 4.等待别人的电话到来（等待客户连接 accept）
    # 监听套接字负责等待有新的客户端进行连接
    # accept产生的新的套接字用来为客户端服务
    print("---1---")
    new_client_socket,client_addr= tcp_server_socket.accept()
    print("---2---")
    

    print(client_addr)

    # 接收客户端发送过来的请求
    recv_data=new_client_socket.recv(1024) # 接受普通数据
    print(recv_data)
    
    # 回送一部分数据给客户端
    new_client_socket.send("hahahah---ok---".encode("utf-8"))

    # 关闭套接字
    new_client_socket.close()
    # 关闭客户连接
    tcp_server_socket.close()
    # 关闭服务器连接





if __name__=="__main__":
    main()
