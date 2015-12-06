#!/usr/bin/python

import time
import sys
import struct
import binascii
import os

rfd = open(sys.argv[1], 'rb')
wfd = open(sys.argv[2], 'wb')
len = os.path.getsize(sys.argv[1]) #int(sys.argv[3])

# q inputs
q0 = 0
q1 = 0
q2 = 0
q3 = 0
q4 = 0
q5 = 0
q6 = 0
q7 = 0


def reset():
    global q0, q1, q2, q3, q4, q5, q6, q7
    q0 = 0
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    q5 = 0
    q6 = 0
    q7 = 0

def get_current_count_a():
    return q2*8 + q1*4 + q0*2 + q7

def get_current_count_b():
    return q6*8 + q5*4 + q4*2 + q3

def count_up():
    global q0, q1, q2, q3, q4, q5, q6, q7
    da = get_current_count_a()
    dan = da + 1
    q7 = 0x01 & dan
    q0 = 0x01 & (dan>>1)
    q1 = 0x01 & (dan>>2)
    q2 = 0x01 & (dan>>3)

    if q7 == 1 and q0 == 1 and q1 == 1 and q2 == 1:
        db = get_current_count_b()
        dbn = db + 1
        q3 = 0x01 & dbn
        q4 = 0x01 & (dbn>>1)
        q5 = 0x01 & (dbn>>2)
        q6 = 0x01 & (dbn>>3)

def init():
    reset()

def setValue(n):
    reset()
    for i in range(n):
        count_up()

def a2v(a):
    return a[7]+2*a[6]+4*a[5]+8*a[4]+16*a[3]+32*a[2]+64*a[1]+128*a[0]

# main
init()

# encrypt/decrypt
for i in range(len):
    value = a2v([q7, q6, q5, q4, q3, q2, q1, q0])
    # file convert 
    v = rfd.read(1)
    d = ''
    d += struct.pack('B', ord(v) ^ value)
    #print "d: " + binascii.b2a_hex(struct.pack('B', ord(v) ^ value)) + "(" + d + "), v: " + v + ", value: " + str(value)
    wfd.write(d)

    setValue(value)
    #time.sleep(0.1)
    count_up()
    count_up()
    count_up()

    #print "q: " + str(q6) + str(q5) + str(q4) + str(q3) + str(q2) + str(q1) + str(q0) + str(q7)

