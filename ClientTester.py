import zmq
import json


context = zmq.Context()

Case1 = {
    "REQ_CURR": ["USD"],
    "SORT": "",
    "NOW_CURR": "USD",
    "AMOUNT": 100.00
    }

# SORT TEST CASES:
# TEST CASE: "SORT BASED ON VALUES RETURNED"
Case2 = {
    "REQ_CURR": ["EUR", "CAD", "AUD", "CHF", "JPY"],
    "SORT": "VALUE",
    "NOW_CURR": "USD",
    "AMOUNT": 100.00
    }

# TEST CASE: "NO SORT SPECIFIED"
Case3 = {
    "REQ_CURR": ["EUR", "CAD", "AUD", "CHF", "JPY"],
    "SORT": "",
    "NOW_CURR": "USD",
    "AMOUNT": 100.00
    }

# TEST CASE: "SORT BASED ON CURR NAME"
Case4 = {
    "REQ_CURR": ["EUR", "CAD", "AUD", "CHF", "JPY"],
    "SORT": "CURR",
    "NOW_CURR": "USD",
    "AMOUNT": 100.00
    }

# TEST CASE: "GARBAGE"
Case5 = {
    "REQ_CURR": ["EUsR", "CAD", "AUD", "CHF", "JPY"],
    "SORT": "CURR",
    "NOW_CURR": "USD",
    "AMOUNT": 100.00
    }


Tests= [Case1, Case2, Case3, Case4, Case5]




print("Starting Client Test:")

for case in Tests:
    sendDict = dict(case)
    print("TEST CASE: ", sendDict)
    #CONNECT TO MICROSERVICE:
    print("Connecting Currency Server")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    #SEND JSON OBJECT:
    dataJSON = json.dumps(sendDict,ensure_ascii=False)
    socket.send_json(dataJSON)
    #RECIEVE DATA:
    returnData = socket.recv_json()
    print("Received reply [ %s ]" % (returnData))
    #CLOSE SOCKET
    socket.close()
    print()
print("COMPLETED CLIENT CASES")