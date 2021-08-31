# Used txt files to store songs' links
# Using classes and objects to store songs' writer, genre, type etc. will prove beneficial
# Further experiments and work required
# Object notations could be useful

from library.VoiceIO import assistant_response
from library.misc import extract_word,pickRandom
import webbrowser as wb

def getMusicRequest(text):
    # Applying a parsing procedure to extract the type of music from the text
    fstr = "play a {} song"
    Type = Type = extract_word(text, fstr)
    if Type == 0:
        fstr = "play a {} music"
        Type = extract_word(text, fstr)
        if Type == 0:
            assistant_response("Sorry, I couldn't understand. Could you repeat that, please")
            return 0
    return Type

def getMusicList(songsdir,Type):
    # Using the type parameter to find list containing that type of songs and returns the contents of the file as a list
    if Type == 0:
        return 0
    doc=songsdir+Type+".txt"
    try:
        Songs = open(doc, 'r')  # Opens the txt file in reading format
    except FileNotFoundError:
        assistant_response("sorry, i couldn't find that type of song")  # Notify if that type of music list is not valid
        return 0
    SongList = Songs.readlines()  # Store the contents of the txt file to a temporary list
    Songs.close()  # Closing the file for memory reduction
    for i in range(0, len(SongList)):  # Removing "\n" to prevent bugs when opening in browser
        SongList[i] = SongList[i].replace("\n", "")
    return SongList

def playRandomMusic(web_path,List):
    # Using the list to play a random song on youtube
    YTprefix = "https://www.youtube.com/watch?v="
    if List == 0:
        return False
    elif List == []:
        assistant_response("I don't know any songs of that type")
        return False
    else:
        # Adding song ID's to youtube link prefix instead of using whole link to reduce memory usage
        wb.get(web_path).open_new_tab(YTprefix + pickRandom(List))  # Plays a random song from the list
        return True