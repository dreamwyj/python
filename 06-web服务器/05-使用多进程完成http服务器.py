import socket
import re
import multiprocessing

def service_client(new_socket):
    """为这个客户端返回数据"""
    # 1. 接收浏览器发送过来的请求
    # Get / HTTP/1.1
    recv_data = new_socket.recv(1024).decode("utf-8")
    # print("客户端发送过来的请求是：%s"%recv_data)
    

    request_lines = recv_data.splitlines()
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
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        # 2.2 准备发送给浏览器的数据---body
        # response +="hahahaha"
        # 将response header发送给浏览器
        new_socket.send(response.encode("utf-8"))
        # 将response body发送给浏览器
        new_socket.send(html_content)

    

    # 关闭套接字
    new_socket.close()
# 多进程，创建子进程时，会有两个变量指向一个接口


def main():

    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # 2.绑定本地信息
    tcp_server_socket.bind(("127.0.0.1",8080))

    # 3.让默认套接字由主动变为被动
    tcp_server_socket.listen(128)

    while True:
        print("等待客户端的到来...")
        # 4.等待新客户端的链接
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("客户端已经到来%s"%str(client_addr))

        # 5.为这个客户端服务
        p = multiprocessing.Process(target = service_client,args = (new_client_socket,))
        p.start()
        # service_client(new_client_socket)
        new_client_socket.close()

    # 关闭服务器
    tcp_server_socket.close()



if __name__ == "__main__" :
    main()
