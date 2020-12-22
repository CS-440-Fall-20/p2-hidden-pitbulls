# MOVING THE FOLLOWING TO GITHUB

from myimage import *

'''
2D Array containing the music melodic sequence
Each entry M[m] of the array is a single beat. It can either be a musical note or silence
M[m][0] contains the musical note and it's octave value (i.e 'C3')
M[m][1] contains the duration that the note is played for; 1 is a full duration note, 1/2 is a half duration note, etc
NN refers to null, or beats with silence. Like a note, a silent beat will have a duration value

M = [('C3', 1/2), ('C3', 1/2), ('D3', 1), ('NN', 1), ('C3', 1), ('NN', 1), ('E3', 1), ('C3', 2)]

Predefine the 12 colours on the colour wheel and their RGB values with a dictionary
Reference: https://i.pinimg.com/originals/ad/4b/cf/ad4bcfcd6b94b8be1aaa9717c08ff580.png

colourArr = {
  'Red': (255, 0, 0), 'Orange': (255, 127, 0), 
  'Yellow': (255, 255, 0), 'Green-Yellow': (127, 255, 0), 
  'Green': (0, 255, 0), 'Green-Cyan': (0, 255, 127),
  'Cyan': (0, 255, 255), 'Blue-Cyan': (0, 127, 255), 
  'Blue': (0, 0, 255), 'Blue-Magenta': (127, 0, 255), 
  'Magenta': (255, 0, 255), 'Red-Magenta': (255, 0, 127)
}

Notes of the western chromatic scale. Sharp representation (#) of accidental notes is used rather than flat representation (b)

chroma = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

'''

# the chromatic scale to color wheel mapping
mapping = {
  'A': (255, 0, 0), 'A#': (255, 127, 0), 
  'B': (255, 255, 0), 'C': (127, 255, 0), 
  'C#': (0, 255, 0), 'D': (0, 255, 127),
  'D#': (0, 255, 255), 'E': (0, 127, 255), 
  'F': (0, 0, 255), 'F#': (127, 0, 255), 
  'G': (255, 0, 255), 'G#': (255, 0, 127)
}

# melodyArr is the array of melodic beats described above
# sig is the time signature of the music; e.g. 8 beats per measure, 16 beats per measure, etc
# key is the key the song is in; e.g. A, C, Dm, F#
def pixelColour(melodyArr: [], sig: int, key: str):
    '''
    1. Create an empty instance of myimage class with a large enough size for virtual pixels. x dimension of the image will be sig; y dimension will be size(melodyArr) // 2
    2. Determine the starting colour based on the root note of the music key. For example, if music is in the key of A, the starting colour is Red (use chromatic scale to colour wheel mapping).
    3. Iterate over each ith element of the melodyArr, based on the sig value. For example, if the music is in a time signature of 8 beats, after every 7th iteration we start with 
    4. 
    '''
    pass

