The following details the instructions for executing the program.

The main file is music.py, which has to be run. Make sure that myimage.py is in the same directory. Running the program as provided should output the same image as in the pdf.

For different test cases, modify the input of the program. The input is taken in the form of the 'music' array in music.py (line 15):

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
    
    This is first verse of the song provided in Appendix A. To see what the different progressions chord progressions, the following steps must be taken:
    
    1. Identify the chords to be played in the song. An example progression is available in Appendix A (e.g. the chorus on page 17).
    2. Replace the chords in the music array with the chords to be played. Chords can be input in the form of X, Xm, X5 or X7
    (where X is a major chord, Xm is a minor chord, X5 is a 5th chord and X7 is a 7th chord). X can be any one of the 12 chroma (including # notes) in line 24.
    You may also add additional chords to the array, which will lead to the number of pixel rows in the output image expanding.
    3. The 'N' corresponds to a silent or skipped beat, as is the case with strumming patterns in a guitar.
    You may replace the 'N's if you wish to come up with a different strumming pattern, but it is recommended to leave them as it is (another example is X, N, X, X, N, X, X, X).
    4. Run the program and see the outputted chords!
    
    BONUS: Not required, but you can also modify the RGB values of the note-colour mappings in the 'mapping' dictionary (line. 34) and see how it affects the visual profile of the chords.
