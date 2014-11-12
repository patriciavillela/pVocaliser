from midiutil.MidiFile import MIDIFile
import sys
blablablabla

time = 0

def noteToPitch(note):
 tone = 0
 octave = 0
 name = note[:-1]
 if name == "C" or name == "B#":
  tone = 0
 if name == "C#" or name == "Db":
  tone = 1
 if name == "D":
  tone = 2
 if name == "D#" or name == "Eb":
  tone = 3
 if name == "E" or name == "Fb":
  tone = 4
 if name == "F" or name == "E#":
  tone = 5
 if name == "F#" or name == "Gb":
  tone = 6
 if name == "G":
  tone = 7
 if name == "G#" or name == "Ab":
  tone = 8
 if name == "A":
  tone = 9
 if name == "A#" or name == "Bb":
  tone = 10
 if name == "B" or name == "Cb":
  tone = 11

 octave = int(note[-1:])

 pitch = tone + octave * 12 + 21
 return pitch

def makeProgression( first, last, progression, MyMIDI ):
 global time
 for p in range(first,last + 1):
  MyMIDI.addNote(0,0,p,time,1,100)
  MyMIDI.addNote(0,0,p + 4,time,1,100)
  MyMIDI.addNote(0,0,p + 7,time,1,100)
  time = time + 2
  for note in progression:
   note = note.split("/")
   pitch = noteToPitch(note[0]) + p - first
   duration = float(note[1])
   MyMIDI.addNote(0,0,pitch,time,duration,100)
   time = time + duration
  MyMIDI.addNote(0,0,p,time,1,100)
  MyMIDI.addNote(0,0,p + 4,time,1,100)
  MyMIDI.addNote(0,0,p + 7,time,1,100)
  time = time + 1

 for p in range(last-1,first-1,-1):
  MyMIDI.addNote(0,0,p,time,1,100)
  MyMIDI.addNote(0,0,p + 4,time,1,100)
  MyMIDI.addNote(0,0,p + 7,time,1,100)
  time = time + 2
  for note in progression:
   note = note.split("/")
   pitch = noteToPitch(note[0]) + p - first
   duration = float(note[1])
   MyMIDI.addNote(0,0,pitch,time,duration,100)
   time = time + duration
  MyMIDI.addNote(0,0,p,time,1,100)
  MyMIDI.addNote(0,0,p + 4,time,1,100)
  MyMIDI.addNote(0,0,p + 7,time,1,100)
  time = time + 1
 return MyMIDI

def main(argv):

 if len(argv) == 1:
  for line in open(argv[0],'r'):
   MyMIDI = MIDIFile(1)
   MyMIDI.addTempo(0,0,120)
   array = line.split(";")
   MyMIDI = makeProgression(noteToPitch(array[0]),noteToPitch(array[1]),array[2].split(" "), MyMIDI)
   writeToFile(array[3].rstrip('\n'), MyMIDI)
   MyMIDI = None
 else:
  print "Enter first note in sequence: "
  firstnote = noteToPitch(raw_input())
  # process first note

  print "Enter last note in sequence: "
  lastnote = noteToPitch(raw_input())
  # process last note

  print "Enter first note progression in the following format: "
  print "note/duration note/duration note/duration"
  progression = raw_input()
  # process note progression

  progression = progression.split(" ")
  makeProgression(firstnote,lastnote,progression)

  print "Enter file name: "
  filename = raw_input()
  writeToFile(filename)

def writeToFile(filename, MyMIDI):
 binfile = open(filename, 'wb')
 MyMIDI.writeFile(binfile)
 binfile.close()

if __name__ == "__main__":
 main(sys.argv[1:])
