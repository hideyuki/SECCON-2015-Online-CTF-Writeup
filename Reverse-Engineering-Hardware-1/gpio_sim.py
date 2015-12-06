#!/usr/bin/python

d1 = 0
d2 = 0
d3 = 0
d4 = 0

l1 = 0
l2 = 0
l3 = 0
l4 = 0
l5 = 0
l6 = 0
l7 = 0

da = 0
db = 0

ic1q = 0
ic2q = 0

def encoder():
    v = 0
    v = ic1q
    v = 2*v + ic2q
    v = 2*v + int(not(l1))
    v = 2*v + int(not(l2))
    v = 2*v + int(not(l3))
    v = 2*v + int(not(l7))
    return v

def update_top_led():
  global l1, l2, l3, l4, l5, l6, l7
  l1 = da or not(ic2q)
  l2 = not(l1) or not(ic1q)
  l3 = db or ic2q
  l4 = not(ic1q) or not(ic2q)
  l5 = not(ic1q) or not(l4)
  l6 = not(ic2q) or not(l4)
  l7 = not(l5) or not(l6)

def update_bottom_led():
  global d1, d2, d3, d4
  d1 = da
  d2 = ic1q
  d3 = db
  d4 = ic1q

def update_ff():
  global ic1q, ic2q
  ic1q = da
  ic2q = db

c = '@'
flag = ""

try:
    update_bottom_led()
    update_top_led()

    for i in range(10) :
        if c == 'Y' :
            da = 0
            db = 1
        else:
            if (i & 1) == 0 :
                da = 0
            else :
                da = 1
            if (i & 2) == 0 :
                db = 0
            else :
                db = 1

        update_bottom_led()
        update_top_led()

        #time.sleep(0.1)

        c = chr(encoder()+32)
        flag = flag + c

        update_ff()

        update_bottom_led()
        update_top_led()

        #time.sleep(0.1)
        flag = flag + chr(encoder()+32)

except KeyboardInterrupt:
    print("stop\n")

print "The flag is SECCON{"+flag+"}"

