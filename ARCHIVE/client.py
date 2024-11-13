import zmq
import pickle
import json 


Case1 = {
    "REQ_CURR":["EUR", "CAD", "AUD", "CHF", "JPY"],
    "SORT":"value",
    "NOW_CURR": "USD",
    "AMOUNT": 1234.56
}

Case2 = {
    "REQ_CURR":["EUR", "CAD", "AUD", "CHF", "JPY"],
    "SORT":"",
    "NOW_CURR": "USD",
    "AMOUNT": 1234.56
}

context = zmq.Context()

#  Socket to talk to server
print("Connecting Currency Server")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
dataJSON = json.dumps(Case2,ensure_ascii=False)
socket.send_json(dataJSON)
# socket.send_pyobj(Case1)

#  Get the reply.
returnData = socket.recv_json()
print("Received reply [ %s ]" % (returnData))


# # SETUP CLIENT SIDE SOCKET
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # SEVER ADDRESS AND PORT:
# HOST = '127.0.0.1'
# PORT = 1000
# # CONNECT TO THE SERVER
# client.connect((HOST, PORT))

# # TRY SENDING THE DATA TO THE SERVER:
# try:
#     # OBJECT TO SEND TO THE SERVER
#     Case1 = {
#         "REQ_CURR":["EUR", "CAD", "AUD", "CHF", "JPY"],
#         "SORT":"value",
#         "NOW_CURR": "USD",
#         "AMOUNT": 1234.56
#     }
#     # SERIALIZE THE OBJECT USING PICKLE
#     serialized = pickle.dumps(Case1)
#     # SEND THE SERIALIZED DATA VIA SOCKET
#     client.sendall(serialized)
#     #GET REPLY FROM SERVER
#     dataStream = b''
#     print('SerVer Connected:')
#     while True:
#         # RECIEVE CHUNK OF STREAM
#         chunk = client.recv(4096)
#         # IF NO DATA IS RETURNED BREAKOUT
#         if not chunk:
#             # IF NO CHUNK IN AVAILABLE BREAK.
#             break
#         # PEICE TOGTHER THE STREAM:
#         dataStream += chunk
#     recievedObject = pickle.loads(dataStream)
#     print(f'Recieved: {recievedObject}')




# finally:
#     client.close();