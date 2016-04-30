#!/usr/bin/env python

from SimComponents import PacketGenerator, PacketSink, FlowDemux, SnoopSplitter, \
    WFQServer, VirtualClockServer
import random
import simpy


def const_arrival():
    return 1
def data_generator():
    return random.random()

def const_size():
    return 123*8


if __name__ == '__main__':

    env = simpy.Environment()
    pg = PacketGenerator(env, "SJSU", const_arrival, const_size, data_generator, initial_delay=0.0, finish=35, flow_id=0)
    pg.run()
