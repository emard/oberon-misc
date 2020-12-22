# Oberon misc tools and examples

# PCLink1 file transfer

This is small python example for linux which
uploads files to oberon using PCLink1 protocol via
serial port at 19200 baud.

Here is example source: a tetris game by Ralf Denger, adapted by jr.

Oberon needs source files with CR line ending, here's shell script
that does the conversion:

    cd tetris
    ../txt2ob.sh RandomNumbers.Mod.txt RandomNumbers.Mod
    ../txt2ob.sh ObTris.Mod.txt ObTris.Mod

On oberon, middle click to "PCLink1.Run" to start file transfer service.
Some LEDs should turn ON during upload and text printed "receiving ObTris.Mod done"

    ../pc2ob.py RandomNumbers.Mod /dev/ttyUSB0
    uploading RandomNumbers.Mod
    upload ok

    ../pc2ob.py ObTris.Mod /dev/ttyUSB0
    uploading RandomNumbers.Mod
    upload ok

On oberon, check files by typing this and middle clicking to
"System.Directory":

    System.Directory *.Mod

We can also download it back to PC

    ../ob2pc.py /dev/ttyUSB0 ObTris.Mod
    downloading ObTris.Mod
    download ok

To compile uploaded sources, on oberon command window 
type this and then middle click "ORP.Compile"

    ORP.Compile RandomNumbers.Mod/s
    ORP.Compile ObTris.Mod/s

Start Tetris with typing and middle cliking on:

    ObTris.Open

Then middle click to "ObTris.Start"
Commands:

    J - Left
    K - Right
    I - Rotate
    H - Drop
