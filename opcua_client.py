# encoding=utf-8
#ref: https://blog.csdn.net/weixin_29482793/article/details/80537862

import sys,time
sys.path.insert(0, "..")
from opcua import Client

if __name__ == "__main__":



    client = Client("opc.tcp://localhost:80/MES OPC UA Data Provider/東莞二廠/")
    # client = Client("opc.tcp://localhost:4840/freeopcua/server/")    
    #client = Client("opc.tcp://127.0.0.1:4840/freeopcua/server/")
    #client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
    try:
        res = client.connect()

        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        root = client.get_root_node()
        print("Objects node is: ", root)

        # Node objects have methods to read and write node attributes as well as browse or populate address space
        print("Children of root are: ", root.get_children()) #Object

        # get a specific node knowing its node id
        #var = client.get_node(ua.NodeId(1002, 2))
        #var = client.get_node("ns=3;i=2002")
        #print(var)
        #var.get_data_value() # get value of node as a DataValue object
        #var.get_value() # get value of node as a python builtin
        #var.set_value(ua.Variant([23], ua.VariantType.Int64)) #set node value using explicit data type
        #var.set_value(3.9) # set node value using implicit data type

        # Now getting a variable node using its browse path
        while(1):
            # myvar = root.get_child(["0:Objects", "2:MyObject", "2:MyVariable"])
            # obj = root.get_child(["0:Objects", "2:MyObject"])
            # print("myvar is: ", myvar)
            # print("myobj is: ", obj)
            
            # # Stacked myvar access
            # print("myvar is: ", root.get_children()[0].get_children()[1].get_variables()[0].get_value())
            # time.sleep(2)



    finally:
        client.disconnect()
