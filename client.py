from ursinanetworking import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader



client = UrsinaNetworkingClient('192.168.1.23', 22625)
content = []
counter = 0
App = Ursina()

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
ground = Entity(model = "parkour.obj",texture = "tex.png", scale = .7, shader=basic_lighting_shader,color = color.white,texture_scale=(10,10), collider="mesh")
ground.visible = True
player = FirstPersonController(origin_x=0,origin_z=0,origin_y=5,speed = 6,gravity=0.7 ,   mouse_sensivity=Vec2(40,40),jump_height=2,collider = 'person.obj')
playersingame= Text(text="Player in game:", wordwrap=30,scale=1.3,x=.57,y=.45)
#playertest = Entity(model = "person.obj",position=(0,0), color=color.white)
deadclients = 0
lobby = Entity(model = "waitlobby",scale = (1,1,1), shader=basic_lighting_shader,color = color.white,texture_scale=(10,10), collider="mesh")
turnpin = Entity(model = "turn",scale = (1,1,1),texture = "pin.png", shader=basic_lighting_shader,color = color.white,texture_scale=(10,10), collider="box")
turnpin.visible = True
turnpin.y -= 0.5
turnpin.z += 20
turnpin.x += 0.5
createid = 0

playerobj = Entity(model = "person.obj", shader=basic_lighting_shader,color = color.green,collider='mesh')
playerobj.visible = True
camera.z = -8
player.y = 2
player.x =0
player.z=0
player.gravity = 0.5
player.camera_pivot.rotation_x = 30
player.camera_pivot.rotation_y = -0.0
player.camera_pivot.rotation_z = 0.0
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
    global createid,playersingame,realclients,deadclients,content,Id, playersingame,lastplayersingame,pos_list,other_players,counter
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
        otherplayer = Entity(model = "person.obj", color = color.white, texture = "white_cube", texture_scale=(10,2),collider='person.obj')
        otherplayers.append(otherplayer)
    if len(realclients) > 0:
        for client in realclients:
            #print(len(realclients))
            otherplayers[counter].position = (client)
            counter +=1

        counter = 0


def update():

    global x,y,Id,player,playerobj,clients,ground,lobby
    #print(player.x)
    
    print(player.camera_pivot.rotation_x,player.camera_pivot.rotation_y,player.camera_pivot.rotation_z)
    turnpin.rotation_y += 100 * time.dt
    if clients >1:
        #ground.visible = True
        lobby.visible = False
        pass
    else:
        #ground.visible = False
        lobby.visible = False
        pass
    if turnpin.intersects(player).hit:
        player.y = 1
        player.x =0
        player.z=0
        player.camera_pivot.rotation_x = 30
        player.camera_pivot.rotation_y = -0.0
        player.camera_pivot.rotation_z = 0.0
    
    
    
    playersingame.text = "Players in game :" + str(clients)
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
        player.camera_pivot.rotation_x = 30
        player.camera_pivot.rotation_y = -0.0
        player.camera_pivot.rotation_z = 0.0
        player.y = 1
        player.x =0
        player.z=0
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

