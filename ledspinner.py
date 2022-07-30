#!/usr/local/bin/python3

from utime import sleep
from urandom import randrange
import machine, neopixel
np = neopixel.NeoPixel(machine.Pin(5), 24)

#color change interval
cint=5
cmin=0
cmax=128
maxpos = 12
stime=.05
owheelpos = 1
iwheelpos = 1
#outer ring color settings
ocr=cmin
ocg=cmin
ocb=cmax
#inner ring color settings
icr=cmax
icg=cmin
icb=cmin

def newcolor(mycolor):
    #function to allow color changes, called for each color
    mynewcolor=mycolor+randrange(-cint,cint)
    if (mynewcolor>cmax):
        mynewcolor=mynewcolor-(cmax-cmin)
    if (mynewcolor<cmin):
        mynewcolor=mynewcolor+(cmax-cmin)
    print("Incoming color: ", mycolor, " Outgoing: ", mynewcolor)
    return (mynewcolor)

# wheel definitions for 8x8 rgb matrix
owheel = [19,11,14,28,23,39,46,54,51,43,34,18]
iwheel = [28,20,21,29,30,38,37,45,44,36,35,27]
#iwheel = [19,20,21,22,30,38,46,45,44,43,35,27]

print("O: ", owheelpos, " I: ", iwheelpos)
np[owheel[owheelpos-1]-1]=(ocr,ocg,ocb)
np[iwheel[iwheelpos-1]-1]=(icr,icg,icb)
np.write()

while True:
  np[owheel[owheelpos-1]-1]=(ocr,ocg,ocb)
  np[iwheel[iwheelpos-1]-1]=(icr,icg,icb)
  np.write()
  x=int(randrange(-10,10))
  y=int(randrange(-10,10))
  newouter=0
  newinner=0
  stime=randrange(5,20)/100
  for count in range(max(abs(x),abs(y))):
    if x:
      xinc = int(x/abs(x))
      newouter=owheelpos+xinc
      x=x-xinc
      if (newouter>maxpos):
        newouter=1
      if (newouter<1):
        newouter=maxpos
    if y:
      yinc = int(y/abs(y))
      newinner=iwheelpos+yinc
      y=y-yinc
      if (newinner>maxpos):
        newinner=1
      if (newinner<1):
        newinner=maxpos
#    print("o: ", owheelpos, " i: ", iwheelpos)
    sleep(stime)
    ocr=newcolor(ocr)
    ocg=newcolor(ocg)
    ocb=newcolor(ocb)
    icr=newcolor(ocr)
    icg=newcolor(ocg)
    icb=newcolor(ocb)
    oold=owheel[owheelpos-1]-1
    iold=iwheel[iwheelpos-1]-1
#    np[owheel[owheelpos-1]-1]=(0,0,0)
#    np[iwheel[iwheelpos-1]-1]=(0,0,0)
    print ("New Outer: ",newouter, " New Inner: ", newinner)
    owheelpos=newouter
    iwheelpos=newinner
    onum=owheel[owheelpos-1]-1
    inum=iwheel[iwheelpos-1]-1
    print("Onum: ", onum, " Inum: ", inum)
    np[onum]=(ocr,ocg,ocg)
    np[inum]=(icr,icg,icb)
    np[oold]=(0,0,0)
    np[iold]=(0,0,0)
    np.write()
  print("-----")
#  sleep(.4)
