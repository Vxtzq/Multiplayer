from ursinanetworking import *
from ursina import *


server = UrsinaNetworkingServer('192.168.1.38',22625)
mapname = ["race","hatchet"]
App = Ursina()
x,y,z = 0,0,0

mapname = random.choice(mapname)
print(mapname)
clientplayers = []
nb_clients = 0
ground = Entity(model='ground.obj', scale=(10,1,10), color=color.white, texture='white_cube',texture_scale=(10,10)) 
#soil.rotation_z = 90
clients_pos = []
ec = EditorCamera(rotation_smoothing=10, enabled=1, rotation=(30,30,0))
ID = 0
last_id = 0
rotation_info = Text(position=window.top_left)
coinpos = (0,0,0)
catch = 1
def update():
    rotation_info.text = str(int(ec.rotation_y)) + '\n' + str(int(ec.rotation_x))

@server.event
def onClientConnected(Client):
    global nb_clients,ID,last_id
    print(f'{Client} joined the game!')
    Client.send_message("ID", last_id)
    
    clientplayers.append(Entity(model="person.obj", position=(0,5,0), color=color.red,collider='sphere'))
    nb_clients += 1
    last_id += 1
    clients_pos.append((0,0,0))
    Client.send_message("mapname",mapname)
    
'''
@server.event
def onClientDisconnected(Client):
    global nb_clients
    ID = str(Client)
    ID = ID.replace("Client ", "")
    ID = int(ID)
    destroy(clientplayers[ID])
    clients_pos.pop(clientplayers[ID])
    print("Client"+ str(ID) + "left the game" )
    
    nb_clients -=1
   '''
@server.event
def catch(Client, Content):
    global catch
    ID = str(Client)
    ID = ID.replace("Client ", "")
    ID = int(ID)
    catch = 1
@server.event
def clientdisconnect(Client, Content):
    global nb_clients,last_id
    ID = str(Client)
    ID = ID.replace("Client ", "")
    ID = int(ID)
    del clients_pos[0]
    destroy(clientplayers[ID])
    print("Client"+ str(ID) + "left the game" )
    
    nb_clients -=1
    last_id-=1
def clienteliminated(Client, Content):
    ID = str(Client)
    ID = ID.replace("Client ", "")
    ID = int(ID)
    print("Client"+ str(ID) + "died" )
@server.event
def xycoords(Client, Content):
    global x,y,z, last_id,clients_pos,clientplayers,coinpos
    #print(f"{Client} says : {Content}")
    x = Content[0]
    y = Content[1]
    z = Content[2]
    clientname = str(Client)
    clientid = str(Client)
    clientid = clientid.replace("Client " ,"")
    #clientplayers[int(clientid)].position = (x,y,z)
    try:
        clients_pos[int(clientid)] = (x,y,z)
    except:
        clients_pos[0] = (x,y,z)
    
    
    #print(Content[3])
    #print(clients_pos)
    Client.send_message("xandyotherplayers",clients_pos)
    if mapname == "hatchet":
        Client.send_message("coinpos",coinpos)
    
    
    
    
    
    


def update():
    global coinpos,catch
    #print(last_id)
    #test = Entity(model="person.obj", position=(0,0), color=color.red)
    server.process_net_events()
    if catch == 1:
        coinpos = (random.randint(-10,10),0,random.randint(-10,10))
        catch = 0
    
        
    
       
          
App.run()


