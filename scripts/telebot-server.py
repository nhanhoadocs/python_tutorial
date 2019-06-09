#!/usr/bin/python3

import requests
import json
import os
import time

token = "your-token"

def get_message(token):
    #url = URL + "getUpdates"
    respon = requests.get("https://api.telegram.org/bot{}/getUpdates".format(token), timeout = 2)
    #print(respon.status_code)
    res = respon.content.decode("utf8")
    js = json.loads(res)
    last_update = len(js["result"]) - 1
    text = js["result"][last_update]["message"]["text"]
    date = js["result"][last_update]["message"]["date"]
    return (text, date)

def send_message(token, text):
    #text, date = get_message()
    requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id=your-chat-id&text={}".format(token, text), timeout = 2)

def command(text):
    com = "sshpass -p 'pass-server' ssh root@10.10.10.160 "
    cmd = com + text + " > telegram-file.txt 2> telegram-file.txt"
    os.system(cmd)

def w_file():
    text, date = get_message(token)
    date = str(date)
    file1 = open('file_date.txt','w')
    file1.write(date)
    file1.close()

def o_file(file):
    file1 = open(file)
    date0 = file1.read()
    return (date0)
while True:
    file = "file_date.txt"
    date0 = o_file(file)
    text, date = get_message(token)
    date = str(date)
    file2 = "telegram-file.txt"
    #tele_text = o_file("telegram-file")
    if date0 != date:
        #print(text)
        command(text)
        send_message(token, text)
        tele_text = o_file(file2)
        send_message(token, tele_text)
    w_file()
    time.sleep(5)

#w_file()
