from ursinanetworking import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader
from playertest import *

score = 0
client = UrsinaNetworkingClient('192.168.1.38', 22625)
content = []
counter = 0
firstspec = 1
App = Ursina()
gamemode = ""
respawn = (0,0,0)
dead = 0
Id = 0
x,y = 0,0
pos_list = []
intplayersingame = 0
otherplayers = []
delindexes = []
realclients = []
view = 0
clients = 1+len(realclients)
lastplayersingame = 0
Sky(texture="skyv4.png")
deadlobby = Entity(model = "waitlobby",scale = (1,1,1), shader=basic_lighting_shader,color = color.white,texture_scale=(10,10),position = (100,0,100), collider="mesh")
deadlobby.visible = False
#player = Player("box", (0, 10, 0), "mesh", controls="wasd")
coin = Entity(model = "coin.obj",texture = "coin.png", scale = 1, shader=basic_lighting_shader,color = color.white,texture_scale=(10,10), collider="box")
coin.visible = False
coin.x = 100000
coin.y = 5
coin.z = 100000
#player.disable()
playersingame= Text(text="Player in game:", wordwrap=30,scale=1.3,x=.57,y=.45)
#playertest = Entity(model = "person.obj",position=(0,0), color=color.white)
deadclients = 0
islobby= []
lobby = Entity(model = "waitlobby",scale = (1,1,1), shader=basic_lighting_shader,color = color.white,texture_scale=(10,10),position=(100,0,100), collider="mesh")
islobby.append(lobby)
turnpin = None
hatcher = None
player=None
createid = 0
score= Text(text="Score", wordwrap=30,scale=1.3,x=-.57,y=.45)
spectatormode = False

playerobj = Entity(model = "person.obj", shader=basic_lighting_shader,color = color.green,collider='mesh')
playerobj.visible = True
playerobj.enabled = False
score = 0
@client.event
def onConnectionEtablished():
    print('Client successfully connected!')

init = 0
@client.event
def onConnectionError(Reason):
    print('Client failed to connect, the reason is : '+Reason)
@client.event
def coinpos(Content):
    coin.visible = True
    coin.position = Content
    coin.y = 5
    coin.collider = "box"
    print(Content)
    #print("test")
@client.event
def ID(Content):
    global Id,createid
    print(Content)
    Id = int(Content[0])
    createid = int(Content[1])
    print(Id)
@client.event
def mapname(Content):
    global islobby,gamemode,lobby,init,turnpin,hatchet,player,respawn
    print("test")
    gamemode = Content
    if Content == "race":
        if len(islobby) > 0:
            
            destroy(lobby)
            islobby.clear()
            ground = Entity(model = "parkour.obj",texture = "tex.png", scale = .7, shader=basic_lighting_shader,color = color.white,texture_scale=(10,10), collider="mesh")
            turnpin = Entity(model = "treetest.obj",scale = (1,1,1),texture = None, shader=basic_lighting_shader,color = color.white,texture_scale=(10,10), collider="mesh")
            turnpin.visible = True
            turnpin.y -= 0.5
            turnpin.z += 20
            turnpin.x += 0.5
            hatchet = Entity(model = "hatchet",scale = (1,1,1),texture = "pin.png", shader=basic_lighting_shader,color = color.white,texture_scale=(10,10), collider="mesh")
            hatchet.y += 5
            hatchet.z += 11
            player = Player("box", (0, 3, 0), "mesh", controls="wasd")
            normalSpeed= 1
            normalJump = .25
            player.SPEED = normalSpeed
            player.jump_height = normalJump
            respawn = (0,20,0)
            init = 1
            
    if Content == "hatchet":
        if len(islobby) > 0:
            player = Player("box", (313, 10, 0), "mesh", controls="wasd")
            destroy(lobby)
            islobby.clear()
            ground = Entity(model = "hatchetground.obj",texture = "tex.png", scale = 1, shader=basic_lighting_shader,color = color.white,texture_scale=(10,10), collider="mesh")
            turnpin = Entity(model = "turnpinlarge",scale = (1,1,1),texture = "pin.png", shader=basic_lighting_shader,color = color.white,texture_scale=(10,10), collider="mesh")
            turnpin.visible = True
            turnpin.y = 2
            turnpin.z = 0
            turnpin.x= 0
            normalSpeed= 1
            normalJump = .25
            respawn = None
            player.SPEED = normalSpeed
            player.jump_height = normalJump
            init = 1
