from ursinanetworking import *
from ursina import *


server = UrsinaNetworkingServer('192.168.1.23',22625)
ID = None
App = Ursina()
x,y,z = 0,0,0
clientxandy = []
clientplayers = []
nb_clients = 0
ground = Entity(model='plane', scale=(100,1,100), color=color.white, texture='white_cube',texture_scale=(100,100), collider='box')
newid=0
#soil.rotation_z = 90
@server.event
def onClientConnected(Client):
    global nb_clients,newid
    print(f'{Client} joined the game!')
    Client.send_message("ID",str(newid))
    newid +=1
    clientxandy.append((0,0))
    clientplayers.append(Entity(model="cube", position=(0,0), color=color.red))
    nb_clients += 1
    print(nb_clients)

@server.event
def onClientDisconnected(Client):
    global nb_clients
    ID = str(Client)
    ID = ID.replace("Client ", "")
    ID = int(ID)
    destroy(clientplayers[ID])
    print("Client"+ str(ID) + "left the game" )

    nb_clients -=1
    newid-=1
    print(nb_clients)
@server.event
def clientdisconnect(Client, Content):
    global nb_clients
    ID = str(Client)
    ID = ID.replace("Client ", "")
    ID = int(ID)
    destroy(clientplayers[ID])
    print("Client"+ str(ID) + "left the game" )
    print("helo")
    nb_clients -=1
    newid-=1
    print(nb_clients)
@server.event
def xycoords(Client, Content):
    global x,y,z
    #print(f"{Client} says : {Content}")
    x = Content[0]
    y = Content[1]
    z = Content[2]
    print(x,y,z)
    
    clientplayers[z[1]].position = (x,y,z[0])





def update_entities(e):
    e.x += 1 * time.dt # dt is short for delta time, the duration since the last frame.



def update():

    server.process_net_events()
    """
    for i in range(nb_clients):
        clientplayers[i].update = update_entities(clientplayers[i])

"""


App.run()


