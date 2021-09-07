# Lucy
A virtual assistant

Summary:
Lucy is a virtual assistant that can help users with their basic operations.
She has speech recognition and text-to-speech for input and output so users can communicate and give commands via their voice.
Things she can do:

    open programs   
    search on google    
    tell date and time    
    play a song    
    keep a to-do list    
    shutdown/restart/sleep


Contributors:
    Author/Creator: Hakan Kestir (Huntsound) Hakankestir@gmail.com
    Contributor: Emre Alaybeyoglu Emrealaybeyoglu01@gmail.com

Necessary packages and versions:

    Python 3.9.0 64-bit
    PyAudio 0.2.11
    SpeechRecognition 3.8.1
    pyttsx3 2.90
    parse 1.18.0



In-Python modules:

    os
    datetime
    calendar
    warnings
    random
    webbrowser



Recommended folder configuration:

    ==Case Sensitive==
    /library/
    /Shortcuts/
    /Shortcuts/Games/
    /Shortcuts/Production/
    /Shortcuts/Softwares/
    /Songs/
    /Texts/To-Do List.txt



NOTE: These directory names can be changed in Lucy.py file, although not recommended.
in library/Program.py , users can change the names of the folders inside the Shortcuts folder, not recommended.

Add shortcuts of programs you want lucy to open inside one of the folders inside Shortcuts folder depending on their class, i.e games.
IMPORTANT: Name of the shortcuts must be lowercase.
IMPORTANT: Lucy will search based on its name so users have to give command using the name of the shortcuts

inside songs folder, create txt files.
Names of the files must be types of the songs inside that txt file.
i.e user wants to create a list of songs that are motivating. File name must be motivating.txt
when giving commands to Lucy, "play a motivating song" will open a random song from this motivating.txt file
Inside this file, YouTube VideoID's must be saved. It is the section after the "=" sign of YouTube URL

    i.e URL = https://www.youtube.com/watch?v=[dQw4w9WgXcQ]
                                              ^^This part^^



Operating Instructions:

For Lucy to accept commands, one of the wake words must be used at the beginning.
List of wake words can be found inside library/Answers.py

Lucy is also capable of handling multiple commands at once

To open a program from shortcuts folder: open up ...

To search on Google: search ...
NOTE:search and open up functions work fine on their own but if these functions get only one section of the command,
try using "open up ... okay" or "search ... okay"
NOTE:While using multiple commands at once and same problem occurs, try saying "and" between commands

For Lucy to tell date and time: Tell me date/time/date and time

To play a song from txt files mentioned above: play a ... song/play a ... music

To write in to-do list: write my to-do list
After this Lucy will ask for an entry
After giving an entry, Lucy will ask confirmation
yes I do for confirmation
no I don't denying
nevermind for canceling
IMPORTANT: When writing an entry, Lucy enters into another loop.
Denying WON'T exit from this loop, it must be cancelled or an entry must be confirmed.

For Lucy to read contents of to-do list: read my to-do list

To clear to-do list: clear my to-do list

To delete a single entry from to-do list: delete entry number ... from to-do list

For system functions: shutdown/restart/sleep computer

Users can ask How is lucy using one of the phrases inside library/Answers.py salute list

To dismiss and close Lucy, use one of the phrases inside library/Answers.py goodbye list




Customization:

Answers.py contains the phrases user uses for certain events.
Responses.py contains the phrases Lucy says to the user in certain events.
Contents of these files can be modified to fit into a better use for user.
Changing commands inside other files to customize can be done but NOT RECOMMENDED
IMPORTANT: inside library/misc.py file, there is a list called func_list. Changing it WON'T CHANGE the commands.
It would break the code.




Problems and future features:
Lucy is very deterministic at the moment but we work on natural language processing to solve this problem.

Users can ask how is lucy but lucy will give a randomized answer which is not suitable for this.
To slove this problem, we are working on a neural network to determine the mood of lucy using inputs like:
battery, uptime, current time, weather etc.

We are also planning to add a feature for lucy to introduce herself, telling user what she can do, which games does she has etc.

We are also planning to add a timer feature to Lucy's already existing to-do list function
