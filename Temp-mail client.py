import os
from mailtm import Email

def menu():
    os.system('cls')
    print("Temp-mail client by Ema - powered by https://mail.tm/\n\n┌───────────┬──────────┬─────────────┐\n│ 1: Create │ 2: Login │ Enter: exit │\n├───────────┴──────────┴─────────────┘")
    choice=input("└ ")
    if choice == "1":
        create()
    elif choice == "2":
        login()
    elif choice == "":
        os.system('cls')
        exit()
    else:
        menu()

def listener(message):
    print("\n[-] Subject: " + message['subject'])
    print("Content: " + message['text'] if message['text'] else message['html'])

def create():
    os.system('cls')
    print("Create\n")
    username = input("[+] Username (leave blank for random): ")
    password = input("\n[+] Create password: ")
    test.register(username=username, password=password)        
    print("\n[!] Email adress created: " + test.address)
    start()

def login():
    os.system('cls')
    print("Login\n")
    address = input("[+] Email adress: ")
    password = input("\n[+] Password: ")
    test.address=address
    test.get_token(password=password)
    print("\n[!] Logged in as: " + test.address)
    start()

def start():
    test.start(listener)
    print("\n[!] Waiting for new emails...")

test = Email()

menu()