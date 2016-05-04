from numpy.random import randint
import numpy as np

packets_number = 10  
node_number = 30
total_time = 35
size = 127


def packets():
    return np.transpose(np.array([randint(node_number, size=packets_number), randint(node_number, size=packets_number), randint(total_time, size=packets_number), [size]*packets_number]))

if __name__ == "__main__":
    np.savetxt('packets.txt', packets(), fmt='%i')