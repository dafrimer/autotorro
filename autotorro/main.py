import lxml
import transmissionrpc
import sys
import os
import json
from lxml import etree

f = open('./torconfig.json')
conf = json.load(f)
f.close()

#Mon, 01 Aug 2016 02:00:00 +0000
def start_client():
    #try:

    #except:
    #    print("ERROR: there was an error reading the json configuration file")

    tc = transmissionrpc.Client(address=conf.pop('transmission_server'), port=int(conf.pop('transmission_port'), user=conf.pop('transmission_user'), password=conf.pop('transmission_password')

    return tc

class Torro(object):
    def __init__(self):
        self.tc = start_client()
        #You need this for the raw_title
        self.tvNamespace = "http://showrss.info"

    def queryRSSFeed(self):
        pass

    def log_DLqueue(self):
        pass

    def




    d = start_client()

    print d.get_torrents()





etree.parse("")

##

