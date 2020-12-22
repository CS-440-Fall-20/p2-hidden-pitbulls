# WORKING ON GITHUB NOW - ON REPL.IT THIS MIGHT BE OUTDATED

from myimage import MyImage

'''
2D Array containing the music melodic sequence:

Each entry M[m] of the array is a single beat. 
It can either be a musical note or silence.
M[m][0] contains the musical note and it's octave value (i.e 'C3').
M[m][1] contains the duration that the note is played for; 
2 is a full duration note, 1 is a half duration note, etc.
This convention can be changed however the lowest  
unit of note should always be represented by 1.
NN refers to null, or beats with silence. 
Like a note, a silent beat will have a duration value.
For example:
M = 
[
  ('C3', 1), ('C3', 1), ('D3', 2), ('NN', 2), 
  ('C3', 2), ('NN', 2), ('E3', 2), ('C3', 4)
]

Color wheel:
  Reference: https://i.pinimg.com/originals/ad/4b/cf/ad4bcfcd6b94b8be1aaa9717c08ff580.png

  Red: (255, 0, 0), Orange: (255, 127, 0), 
  Yellow: (255, 255, 0), Green-Yellow: (127, 255, 0), 
  Green: (0, 255, 0), Green-Cyan: (0, 255, 127),
  Cyan: (0, 255, 255), Blue-Cyan: (0, 127, 255), 
  Blue: (0, 0, 255), Blue-Magenta: (127, 0, 255), 
  Magenta: (255, 0, 255), Red-Magenta: (255, 0, 127)


The western chromatic scale: 
Sharp representation (#) of accidental notes 
is used rather than flat representation (b)
['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'] 

'''

# The chromatic scale to color wheel mapping
mapping = {
  'A': (255, 0, 0), 'A#': (255, 127, 0), 
  'B': (255, 255, 0), 'C': (127, 255, 0), 
  'C#': (0, 255, 0), 'D': (0, 255, 127),
  'D#': (0, 255, 255), 'E': (0, 127, 255), 
  'F': (0, 0, 255), 'F#': (127, 0, 255), 
  'G': (255, 0, 255), 'G#': (255, 0, 127),
  'NN': (255, 255, 255)
}

def PixelColour(melodyArr: [], sig: int):
    '''
    Function to convert a melody to an image

    Arguments:
    melodyArr is the array of melodic beats described above.
    sig is the time signature of the music; 
    e.g. 8 beats per measure, 16 beats per measure, etc.
    --startingNote is the first note of the melody.-- (REMOVED)
    --key is the key the song is in; e.g. A, C, Dm, F#.--(REMOVED)

    Returns: 
    MyImage object

    '''

    # Setting x dimension
    x = sig 

    # Counting total duration of   
    # melody in beats for y dimension
    totalBeats = 0
    for noteOctDur in melodyArr:
      totalBeats += noteOctDur[1]

    # Setting y dimension
    y = totalBeats // sig
    
    # Creating image
    img = MyImage((x, y), 0, 100, 'RGBA')

    # Keeping track of beats and 
    # measures or x and y values
    beat = 0
    measure = 0

    for noteOctDur in melodyArr:
      
      # Separating note and octave
      note = ''
      octave = ''
      for char in noteOctDur[0]:
        if (char in 'ABCDEN#'):
          note += char
        else:
          octave += char

      # Converting octave from
      # str to int for alpha value
      if (len(octave) != 0):
        octave = int(octave)
      else:
        octave = 0

      for halfNote in range(noteOctDur[1]):
        
        # Setting alpha value based on octave
        alphaVal = int((255 / 8) * (8 - octave))

        # Adding the colored pixel to the image
        img.putpixel((beat, measure), mapping[note] + (alphaVal,))
        
        # Changing beats and measures
        # or x and y values
        beat += 1
        if (beat == sig):
          measure = (measure + 1) % y
        beat = beat % x

    # Showing and returning image
    img.show()  
    return img

    '''
    MUST DELETE FOLLOWING COMMENTS - ONLY FOR DEVELOPERS
    1. Create an empty instance of myimage class with a large enough size for virtual pixels. 
    x dimension of the image will be sig; y dimension will be size(melodyArr) // no of beats per measure
    2. Determine the starting colour based on the root note of the music key. For example, 
    if music is in the key of A, the starting colour is Red (use chromatic scale to colour wheel mapping).
    3. Iterate over each ith element of the melodyArr, based on the sig value. 
    For example, if the music is in a time signature of 8 beats, after every 7th iteration we start with 
 
    '''

def _test1():
  M = [
    ('C3', 1), ('C3', 1), ('D3', 2), ('NN', 2), 
    ('C3', 2), ('NN', 2), ('E3', 2), ('C3', 4)
  ]
  
  PixelColour(M, 4)
    
if __name__ == '__main__':
  _test1()
  
