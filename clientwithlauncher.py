from ursinanetworking import *
from ursina.prefabs.first_person_controller import FirstPersonController

client = UrsinaNetworkingClient('192.168.1.34', 22625)
content = []
counter = 0
App = Ursina()
Id = 0
x,y = 0,0
pos_list = []
playersingame = 0
otherplayers = []
delindexes = []
realclients = []
view = 1
client = 0
lastplayersingame = 0
def client():
    ground = Entity(model = "ground.obj", scale = (10,1,10), color = color.white, texture = "white_cube", texture_scale=(10,10), collider="mesh")
    player = FirstPersonController(origin_x=0,origin_z=0,origin_y=5, mouse_sensivity=Vec2(40,40),jump_height=2,collider = 'cube')
    #playertest = Entity(model = "person.obj",position=(0,0), color=color.white)
    deadclients = 0
    createid = 0
    playerobj = Entity(model = "person.obj", color = color.green,collider='person.obj')
    @client.event
    def onConnectionEtablished():
        print('Client successfully connected!')


    @client.event
    def onConnectionError(Reason):
        print('Client failed to connect, the reason is : '+Reason)
    @client.event
    def ID(Content):
        global Id,createid
        print(Content)
        Id = int(Content[0])
        createid = int(Content[1])
        print(Id)
    @client.event
    def xandyotherplayers(Content):
        global createid,realclients,deadclients,content,Id, playersingame,lastplayersingame,pos_list,other_players,counter
        #pos_list = Content.pop(Id)
        #print(len(pos_list))
        playersingame = len(Content)-1
        content = Content
        #print(Id)
        try:
            del content[Id]
        except:
            pass
        #print(content)
        #print(Content)

        realclients.clear()
        for pos in content:
            if pos != 1:
                realclients.append(pos)
            else:
                deadclients +=1
        print(len(realclients))

        #del realclients[createid]
        print(realclients)
        print(otherplayers)

        if len(otherplayers) >len(realclients):
            #delindexes.append(content.index(pos))
            destroy(otherplayers[0])
            del otherplayers[0]
        if len(otherplayers) <len(realclients):
            otherplayer = Entity(model = "person.obj", color = color.white, texture = "white_cube", texture_scale=(10,2),collider='person.obj')
            otherplayers.append(otherplayer)
        if len(realclients) > 0:
            for client in realclients:
                #print(len(realclients))
                otherplayers[counter].position = (client)
                counter +=1

            counter = 0


    def update():

        global x,y,Id,player,playerobj
        #print(player.x)
        client.send_message("xycoords",(player.x,player.y,player.z,Id))
        playerobj.position = (player.x,player.y,player.z)
        client.process_net_events()
        if held_keys["a"]:
            x-=0.1
        if held_keys["d"]:
            x+=0.1
        if held_keys["w"]:
            y+=0.1
        if held_keys["s"]:
            y-=0.1
        if held_keys["q"]:
            client.send_message("clientdisconnect",Id)
            quit()
        if player.y <= -20:
            player.y = 5
            player.x =0
            player.z=0
    def input(keys):
        global view
        if keys == 't':
            view = -view
            if view == 1:
                camera.z = 0
            else:

                camera.z = -8
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
    

entities = []
background = Entity(model='quad', color=color.gray, position=(0,0,1), scale=(100,100,1))
#te = TextField(max_lines=1, register_mouse_input = True,color=color.black,scale=1,character_limit = 50)
entities.append(background)
#te.render()

#print(Fore.RED + 'This text is red in color')
register = Button(text='Register', color=color.dark_gray, scale=(.25,.10,.1), text_origin=(0,0))
register.on_click = registerbtn # assign a function to the button.
register.position = (0,0.2,0)
entities.append(register)
#register.tooltip = Tooltip('register')
login = Button(text='Login',position=(0,0,0), color=color.dark_gray, scale=(.25,.10,.1), text_origin=(0,0))
login.on_click = loginbtn # assign a function to the button.
entities.append(login)

if client == 0:
    def update():
        global ifregister,iflogin,updateok,username,password,entities
    
        
        
        if ifregister == 1:
            validation = Button(text='Register', color=color.dark_gray, scale=(.25,.10,.1), text_origin=(0,0))
            validation.position = (0,-0.1,0)
            validation.on_click = valid
            entities.append(validation)
            ifregister = 0
            updateok = 1
            username=InputField(y=0.1)
            password=InputField()
            entities.append(username)
            entities.append(password)
            #(username,password) # assign a function to the button.
        
        if updateok == 1:
            
            user = username.text
            pwd = password.text
            print(user,pwd)
        
   
    
    def valid():
        global user,pwd,entities
        
        client()
        for entity in entities:
            destroy(entity)

App.run()
