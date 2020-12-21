files=ObTris.Mod RandomNumbers.Mod

all: $(files)

ObTris.Mod: ObTris.Mod.txt
	../txt2ob.sh $< $@

RandomNumbers.Mod: RandomNumbers.Mod.txt
	../txt2ob.sh $< $@

upload: $(files)
	../pc2ob.py RandomNumbers.Mod /dev/ttyUSB0
	../pc2ob.py ObTris.Mod /dev/ttyUSB0

clean:
	rm -f *.Mod *~
