def fget():
    for j in range (0, 7):
        fruit = tt[j].split(' ')
        #print "%s", paramaters[j]
        for i in range (0, 9):
            #print " %s.", fruit
            tt1[i] [j-1]= fruit[i-1]
            #print "dhjkshfskdljo"
            #print "%d, %d", i, j
            print tt1[i-1][j-1]

    return

def datalength (n):
    if n > 0:
        digits = int(numpy.log2(n))+1
        print digits
    return digits