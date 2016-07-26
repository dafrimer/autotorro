import lxml
import transmissionrpc
import sys
import os
import json
from lxml import etree

f = open('./torconfig.json')
conf = json.load(f)



def start_client():
    #try:

    #except:
    #    print("ERROR: there was an error reading the json configuration file")

    tc = transmissionrpc.Client(address=conf['transmission_server'], port=int(conf['transmission_port']), user=conf['transmission_user'], password=conf['transmission_password'])

    return tc

class

    d = start_client()

    print d.get_torrents()





etree.parse("")

##

