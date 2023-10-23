from btSendSignal import send,client_sock
from inference import detect

coordinates=detect()

def receiveSignal():
    signal=''
    while signal=='':  
        signal = client_sock.recv(1024)
        
    return signal

while True:
    if(len(coordinates)==0):
        send(f'exit.0')
        break
    
    send(f'{coordinates[0]}.{coordinates[1]}')
    
    
    signal = receiveSignal()
        
    print('--------------')
    
    if signal.decode('utf-8') == 'check_qr':
        print(signal.decode('utf-8'))
        #--- if not found
        #for now lets check flip only
        # send('rotate')
        send('flip')
        #--- if found
        # send('found')
        
    signal= receiveSignal()

    
    if signal.decode('utf-8') == 'detect':
        coordinates=detect()
        print("reached here")
        
    break