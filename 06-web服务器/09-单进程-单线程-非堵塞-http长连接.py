import socket
import re

def service_client(new_socket, request):
    """为这个客户端返回数据"""
    # 1. 接收浏览器发送过来的请求
    # Get / HTTP/1.1
    # recv_data = new_socket.recv(1024).decode("utf-8")
    # print("客户端发送过来的请求是：%s"%recv_data)
    
    request_lines = request.splitlines()
    print("")
    print(">"*20)
    print(request_lines)
    
    file_name = ""
    # GET /index.html HTTP/1.1
    # get post put del
    ret = re.match(r"[^/]+(/[^ ]*) HTTP/1.1",request_lines[0])
    # 从/开始匹配，[^ ]取到空格之前停，*代表可以有可以无 
    if ret:
        file_name = ret.group(1)
        # print("*"*50,file_name)
        if file_name == "/":
            file_name = "/index.html"

    # 2.返回http格式的数据，给浏览器

    try:
        f = open("./html"+file_name,"rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += '-----file not found-----'
        new_socket.send(response.encode("utf-8"))
    else:    
        html_content = f.read()
        f.close()
        # 2.1 准备发送给浏览器的数据---header
        response_body = html_content
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n"% len(response_body)
        response_header += "\r\n"

        response = response_header.encode("utf-8") + response_body
        new_socket.send(response)
    

def main():

    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # 绑定本地信息
    tcp_server_socket.bind(("127.0.0.1",8080))

    # 让默认套接字由主动变为被动
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  #将套接字设为非堵塞

    client_socket_list=list()
    while True:
        try:
            new_client_socket, client_addr = tcp_server_socket.accept()
        except Exception as ret:
            pass
        else:
            new_client_socket.setblocking(False)
            client_socket_list.append(new_client_socket)

        for client_socket in client_socket_list:
            try:
                recv_data=client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                pass
            else:
                if recv_data:
                    service_client(client_socket,recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)

    # 关闭服务器
    tcp_server_socket.close()



if __name__ == "__main__" :
    main()
