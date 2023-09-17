import colorama
from colorama import Fore
import sys

from client import *
print(color.colors)
App = Ursina(borderless=False)
width = 800
height = 600
window.size = (width,height)
ifregister = 0
iflogin = 0
#username = None
#password = None
usernametext = ""
user = ""
pwd = ""
updateok = 0
username,password = None,None
    
def registerbtn():
    global register,login,ifregister
    ifregister = 1
    destroy(register)
    destroy(login)
    
    
def loginbtn():
    global register,login,iflogin
    iflogin = 1
    destroy(register)
    destroy(login)
    


background = Entity(model='quad', color=color.gray, position=(0,0,1), scale=(100,100,1))
#te = TextField(max_lines=1, register_mouse_input = True,color=color.black,scale=1,character_limit = 50)

#te.render()

#print(Fore.RED + 'This text is red in color')
register = Button(text='Register', color=color.dark_gray, scale=(.25,.10,.1), text_origin=(0,0))
register.on_click = registerbtn # assign a function to the button.
register.position = (0,0.1,0)
#register.tooltip = Tooltip('register')
login = Button(text='Login',position=(0,0,0), color=color.dark_gray, scale=(.25,.10,.1), text_origin=(0,0))
login.on_click = loginbtn # assign a function to the button.
register.position = (0,0.2,0)

 

def update():
    global ifregister,iflogin,updateok,username,password
    
        
        
    if ifregister == 1:
        validation = Button(text='Validate', color=color.dark_gray, scale=(.25,.10,.1), text_origin=(0,0))
        validation.position = (0,-0.1,0)
        validation.on_click = valid
        ifregister = 0
        updateok = 1
        username=InputField(y=0.1)
        password=InputField()
        #(username,password) # assign a function to the button.
    
    if updateok == 1:
        
        user = username.text
        pwd = password.text
        print(user,pwd)
        
   
    
def valid():
    global user,pwd
    App.destroy()
    client((user,pwd))
    quit()
    
    
    
    

App.run()
