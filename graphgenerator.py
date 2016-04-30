#!/usr/bin/env python

try:
    import matplotlib.pyplot as plt
except:
    raise


import networkx as nx
import numpy
import math
from decoder_optimized import *
from encoder import *

import matplotlib.pyplot as plt
#G=nx.Graph()
#G.add_nodes_from([0,1,2,3,4,5])
import itertools
from itertools import islice


G= nx.gnp_random_graph(20, 0.5, seed=None, directed=False)


tt1= []
l1 = []
l2 = []
overlap = []
with open('test.txt', 'r')as f:
    txt = f.read()
tt1 = txt.split(' ')


pos=nx.spring_layout(G)
H = G.number_of_edges()

colors=range(H)
#nx.draw(G,pos,node_color='#A0CBE2',edge_color=colors,width=4,edge_cmap=plt.cm.Reds,with_labels=True)
nx.draw(G,pos,node_color='#A0CBE2',width=0.4,edge_cmap=plt.cm.Reds,with_labels=True )
plt.savefig("edge_colormap.png", dpi=300) # save as png
plt.show()


def datalength (n):
    if n > 0:
        digits = int(numpy.log2(n))+1
        print digits
    return digits

def all_pairs_shortest_path(G, source, target, weight=None):
    return list(islice(nx.shortest_simple_paths(G, source, target, weight=None), 1, 2))

def common_elements(list1, list2):
    return [element for element in list1 if element in list2]

#for path in all_pairs_shortest_path(G, tt1[0], tt1[1]):
#	l1= path

#for path in all_pairs_shortest_path(G, tt1[2], tt1[3]):
#	l2= path

#overlap = common_elements(l1, l2)
#print overlap

##give the overlap to the encoder and decoder.
#a = ['H','a']
#b = ['a','c']
#encodedstringreceived = '[[[1.0, 2.0, 234.0], [2.0, 1.0, 306.0], [1.0, 2.0, 331.0]], [[2.0, 1.0, 311.0]]]'
#numpacket  = 2
#encodeddata = []
#encodeddata = get_raw_data(a, b)

#decodedata = []
#decodedata = get_raw_encoded_data(encodedstringreceived, numpacket)



#determine if the node needs to broadcast the packets or not.
#dstde means the decoded destination, if the dstde equals to the node
#flag determines if the packets need to be broadcasted
#recevie means if the packets has been broadcasted or not.
def broadcastor_not(source, dstde, node):
    index=0
    receive=[]
    i = len(dstde)
    j = len(node)
    if i == 1:
        if i == j:
            if dstde == node:
                flag = 0 #stop broadcasting the packets. Because we reach the only destination.
                receive[index] = 0 # stop the transmission of current packets, we have reached the destination.
                ++index
            else:
                flag = 0 #stop broadcasting the packets. Because it is not on the path.
                receive[index] = 1  #Even though we stop the transmission, the packet has not been received by the destination.
                ++index

        else:
            if dstde != node:
                for path in all_pairs_shortest_path(G, source,dstde):
                    str.join(path, "")
                    intermediate= re.search( r'dst', path, re.M|re.I)
                    if intermediate == node: #it is the intermediate node of the path.
                        flag =1 #broadcasting the packets, because we have not reached the destination, it is a intermediate node.
                    else:
                        flag = 0 #stop broadcasting. it is the wrong node.
            else:
                flag =1 #broadcasting the packets, even though we have reached the destination, there iare more destination needs to be transmitted.
                receive[index] = 0 #The packet has not been fully received by all the destination, only the index th of packets received the data.
                ++index


def encode_decode_or_nothing(source, dstde, node):
    i = 0
    tt1 = dstde.split(',')#problematic to split the string.
    for path in all_pairs_shortest_path(G, source, tt1[i]):
        l1= path
    for path in all_pairs_shortest_path(G, source, tt1[i+1]):
        l2= path
overlap = common_elements(l1, l2)# you have found the overlap between nodes.

