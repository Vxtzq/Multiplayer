import colorama
from colorama import Fore
import sys
from ursinanetworking import *
import subprocess
cmd = 'python3 client.py 1'
user = ""
pwd = ""
def loginorregister():
    loginregister = input("1 : s'identifier\n2 : s'authentifier\n3 : jouer en tant qu'invité\n")
    if "1" in loginregister:
        
        
        user = input(Fore.BLUE + "Entrez votre surnom : \n")
        pwd = input(Fore.BLUE + "Entrez votre mot de passe : \n")
        userpwd = ((user,pwd))
        try:
            client.send_message("pwd",("login",user,pwd))
        except:
            "Une erreur est survenue, le serveur n'est pas connecté"
    if "2" in loginregister:
        
        
        user = input(Fore.BLUE + "Entrez votre surnom : \n")
        pwd = input(Fore.BLUE + "Entrez votre mot de passe : \n")
        userpwd = ((user,pwd))
        try:
            client.send_message("pwd",("register",user,pwd))
        except:
            "Une erreur est survenue, le serveur n'est pas connecté"
    if "3" in loginregister:
        try:
            client.send_message("invite",None)
        except:
            "Une erreur est survenue, le serveur n'est pas connecté"
#from client import *
print(Fore.RED+"_______________________________________________________\n")
print(Fore.BLACK+"                  Exécuteur du client")
print(Fore.RED+"_______________________________________________________")
client = UrsinaNetworkingClient('192.168.1.23', 22625)
loginorregister()

    
@client.event
def login(Content):
    global cmd
    if content == True:
        subprocess.call(cmd, shell=True)
    else:
        print("Invalid username or password")
        loginorregister()
    
    
