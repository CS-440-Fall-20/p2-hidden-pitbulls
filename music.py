# WORKING ON GITHUB NOW - ON REPL.IT THIS MIGHT BE OUTDATED

from myimage import MyImage

'''
An array containing the musical sequence in chords:
Each entry music[m] of the array is a single beat. 
It can either be a chord (fifth, major, minor or seventh) or silence.
N refers to null, or beats with silence. 

Color wheel for notes on the western chromatic scale:
  Reference: https://i.pinimg.com/originals/ad/4b/cf/ad4bcfcd6b94b8be1aaa9717c08ff580.png

  Red: (255, 0, 0), Orange: (255, 127, 0), 
  Yellow: (255, 255, 0), Green-Yellow: (127, 255, 0), 
  Green: (0, 255, 0), Green-Cyan: (0, 255, 127),
  Cyan: (0, 255, 255), Blue-Cyan: (0, 127, 255), 
  Blue: (0, 0, 255), Blue-Magenta: (127, 0, 255), 
  Magenta: (255, 0, 255), Red-Magenta: (255, 0, 127),
  White: (255, 255, 255)

'''

# The western chromatic scale: 
# Sharp representation (#) of accidental notes 
# is used rather than flat representation (b).
chroma = [
  'A', 'A#', 'B', 'C', 'C#', 'D', 
  'D#', 'E', 'F', 'F#', 'G', 'G#'
] 

# The chromatic scale to color wheel mapping
mapping = {
  'A': (255, 0, 0), 'A#': (255, 127, 0), 
  'B': (255, 255, 0), 'C': (127, 255, 0), 
  'C#': (0, 255, 0), 'D': (0, 255, 127),
  'D#': (0, 255, 255), 'E': (0, 127, 255), 
  'F': (0, 0, 255), 'F#': (127, 0, 255), 
  'G': (255, 0, 255), 'G#': (255, 0, 127),
  'N': (255, 255, 255)
}

def _ChordToNotes(chord: str):
    '''
    Helper function to return notes given a chord.
    Only for chords fifth, major, minor and seventh.

    Arguments:
    chord as a string

    Returns:
    A list of notes

    '''

    # Separating first note and chord types   
    firstNote = ''
    chordType = ''

    for char in chord:
      if (char in 'ABCDEN#'):
        firstNote += char
      elif (char in 'm57M'):
        chordType += char

    if (len(chordType) == 0):
      chordType += 'M'

    # Finding the position of first note
    # on the chromatic scale
    chromaInd = chroma.index(firstNote)

    # Returning list of notes according to
    # first note and chord type
    if (chordType == '5'):
      return [firstNote, chroma[chromaInd + 4]]
    elif (chordType == 'M'):
      return [firstNote, chroma[chromaInd + 2], chroma[chromaInd + 4]]
    elif (chordType == 'm'):
      return [firstNote, chroma[chromaInd + 3], chroma[chromaInd + 4]]
    else:
      return [firstNote, chroma[chromaInd + 2], chroma[chromaInd + 4], chroma[chromaInd + 6]]

def _InterpolateHorizontal(img, startPos, endPos, startColor, endColor):
    diff = abs(endPos[0] - startPos[0])
    r_grad = (endColor[0] - startColor[0]) / diff
    g_grad = (endColor[1] - startColor[1]) / diff
    b_grad = (endColor[2] - startColor[2]) / diff
    a_grad = (endColor[3] - startColor[3]) / diff

    img.putpixel(startPos, startColor)

    x = startPos[0]
    y = startPos[1]
    r = startColor[0]
    g = startColor[1]
    b = startColor[2]
    a = startColor[3]

    for pixelPos in range(1, diff):
      x += pixelPos
      r += r_grad
      g += g_grad
      b += b_grad
      a += a_grad

      img.putpixel((x, y), (round(r), round(g), round(b), round(a)))

    img.putpixel(endPos, endColor)

    return img
    

def CreateWall(music: []):
    '''
    Function to convert a melody to an image

    Arguments:
    music as a list of chords.

    Returns: 
    MyImage object.

    '''

    # Setting y dimension
    yDim = len(music)
    
    # Creating image
    img = MyImage((16, yDim), 0, 20, 'RGBA')

    # For each chord position or y value
    for chordPos in range(yDim):
      # Storing the chord
      chord = music[chordPos]

      # If it is not silent
      if (chord != 'N'):
        # Extracting notes from the chord
        notes = _ChordToNotes(music[chordPos])
        
        # Values needed to interpolate between notes
        notesLastInd = len(notes) - 1
        jump = 15 // notesLastInd

        # For each note except the last two
        for i in range(notesLastInd - 1):
          # Storing start and end colors
          startColor = mapping[notes[i]] + (255,)
          endColor = mapping[notes[i + 1]] + (255,)

          # Interpolating colors in the middle accordingly
          _InterpolateHorizontal(img, ((jump * i), chordPos), ((jump * (i + 1)), chordPos), startColor, endColor)

        # Interpolating colors between the last two notes
        startColor = endColor
        endColor = mapping[notes[notesLastInd]] + (255,)
        _InterpolateHorizontal(img, ((jump * (notesLastInd - 1)), chordPos), (15, chordPos), startColor, endColor)

    # Showing and returning image
    img.show()  
    return img

def _test():
    music = [
      'D', 'N', 'D', 'D', 'Bm', 'N', 'Bm', 'Bm',
      'D', 'N', 'D', 'D', 'Bm', 'N', 'Bm', 'Bm',
      'D', 'N', 'D', 'D', 'Bm', 'N', 'Bm', 'Bm',
      'D', 'N', 'D', 'D', 'Bm', 'N', 'Bm', 'Bm',

      'Em', 'N', 'Em', 'Em', 'A7', 'N', 'A7', 'A7',
      'D', 'N', 'D', 'D', 'Bm', 'N', 'Bm', 'Bm',
      'D', 'N', 'D', 'D', 'N', 'D', 'D', 'D',
      'D', 'N', 'D', 'D', 'N', 'D', 'D', 'D',

      'Bm', 'N', 'Bm', 'Bm', 'D', 'N', 'D', 'D'
      'Bm', 'N', 'Bm', 'Bm', 'D', 'N', 'D', 'D'
      'Bm', 'N', 'Bm', 'Bm', 'D', 'N', 'D', 'D'
      'Bm', 'N', 'Bm', 'Bm', 'D', 'N', 'D', 'D'

      'Em', 'N', 'Em', 'Em', 'N', 'Em', 'Em', 'Em'
      'A7', 'N', 'A7', 'A7', 'N', 'A7', 'A7', 'A7'
      'A#', 'N', 'A#', 'A#', 'N', 'A#', 'A#', 'A#'
    ]

    CreateWall(music)
    
if __name__ == '__main__':
  _test()
  
