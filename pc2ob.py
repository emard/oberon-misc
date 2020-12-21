#!/usr/bin/env python3
# send file from PC to oberon (middle click on PCLink1.Run)
# ./pc2ob.py File.Mod /dev/ttyUSB0

import sys, serial
filename=sys.argv[1]
pclink1=serial.Serial(sys.argv[2], 19200, timeout=1)
f=open(filename,"rb")
f.seek(0,2) # end
length=f.tell() # file length
f.seek(0) # rewind
header=bytearray([0x21])+filename.encode()+bytearray([0])
response=bytearray(1)
pclink1.write(header)
pclink1.readinto(response)
if response[0]==16:
  print("uploading",filename)
  total=0
  while total<length:
    buf=f.read(255)
    pclink1.write(bytearray([len(buf)]))
    pclink1.write(buf)
    pclink1.readinto(response)
    total+=len(buf)
    if response[0]==16:
      print("%9d" % total,end="\r")
      sys.stdout.flush() # make "." appear immediately
    else:
      print("")
      print("blk",len(buf),"error")
      break
    if len(buf)<255:
      break
  print("")
  print("upload done")
else:
  print("hdr error")
