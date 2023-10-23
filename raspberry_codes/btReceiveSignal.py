import bluetooth
from connections import Connection

obj=Connection()
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 1  # You can choose any available port

server_sock.bind(("", port))
server_sock.listen(1)

print("Waiting for a connection...")

client_sock, client_info = server_sock.accept()
print(f"Accepted connection from {client_info}")

try:
    while True:
        data = client_sock.recv(1024)
        if not data:
            break
        
        if data.decode('utf-8').split(sep='.')[0] == "exit":
            print("exiting")
            
        x , y = data.decode('utf-8').split(sep='.')[0] , data.decode('utf-8').split(sep='.')[1]
        
        print("moving x",data.decode('utf-8').split(sep='.')[0])
        # obj.moveX(1,x)

        print("moving y",data.decode('utf-8').split(sep='.')[1])
        # obj.moveY(1,y)
        
        # fetch z-axis 
        z=obj.distance()
        # open valve
        obj.valve(1)
        # obj.moveZ(1,z)
        
        tempZ=z
        while tempZ >= 4 :
            tempZ=obj.distance()
        
        #go back to initial height (top height)
        # obj.moveZ(0,z)
        
        #suppose table center = 255,255
        #reach table center
        # obj.moveX(1,255-x)
        # obj.moveY(1,255-y)
        
        # check qr
        # close valve
        obj.valve(0)
        
        # reach 0,0
        # obj.moveX(0,255)
        # obj.moveY(0,255)
        
        client_sock.send('detect')
        
        
except KeyboardInterrupt:
    obj.exitGPIO()

print("Closing connection...")
client_sock.close()
server_sock.close()
