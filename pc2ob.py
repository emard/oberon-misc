#!/usr/bin/env python3
# send file from PC to oberon (middle click on PCLink1.Run)

import sys, serial
filename=sys.argv[1]
pclink1=serial.Serial("/dev/ttyUSB0", 19200, timeout=1)
f=open(filename,"rb")
f.seek(0,2) # end
remain=f.tell() # file length
f.seek(0) # rewind
header=bytearray([0x21])+filename.encode()+bytearray([0])
response=bytearray(1)
buf=bytearray(255)
pclink1.write(header)
pclink1.readinto(response)
if response[0]==16:
  print("hdr ok")
while remain>255:
  f.readinto(buf)
  pclink1.write(bytearray([255]))
  pclink1.write(buf)
  pclink1.readinto(response)
  if response[0]==16:
    print("blk 255 ok")
  remain-=255
if remain>0:
  buf=f.read()
  pclink1.write(bytearray(remain))
  pclink1.write(buf)
  pclink1.readinto(response)
  if response[0]==16:
    print("blk",remain,"ok")
