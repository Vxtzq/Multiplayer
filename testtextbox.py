from ursina import *

App = Ursina(borderless=False)
width = 800
height = 600
window.size = (width,height)
user = ""
usernametext = ""

username=InputField(y=0.1)
password=InputField()




        
def update():
    print(username.text)

App.run()
