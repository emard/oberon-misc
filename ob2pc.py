#!/usr/bin/env python3
# send file from PC to oberon (middle click on PCLink1.Run)
# ./pc2ob.py File.Mod /dev/ttyUSB0

import sys, serial
filename=sys.argv[2]
pclink1=serial.Serial(sys.argv[1], 19200, timeout=1)
header=bytearray([0x22])+filename.encode()+bytearray([0])
response=bytearray(1)
pclink1.write(header)
pclink1.readinto(response)
if response[0]==0x10:
  print("downloading",filename)
  f=open(filename,"wb")
  total=0
  while True:
    pclink1.readinto(response)
    length=response[0]
    buf=pclink1.read(length)
    f.write(buf)
    pclink1.write(bytearray([0x10]))
    total+=length
    print("%9d" % total,end="\r")
    if length<255:
      break
  f.close()
  print("")
  print("download ok")
else:
  print("hdr error")
