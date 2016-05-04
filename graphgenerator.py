#!/usr/bin/env python

try:
    import matplotlib.pyplot as plt
except:
    raise

import sys
import networkx as nx
import numpy as np
import math
import matplotlib.pyplot as plt
from itertools import islice

from decoder_optimized import *
from encoder import *

time = []
source = []
dst = []
tt1 = np.zeros((7, 9))
paramaters = []
l1 = []
num_packets = 7

overlap = []
path = []
reduced_transmission = []
#temp = 0

path_in_order = {6: 24}
fill_num = 25
G = nx.dense_gnm_random_graph(10, 50)
pos = nx.spring_layout(G)
H = G.number_of_edges()

colors = range(H)
# nx.draw(G,pos,node_color='#A0CBE2',edge_color=colors,width=4,edge_cmap=plt.cm.Reds,with_labels=True)
nx.draw(G, pos, node_color='#A0CBE2', width=0.4, edge_cmap=plt.cm.Reds, with_labels=True)


# plt.savefig("edge_colormap.png", dpi=300) # save as png
# plt.show()

# separate the string and packets.
def copy_source_dst_time(x):
    source_c = []
    dst_c = []
    time_c = []
    # print x[:,0]
    for i in range(0, len(x[:, 0])):
        source_c.append(x[i][1])
        # print source_c[i]
        dst_c.append(x[i][0])
        time_c.append(x[i][2])
    return (source_c, dst_c, time_c)


# pad the packets to take the time into acount.
def padding_packet_info(source_find, dst_find, starttime):
    temp = [0]
    for i in range(0, len(source_find)):
        path = (nx.shortest_path(G, source_find[i], dst_find[i], starttime[i]))
        # sys.exit()
        path.reverse()
        for j in range(0, starttime[i]):
            path.append(-1)

        path.reverse()
        for k in range(0, fill_num - len(path)):
            path.append(-1)
        # print path
        l1.append(path)
    return (fill_num)


# split the string into separate elments for better manipulation.
def split_string(num_pack, fill_number):
    temp = [0]
    split_t = []
    # print l1[0]
    for i in range(0, num_pack):
        # print i
        temp = l1[i]
        # temp.append(l1[i])
        split_t.append([temp[j:j + 1] for j in range(0, len(l1[i]), 1)])
        # print split_t
    return split_t


# count reduce transmission.
def count_reduced_transmission(path_in_order):
    # sys.exit()

    flag = 0
    index2 = 0
    index1 = 0  # at each time unit, see how many different nodes involved
    count = 0  # how many transmission could be reduced for each different node at each time unit.
    elements1 = 0
    elements12 = 0
    temp_equal = []

    for j in range(0, fill_num - 1):
        temp1 = []  # a dictionary shows that what are the different elments at time unit.
        temp2 = []  # a dictionary shows the nodes at each unit for each packet.
        for i in range(0, num_packets - 1):
            #print i
            if path_in_order[i][j] != [-1]:
                temp2.append(path_in_order[i][j])
            else:
                pass
        #print temp2
        for k in range(0, num_packets - 1):
            #print k
            if path_in_order[k][j] != [-1]:
                #print path_in_order[k][j]
                # sys.exit()
                if not temp1:
                    temp1.append(path_in_order[k][j])
                    #print temp1
                    # sys.exit()
                else:
                    length = len(temp2)
                    #print "length alkdjalk;dj"
                    #print length
                    for l in range(0, length - 1):
                        #print "asfkjhsd;glkn"
                        # print temp1
                        #print temp1
                        # sys.exit()
                        if path_in_order[k][j] in temp1:
                            pass
                            # print "temp1 ksfjlajfk"
                            # print temp1
                        else:
                            #print "hfakljfbhlk"
                            temp1.append(path_in_order[k][j])
                            #print temp1
                        # sys.exit()
            else:
                pass
        # print "sjfklhfdjk"
        reduced_transmission.append(len(temp2) - len(temp1))
        #print reduced_transmission

        #return reduced_transmission
        #print "total reduced", reduced


