from mailtm import Email
import os

def listener(message):
    print("\n[-] Subject: " + message['subject'] + "\nContent: " + message['text'] if message['text'] else message['html'])

def menu():
    os.system('cls')
    choice=input("Temp-mail client by Ema - powered by https://mail.tm/\n\n┌───────────┬──────────┬─────────────┐\n│ 1: Create │ 2: Login │ Enter: exit │\n├───────────┴──────────┴─────────────┘\n└ ")
    if choice == "1":
        create()
    elif choice == "2":
        login()
    elif choice == "":
        os.system('cls')
        exit()
    else:
        menu()

def create():
    os.system('cls')
    test.register(username=input("Create\n\n[+] Username (leave blank for random): "), domain=input("\n[+] Domain (leave blank for random): "), password=input("\n[+] Create password: ")) # awgarstone.com - mailtub.com
    print("\n[!] Email adress created: " + test.address)
    start()

def login():
    os.system('cls')
    test.address = input("Login\n\n[+] Email adress: ")
    test.get_token(password=input("\n[+] Password: "))
    print("\n[!] Logged in as: " + test.address)
    start()

def start():
    test.start(listener)
    print("\n[!] Waiting for new emails...")

test = Email()

menu()
