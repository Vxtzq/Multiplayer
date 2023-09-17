from ursinanetworking import *



server = UrsinaNetworkingServer('192.168.1.23',22625)

x,y,z = 0,0,0

clientplayers = []
nb_clients = 0
#ground = Entity(model='ground.obj', scale=(10,1,10), color=color.white, texture='white_cube',texture_scale=(10,10)) 
#soil.rotation_z = 90
clients_pos = []

ID = 0
last_id = 0
createid = 0


@server.event
def onClientConnected(Client):
    global nb_clients,ID,last_id,createid
    print(f'{Client} joined the game!')
    Client.send_message("ID", (last_id,createid))
    
    #clientplayers.append(Entity(model="person.obj", position=(0,5,0), color=color.red,collider='sphere'))
    nb_clients += 1
    
    clients_pos.append((0,0,0))
    last_id = len(clients_pos)
    
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
def clientdisconnect(Client, Content):
    global nb_clients,last_id,createid
    ID = str(Client)
    ID = ID.replace("Client ", "")
    ID = int(ID)
    clients_pos[Content] = 1
    #destroy(clientplayers[ID])
    print("Client"+ str(ID) + "left the game" )
    createid -=1
    nb_clients -=1
    
    
@server.event
def xycoords(Client, Content):
    global x,y,z, last_id,clients_pos,clientplayers
    #print(f"{Client} says : {Content}")
    x = Content[0]
    y = Content[1]
    z = Content[2]
    clientname = str(Client)
    clientid = str(Client)
    clientid = clientid.replace("Client " ,"")
    #clientplayers[int(clientid)].position = (x,y,z)
    print(clients_pos)
    try:
        if clients_pos[Content[3]] != 1:
            clients_pos[Content[3]] = (x,y,z)
    except:
        pass
    
    
    #print(Content[3])
    #print(clients_pos)
    Client.send_message("xandyotherplayers",clients_pos)
    
    
    
    
    


while True:
    server.process_net_events()
    
    



