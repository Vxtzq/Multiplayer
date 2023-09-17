from ursinanetworking import *
from ursina.prefabs.first_person_controller import FirstPersonController

client = UrsinaNetworkingClient('145.239.199.14', 22625)

App = Ursina()
x,y = 0,0
ground = Entity(model = "cube", scale = (10,1,10), color = color.white, texture = "white_cube", texture_scale=(100,100), collider="box")
player = FirstPersonController(origin_y=5, mouse_sensivity=Vec2(40,40))
clientid = 0

@client.event
def onConnectionEtablished():
    print('Client successfully connected!')


@client.event
def onConnectionError(Reason):
    print('Client failed to connect, the reason is : '+Reason)
@client.event
def ID(Content):
    clientid = int(Content)

def update():
    global x,y
    client.send_message("xycoords",(player.x,player.z, (player.y,clientid)))

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
        #client.send_message("clientdisconnect","byee! :D")
        quit()


App.run()
