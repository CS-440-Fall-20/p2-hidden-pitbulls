from myimage import MyImage

'''
An array containing the musical sequence in chords:
Each entry music[m] of the array is a single beat. 
It can either be a chord (fifth, major, minor or seventh major) or silence.
N refers to null, or beats with silence. 

Color wheel for notes on the western chromatic scale:
  Reference: https://i.pinimg.com/originals/ad/4b/cf/ad4bcfcd6b94b8be1aaa9717c08ff580.png

  Red: (255, 0, 0), Orange: (255, 127, 0), 
  Yellow: (255, 255, 0), Green-Yellow: (127, 255, 0), 
  Green: (0, 255, 0), Green-Cyan: (0, 255, 127),
  Cyan: (0, 255, 255), Blue-Cyan: (0, 127, 255), 
  Blue: (0, 0, 255), Blue-Magenta: (127, 0, 255), 
  Magenta: (255, 0, 255), Red-Magenta: (255, 0, 127)

'''

# The western chromatic scale: 
# Sharp representation (#) of accidental notes 
# is used rather than flat representation (b).
chroma = [
  'A', 'A#', 'B', 'C', 'C#', 'D', 
  'D#', 'E', 'F', 'F#', 'G', 'G#'
]

# Scales for chords, based on the rules for composing 
# scales relative to semitones from the previous note.
major = '02212221'
minor = '02122122'

# The chromatic scale to color wheel mapping.
mapping = {
  'A': (255, 0, 0), 'A#': (255, 127, 0), 
  'B': (255, 255, 0), 'C': (127, 255, 0), 
  'C#': (0, 255, 0), 'D': (0, 255, 127),
  'D#': (0, 255, 255), 'E': (0, 127, 255), 
  'F': (0, 0, 255), 'F#': (127, 0, 255), 
  'G': (255, 0, 255), 'G#': (255, 0, 127)
}

def _ChordToNotes(chord: str):
    '''
    Helper function to return notes given a chord.
    Only for chords fifth, major, minor and seventh major.

    Arguments:
    chord as a string.

    Returns:
    A list of notes.

    '''

    # Separating first note and chord types.   
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
    # on the chromatic scale.
    chromaInd = chroma.index(firstNote)

    # Returning list of notes according to
    # first note and chord type.
    ret = [firstNote]

    if (chordType == '5'):
      for i in range(7):
        chromaInd =+ (chromaInd + int(major[i])) % 12
        if (i == 4):
          ret.append(chroma[chromaInd])

    elif (chordType == 'M'):
      for i in range(7):
        chromaInd = (chromaInd + int(major[i])) % 12
        if ((i == 2) or (i == 4)):
          ret.append(chroma[chromaInd])

    elif (chordType == 'm'):
      for i in range(7):
        chromaInd =+ (chromaInd + int(minor[i])) % 12
        if ((i == 3) or (i == 4)):
          ret.append(chroma[chromaInd])
    
    else:
      for i in range(7):
        chromaInd =+ (chromaInd + int(major[i])) % 12
        if ((i == 2) or (i == 4) or (i == 6)):
          ret.append(chroma[chromaInd])

    return ret

def _InterpolateHorizontal(img, startPos, endPos, startColor, endColor):
    '''
    Helper function to interpolate colors 
    between two pixels on a horizontal line.

    Arguments:
    img as MyImage object to write pixels into.
    startPos as starting pixel position.
    endPos as ending pixel position.
    startColor as color of starting pixel in rgba tuple.
    endColor as color of ending pixel in rgba tuple.

    Returns: 
    the MyImage object img after interpolation.

    '''
    diff = abs(endPos[0] - startPos[0])

    # Color component gradients.
    r_grad = (endColor[0] - startColor[0]) / diff
    g_grad = (endColor[1] - startColor[1]) / diff
    b_grad = (endColor[2] - startColor[2]) / diff
    # a_grad = (endColor[3] - startColor[3]) / diff

    # Coloring starting pixel.
    img.putpixel(startPos, startColor)

    x = startPos[0]
    y = startPos[1]
    r = startColor[0]
    g = startColor[1]
    b = startColor[2]
    # alpha value lowered to differentiate
    # between played notes and interpolated colors.
    a = 180 

    # Interpolating and coloring.
    for pixelPos in range(1, diff):
      x += 1
      r += r_grad
      g += g_grad
      b += b_grad
      # a += a_grad

      img.putpixel((x, y), (round(r), round(g), round(b), round(a)))

    # Coloring ending pixel.
    img.putpixel(endPos, endColor)

    return img
    