@client.event
def xandyotherplayers(Content):
    global createid,respawn,playersingame,realclients,deadclients,content,Id, playersingame,lastplayersingame,pos_list,other_players,counter
    #pos_list = Content.pop(Id)
    
    #print(len(pos_list))
    
    intplayersingame = len(Content)-1
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
        otherplayer = Entity(model = "person.obj", color = color.white, texture = "white_cube", texture_scale=(10,2),collider=None)
        otherplayers.append(otherplayer)
    if len(realclients) > 0:
        for client in realclients:
            #print(len(realclients))
            otherplayers[counter].position = (client)
            counter +=1

        counter = 0


def update():

    global x,coin,y,dead,score,score,Id,gamemode,firstspec,spectatormode,player,playerobj,clients,ground,turnpin,hatchet,lobby,init
    #print(player.x)
    print(init)
    coin.rotation_y -= 100 * time.dt
    coin.rotation_x = 90
    if player != None:
        if player.intersects(coin).hit:
            coin.collider = None
            coin.visible = False
            client.send_message("catch",Id)
            score += 1
            print("catched coin!")
    try:
        if gamemode == "race":
            turnpin.rotation_y -= 100 * time.dt
        else:
            turnpin.rotation_y -= 60 * time.dt
        
    except Exception as exception:
        print(exception)
    try:
        hatchet.rotation_z += 100 * time.dt
    except:
        pass
   
    if clients >1:
        try:
            ground.visible = True
            
            lobby.visible = False
            
            hatchet.visible = True
            turnpin.visible = True
        except:
            pass
        
    else:
        try:
            ground.visible = True
            
            
            lobby.visible = False
            hatchet.visible = False
            turnpin.visible = False
        except:
            pass
    try:
        if player.intersects(turnpin).hit:
            if gamemode == "race":
                player.position = (0,5,0)
                player.rotation = (0, 0, 0)
            if gamemode == "hatchet":
                dead = 1
            
            #print("sus")
    except Exception as exception:
        print(exception)
    try:
        if player.intersects(hatchet).hit:
            if gamemode == "race":
                player.position = (0,5,0)
                player.rotation = (0, 0, 0)
            if gamemode == "hatchet":
                dead = 1
    except:
        pass
    
    
    
    playersingame.text = "Players in game :" + str(clients)
    if player != None:
        if spectatormode == False:
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
    if player != None:
        if spectatormode == False:
            if player.y <= -20:
                if gamemode == "race":
                    player.position = (0,5,0)
                    player.rotation = (0, 0, 0)
                if gamemode == "hatchet":
                    dead = 1
    if dead == 1:
        #player.position = (100, 3, 100)
        #player.rotation = (0, 0, 0)
        if player != None:
            if respawn != None:
                if spectatormode == False:
                    player.position = respawn
                    player.rotation = (0, 0, 0)
                    if score >= 5:
                        score -= 5
                    else:
                        score = 0
            else:
                client.send_message("eliminated",Id)
                spectatormode  =True
    if gamemode == "hatchet":
        pass
    if spectatormode == True:
        if gamemode == "hatchet":
            if firstspec == 1:
                firstspec = 0
                
                #spectator= Text(text="You are dead, you will respawn soon", wordwrap=30,scale=1.3,x=0,y=0)
                
                spectatormode = False
                firstspec = 1
                dead = 0
                player.position = (13,5,0)
                #spectator = FirstPersonController(origin_x=10,origin_z=50,origin_y=50,speed = 6,gravity=0,   mouse_sensivity=Vec2(40,40),jump_height=2,collider = 'box')
        
def input(keys):
    global view,playerobj
    if keys == 't':
        view = -view
        if view == 1:
            camera.z = 0
            playerobj.visible = False
        else:
            playerobj.visible = True
            camera.z = -8


App.run()

