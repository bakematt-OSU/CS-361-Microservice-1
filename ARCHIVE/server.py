import socket
import pickle
from ARCHIVE.Func import Functions

# SETUP THE SER SOCKET:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SERVER HOST AND BINDING PORT
HOST = '127.0.0.1'
PORT = 4839
# CONFIGURE SERVER TO THE HOST AND PORT
server.bind((HOST, PORT))
# ALLOW THE SERVER TO HAVE ONE CONNECTION AT A TIME.
numberConn = 1
server.listen(numberConn)

while True:
    print('Waiting for connections')
    # ACCEPT CONNECTIONS FROM CLIENTS:
    client, addr = server.accept()
    # TRY AND PROCESS THE CONNECTION:
    try:
        print('Client Connected:')
        # IDENTIFY THE STREAM
        dataStream = b''
        # RECIEVE STREAM AND TRY TO GET THE DATA
        while True:
            # RECIEVE CHUNK OF STREAM
            chunk = client.recv(4096)
            # IF NO DATA IS RETURNED BREAKOUT
            if not chunk:
                # IF NO CHUNK IN AVAILABLE BREAK.
                break
            # PEICE TOGTHER THE STREAM:
            dataStream += chunk
        # ASSMBLE THE RECIVED OBJECT:
        recievedObject = pickle.loads(dataStream)
        # PRINT RECIEVED:
        print(f'Recieved: {recievedObject}')
        ReturnValue = Functions.CurrencyRequest(recievedObject)
        ReturnValue["ADDR"] = addr
        print(ReturnValue)

        # SERIALIZE THE OBJECT USING PICKLE
        serialized = pickle.dumps(ReturnValue)
        # SEND THE SERIALIZED DATA VIA SOCKET
        client.sendall(serialized)
    finally:
        # CLOSE CLIENT AFTER JOB IS COMPLETE
        client.close()
