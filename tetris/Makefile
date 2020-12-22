files=ObTris.Mod RandomNumbers.Mod

upload: $(files)
	../pc2ob.py RandomNumbers.Mod /dev/ttyUSB0
	../pc2ob.py ObTris.Mod /dev/ttyUSB0

clean:
	rm -f *.Mod *~