def CreateWall(music: []):
    '''
    Function to convert a melody to an image.

    Arguments:
    music as a list of chords.

    Returns: 
    The MyImage object img that contains the 'chromatic wall'
    (or grid of pixels with interpolated chord colours).

    '''

    # Setting y dimension.
    yDim = len(music)
    
    # Creating image 
    # (16 is used by default for number of columns,
    # as we fix our program 16 divisions of a beat).
    img = MyImage((16, yDim), 2, 20, 'RGBA')

    # For each chord position or y value.
    for chordPos in range(yDim):
      # Storing the chord.
      chord = music[chordPos]

      # If the beat is not a silent beat.
      if (chord != 'N'):
        # Extracting notes from the chord.
        notes = _ChordToNotes(chord)

        # Values needed to interpolate between notes.
        notesLastInd = len(notes) - 1
        jump = 15 // notesLastInd

        # For each pairs of notes except the last two.
        for i in range(notesLastInd - 1):
          # Storing start and end colors.
          startColor = mapping[notes[i]] + (255,)
          endColor = mapping[notes[i + 1]] + (255,)

          # Interpolating colors in the middle accordingly.
          img = _InterpolateHorizontal(img, ((jump * i), chordPos), ((jump * (i + 1)), chordPos), startColor, endColor)

        # Interpolating colors between the last two notes.
        startColor = endColor
        endColor = mapping[notes[notesLastInd]] + (255,)
        img = _InterpolateHorizontal(img, ((jump * (notesLastInd - 1)), chordPos), (15, chordPos), startColor, endColor)

      else:
        # Else fill a white line of 16 pixels.
        color = (255,) * 4
        img = _InterpolateHorizontal(img, (0, chordPos), (15, chordPos), color, color)

    # Showing and returning image.
    img.show()  
    return img

def _test():
    '''
    # Function to test the program.

    Arguments:
    None.

    Returns:
    None.
    
    '''

    # An array of chord progressions based
    # on the chords of "Still Alive" 
    # (Portal end song).   
    music = [
      'D', 'N', 'D', 'D', 'Bm', 'N', 'Bm', 'Bm',
      'D', 'N', 'D', 'D', 'Bm', 'N', 'Bm', 'Bm',
      'D', 'N', 'D', 'D', 'Bm', 'N', 'Bm', 'Bm',
      'D', 'N', 'D', 'D', 'Bm', 'N', 'Bm', 'Bm',

      'Em', 'N', 'Em', 'Em', 'A7', 'N', 'A7', 'A7',
      'D', 'N', 'D', 'D', 'Bm', 'N', 'Bm', 'Bm',
      'D', 'N', 'D', 'D', 'N', 'D', 'D', 'D',
      'D', 'N', 'D', 'D', 'N', 'D', 'D', 'D',

      'Bm', 'N', 'Bm', 'Bm', 'D', 'N', 'D', 'D',
      'Bm', 'N', 'Bm', 'Bm', 'D', 'N', 'D', 'D',
      'Bm', 'N', 'Bm', 'Bm', 'D', 'N', 'D', 'D',
      'Bm', 'N', 'Bm', 'Bm', 'D', 'N', 'D', 'D',

      'Em', 'N', 'Em', 'Em', 'N', 'Em', 'Em', 'Em',
      'A7', 'N', 'A7', 'A7', 'N', 'A7', 'A7', 'A7',
      'A#', 'N', 'A#', 'A#', 'N', 'A#', 'A#', 'A#'
    ]

    CreateWall(music)
    
if __name__ == '__main__':
  _test()
  
