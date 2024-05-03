# Self.py Hangman Project - Tomer Haik
## Game Process - This README is txt because md is messing up the new lines 

--------------------------------------------------------

Welcome to the Hangman game!
    __  _____    _   __________  ______    _   __
   / / / /   |  / | / / ____/  |/  /   |  / | / /
  / /_/ / /| | /  |/ / / __/ /|_/ / /| | /  |/ /
 / __  / ___ |/ /|  / /_/ / /  / / ___ |/ /|  /
/_/ /_/_/  |_/_/ |_/\____/_/  /_/_/  |_/_/ |_/

Lives: 6
Enter words text file path: C:\...\words.txt
Enter word index (min 1): 6

Let's start!
_ _ _ _ _

Guess a letter: b
b _ _ _ _

Guess a letter: e
b e _ _ _

Guess a letter: e
X
Guessed Letters: b -> e

Guess a letter: w
Wrong :(

x-------x
|       |
|       0
|
|
|

b e _ _ _

Guess a letter: q
Wrong :(

x-------x
|       |
|       0
|       |
|
|

b e _ _ _

Guess a letter: d
Wrong :(

x-------x
|       |
|       0
|      /|
|
|

b e _ _ _

Guess a letter: x
Wrong :(

x-------x
|       |
|       0
|      /|\
|
|

b e _ _ _

Guess a letter: c
b e _ c _

Guess a letter: g
Wrong :(

x-------x
|       |
|       0
|      /|\
|      /
|

b e _ c _

Guess a letter: h
b e _ c h

Guess a letter: a

WIN!
Secret Word: beach
Total Fails: 5/6