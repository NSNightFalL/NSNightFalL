import hashlib
import colorama
import os
import random
import time
import aiohttp
from colorama import Fore
from colored import fg, attr
b = Fore.LIGHTBLACK_EX
r = Fore.RESET
global g
g = g = fg('#E23C3C')
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
import sys
import ctypes
import subprocess


def setTitle():
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{g} - Made By NightFalL")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{g} - Made By NightFalL#2758\x07")
    else:
        pass



# Directory
directory = "Background cache"
  
# Parent Directory path
parent_dir = "C:\Program Files"
  
# mode
mode = 0o666
  
# Path
path = os.path.join(parent_dir, directory)
  
# Create the directory
# '' in
# '/home / User / Documents'
# with mode 0o666
try:
    os.mkdir(path, mode)
    print("Directory '% s' created" % directory)
    time.sleep(2)
except OSError as error:
    print(error)
    pass




def menu():
    print(f'''
                            {g}$$\\                         $$\\            
                        {g}$$ |                        \\__|           
                        {g}$$ |     $$$$$$\\   $$$$$$\\  $$\\ $$$$$$$\\   
                        {g}$$ |    $$  __$$\\ $$  __$$\\ $$ |$$  __$$\\  
                        {g}$$ |    $$ /  $$ |$$ /  $$ |$$ |$$ |  $$ | 
                        {g}$$ |    $$ |  $$ |$$ |  $$ |$$ |$$ |  $$ | 
                        {g}$$$$$$$$\\$$$$$$  |\\$$$$$$$ |$$ |$$ |  $$ | 
                        {g}\\________\\______/  \\____$$ |\\__|\\__|  \\__| 
                                        {g}$$\\   $$ |               
                                        {g}\\$$$$$$  /               
                                        {g}\\______/      

                        {g}$$\\      $$\\                               
                        {g}$$$\\    $$$ |                              
                        {g}$$$$\\  $$$$ | $$$$$$\\  $$$$$$$\\  $$\\   $$\\ 
                        {g}$$\\$$\\$$ $$ |$$  __$$\\ $$  __$$\\ $$ |  $$ |
                        {g}$$ \\$$$  $$ |$$$$$$$$ |$$ |  $$ |$$ |  $$ |
                        {g}$$ |\\$  /$$ |$$   ____|$$ |  $$ |$$ |  $$ |
                        {g}$$ | \\_/ $$ |\\$$$$$$$\\ $$ |  $$ |\\$$$$$$  |
                        {g}\\__|     \\__| \\_______|\\__|  \\__| \\______/ 
                        {g}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
                            {g}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{r}                                                        
                      {g}╔═══════════════════╗       ╔════════════════════╗
                      ║ {r}made by NightFalL{g} ║       ║{r}NightFalL#2758{g}      ║ 
                    ╔═══════════════════════╗   ╔═══════════════════════╗
                    ║{r}1 {g}:{r}Login               {g}║   ║{r}3 {g}:{r} Exit  {g}             ║
                    ║{r}2 {g}:{r}Sign up             {g}║   ║{r}4 {g}:{r} Credits\\Other {g}     ║
                    ╚═══════════════════════╝   ╚═══════════════════════╝{r}  

    
''')
setTitle()
menu()

def menu2():
    menu()
    start()

def Credit():
      os.system(f'title - Credits')
      print(f'''
                          {g}
                          \033[90m█▀▀ █▀█ █▀▀ █▀▄ █ ▀█▀ █▀
                          \033[37m█▄▄ █▀▄ ██▄ █▄▀ █ ░█░ ▄█
                            {g}[\033[37m{g}] \033[37mhelper TheTurtle#6616
                            {g}[\033[37m{g}] \033[37mdeveloper  NightFalL#2758
        \033[37m''')

    

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return




def Spinner():
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Loading... {i}""")
        sys.stdout.flush()
        time.sleep(0.2)


def transition():
    clear()
    Spinner()
    clear()


def transition2():
    clear()
    Spinner2()
    clear()


def Spinner2():
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Loading... {i}""")
        sys.stdout.flush()
        time.sleep(0.1)



def signup():
    clear()
    transition2()
    email = input("Enter email address:")
    pwd = input("Enter password:")
    conf_pwd = input("Confirm password:")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("C:\Program Files\Background cache/credentials.txt", "w") as f:
             f.write(email + "\n")
             f.write(hash1)
        f.close()
        print("You have registered successfully!")
    else:
         print("Password is not same as above! \n")
         time.sleep(2)
         clear()
         transition2()
         clear()
         menu()
         start()


def login():
    clear()
    email = input(f'{r}[{g}~{r}] {g}Enter Email{r}: ')
    pwd = input(f'{r}[{g}~{r}] {g}Enter Password{r}: ')
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("C:\Program Files\Background cache/credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if email == stored_email and auth_hash == stored_pwd:
         print(f"{y}Logged{w} in {g}Successfully!{r}")
         clear()
         menu2()
    else:
         print(f'{y}[{g}~{y}] {w}Login Failed{r} ')
         time.sleep(2)
         clear()
         transition2()
         clear()
         menu2()
         

def start():
    while True:
        global g
        g = g = fg('#E23C3C') 
        ch = input(f'{r}[{g}~{r}] {g}Choice{r}: ')
        if ch == '1':
            if ch == '1' or 'login':
                transition()
                login()

        if ch == '2':
            if ch == '2' or 'sign up':
                clear()
                signup()

        if ch == '3':
            if ch == '3' or 'exit':
                sys.exit()

        if ch == '4':
            if ch == '4' or 'credits':
                clear()
                Credit()
                while True:
                    exit = input(f'{r}[{g}~{r}] {g}> again to exit{r}: ')
                    if exit == '>':
                        clear()
                        menu()
                        return start()
                    else:
                        print("Wrong Choice!")
                        time.sleep(2)
                        clear()
        if ch == 'cls':
            clear()
            menu2()
            
start()

