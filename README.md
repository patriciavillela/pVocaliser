Python program to create vocalises MIDI files for vocal study.

###The use

```shell
$ python vocaliser.py
Enter the first note in sequence:
C3
Enter the last note in sequence:
D3
Enter the first progression int the following format:
note/duration note/duration ...
C3/1 E3/1 G3/1 E3/1 C3/1
Enter file name:
test.mid
$
```

The notes are symbolized by the tone and the octave. C3 represents the middle C, and C4 represents the next C in the keyboard.

Now you can execute the program with a configuration file. The file needs to have this format:

<firstnote>,<lastnote>,<prograssion>,<filename>

Execute like this;

python vocalizer.py configurationfile

###Dependencies

To this day, I haven't figured out yet how to automate dependencies in Python. I'm openning an issue to fix this.

#####MIDIUtil
MIDIUtil is a pure Python library that allows one to write multi-track Musical Instrument Digital Interface (MIDI) files from within Python programs. (...)
(excerpt taken from MIDIUtil's home page, [https://code.google.com/p/midiutil/](https://www.google.com "MIDIUtil's Homepage"))

To use it, you need only to download the tarball or ZIP file of the 0.89 version (not tested against others) and run **python setup.py install** (might need root access)

Then you're good to go!! Have fun!!


Any questions, you can email me at patrickvob@gmail.com