# main function:
'''
with open('test_packets.txt', 'r')as f:
    for line in f:
        if line == '\n':
            continue
        temp = line.split()
        #        num_packets+=1

        temp = [temp[1], temp[3], temp[5], temp[7]]
        temp = map(int, temp)
        # print temp
        paramaters.append(temp)

paramaters = np.array(paramaters)
'''
paramaters = np.loadtxt('packets.txt')

(source, dst, time) = copy_source_dst_time(paramaters)

path_info_len = 0

path_info_len = padding_packet_info(source, dst, time)

path_in_matrix = split_string(6, path_info_len)

count_reduced_transmission(path_in_matrix)

b = sum(reduced_transmission)
print b
#print path_in_matrix[0]
#print path_in_matrix[1]
#print path_in_matrix[2]
#print path_in_matrix[3]
#print path_in_matrix[4]
#print path_in_matrix[5]

# for path in all_pairs_shortest_path(G, tt1[0], tt1[1]):
#	l1= path

# for path in all_pairs_shortest_path(G, tt1[2], tt1[3]):
#	l2= path

# overlap = common_elements(l1, l2)
# print overlap

##give the overlap to the encoder and decoder.
# a = ['H','a']
# b = ['a','c']
# encodedstringreceived = '[[[1.0, 2.0, 234.0], [2.0, 1.0, 306.0], [1.0, 2.0, 331.0]], [[2.0, 1.0, 311.0]]]'
# numpacket  = 2
# encodeddata = []
# encodeddata = get_raw_data(a, b)

# decodedata = []
# decodedata = get_raw_encoded_data(encodedstringreceived, numpacket)






# determine if the node needs to broadcast the packets or not.
# dstde means the decoded destination, if the dstde equals to the node
# flag determines if the packets need to be broadcasted
# recevie means if the packets has been broadcasted or not.

# test commom elements:
common1 = [1, 2, 3, 4]
common2 = [1, 2, 3, 4]
list_common = []
number_reduced = 0


def common_elements(list1, list2):
    return [element for element in list1 if element in list2]


list_common = common_elements(common1, common2)
number_reduced = len(list_common)


def broadcast_or_not(source, dstde, node):
    index = 0
    receive = []
    i = len(dstde)
    j = len(node)
    if i == 1:
        flag = 1  # broadcasting the packets, because we have not reached the destination, it is a intermediate node.
        flag = 0  # stop broadcasting. it is the wrong node.
        if i == j:
            if dstde == node:
                flag = 0  # stop broadcasting the packets. Because we reach the only destination.
                receive[index] = 0  # stop the transmission of current packets, we have reached the destination.
                ++index
            else:
                flag = 0  # stop broadcasting the packets. Because it is not on the path.
                receive[
                    index] = 1  # Even though we stop the transmission, the packet has not been received by the destination.
                ++index


        else:
            if dstde != node:
                for path in all_pairs_shortest_path(G, source, dstde):
                    str.join(path, "")
                    intermediate = re.search(r'dst', path, re.M | re.I)
                    if intermediate == node:  # it is the intermediate node of the path.
                        pass
                    else:
                        pass
            else:
                flag = 1  # broadcasting the packets, even though we have reached the destination, there iare more destination needs to be transmitted.
                receive[
                    index] = 0  # The packet has not been fully received by all the destination, only the index th of packets received the data.
                ++index
    return

# get a array of  sources and destinations. Get all the packets all at once, but there is a packet time need to be considered as the point of view.




# sourc e: array contians a number of packets destination.
# destination: array contains a number of packets desitination.
# node1 is the encoding node.
# nod e2 is the decoding node.They are array as well.


# overlap = common_elements(l1, l2)# you have found the overlap between nodes.
