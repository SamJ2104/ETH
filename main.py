from os import system, name
from time import sleep
def clear():




    if name == 'nt':

        _ = system('cls')


    else:

        _ = system('clear')
line1 = " _____ _____ _   _ "
line2 = "|  ___|_   _| | | |"
line3 = "| |__   | | | |_| | "
line4 = "|  __|  | | |  _  |"
line5 = "| |___  | | | | | |  _   _   _"
line6 = "\____/  \_/ \_| |_/ (_) (_) (_)"
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(" ")
password = input("Password: ")
if password == "1234":
 sleep(3)
 clear()
 print("User: SamJ2104 - 0x0f8c6b4f8d9b8b5b7c2b")
 print(" ")
 print("Total Account Balance: ETH 0.32004")
 print("[1] Send ETH")
 print("[2] Receive ETH")
 print("[3] Send Tokens")
 print("[4] Receive Tokens")

else:
  print("Password Incorrect")