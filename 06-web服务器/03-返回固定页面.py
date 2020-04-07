import socket

def service_client(new_socket):
    """为这个客户端返回数据"""
    # 1. 接收浏览器发送过来的请求
    # Get / HTTP/1.1
    recv_data = new_socket.recv(1024)
    print("客户端发送过来的请求是：%s"%recv_data.decode("utf-8"))
    
    # 返回http格式的数据，给浏览器
    # 2.1 准备发送给浏览器的数据---header
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    # 2.2 准备发送给浏览器的数据---body
    # response +="hahahaha"

    f = open("./html/index.html","rb")
    html_content = f.read()
    f.close()
    
    # 将response header发送给浏览器
    new_socket.send(response.encode("utf-8"))
    # 将response body发送给浏览器
    new_socket.send(html_content)

    # 关闭套接字
    new_socket.close()



def main():

    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # 绑定本地信息
    tcp_server_socket.bind(("127.0.0.1",8080))

    # 让默认套接字由主动变为被动
    tcp_server_socket.listen(128)
    while True:
        print("等待客户端的到来...")
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("客户端已经到来%s"%str(client_addr))
        # 接收客户端发送过来的数据
        service_client(new_client_socket)
        print("服务完毕")
    # 关闭服务器
    tcp_server_socket.close()



if __name__ == "__main__" :
    main()
