# Oberon PCLink1 python tools

This is small python example for linux which
uploads files to oberon using PCLink1 protocol via
serial port at 19200 baud.

Here is example source: a tetris game by Ralf Denger, adapted by jr.

Oberon needs source files with CR line ending, here's shell script
that does the conversion:

    ./convert.sh oberon_tetris/RandomNumbers.Mod.txt oberon_tetris/RandomNumbers.Mod
    ./convert.sh oberon_tetris/ObTris.Mod.txt oberon_tetris/ObTris.Mod

On oberon, middle click to "PCLink1.Run" to start file transfer service.
On PC, when uploading dots will be printed for each 255 byte block
and on oberon LEDs should turn ON during upload and finally some text
printed "uploading filename done"

    ./pc2ob.sh oberon_tetris/RandomNumbers.Mod /dev/ttyUSB0
    ./pc2ob.sh oberon_tetris/ObTris.Mod /dev/ttyUSB0

On oberon, check are files there by typing this and middle clicking to
"System.Directory":

    System.Directory *.Mod

Let's compile upload sources. 
On oberon commaand window, type this and then middle click "ORP.Compile"

    ORP.Compile RandomNumbers.Mod/s
    ORP.Compile ObTris.Mod/s

Start Tetris with typing and middle clinking on:

    ObTris.Open

