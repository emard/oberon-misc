# Oberon misc tools and examples

# PCLink1 file transfer

This is small python example for linux which
uploads files to oberon using PCLink1 protocol via
serial port at 19200 baud.

Here is example source: a tetris game by Ralf Denger, adapted by jr.

Oberon can work with CRLF or CR line ending. Here are shell scripts
to convert between unix LF line ending and oberon CR line ending:

    cd tetris
    ../txt2ob.sh File.Mod.txt File.Mod

On oberon, middle click to "PCLink1.Run" to start file transfer service.
Some LEDs should turn ON during upload and text printed "receiving ObTris.Mod done"

    ../pc2ob.py ObTris.Mod /dev/ttyUSB0
    uploading ObTris.Mod
    upload ok

On oberon, check files by typing this and middle clicking to
"System.Directory":

    System.Directory *.Mod

We can also download it back to PC

    ../ob2pc.py /dev/ttyUSB0 ObTris.Mod
    downloading ObTris.Mod
    download ok

To compile uploaded sources, on oberon command window 
type this and then middle click "System.Free" then "ORP.Compile".
System.Free unloads from memory previous version if it exists.
Ending with tilde "~" terminates the command otherwise it would
proceed with next line.

    System.Free ObTris ~
    ORP.Compile ObTris.Mod/s ~

Errors? To edit a file, right-select file name
and middle-click at "Edit.Open". To locate reporeted
compiler error

    1) left-click in the source file to set the cursor somewhere
    2) right-select the pos line of the compiler error
    3) middle-click on Edit.Locate

Start Tetris with typing and middle cliking on:

    ObTris.Open

Then middle click to "ObTris.Start"
Commands:

    J - Left
    K - Right
    I - Rotate
    H - Drop
