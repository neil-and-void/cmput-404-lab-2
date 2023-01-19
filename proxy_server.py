#!/usr/bin/env python3
import socket
import time

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        try:
            #continuously listen for connections
            while True:
                conn, addr = s.accept()
                print("Connected by", addr)
                
                #recieve data, wait a bit, then send it back
                # get the host name from the 
                full_data = conn.recv(BUFFER_SIZE)

                # perform outgoing query
                host = "www.google.com"
                buffer_size = 4096

                http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

                remote_ip = socket.gethostbyname(host)

                http_socket.connect((remote_ip, 80));
                
                http_socket.send(full_data)
                # perform outgoing request end

                #continue accepting data until no more left
                response_data = b""
                while True:
                    data = http_socket.recv(buffer_size)
                    if not data:
                        break
                    response_data += data
                
                time.sleep(0.5)
                conn.sendall(response_data)
                
                conn.close()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
