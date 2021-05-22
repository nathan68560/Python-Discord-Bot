# Python-Discord-Bot
A small discord bot I made in python with discord.py to learn the python programming language.

## Functionalities
- The command **!morpion** give the commands used to start, play and stop a morpion game *(Tic Tac Toe)* agaisnt the bot.
- The command **!bataille** start a navalle battle game against the bot and give the player all the commands to use, step-by-step
- The bot respond to "Pierre", "Feuille", or "Ciseau" with one random word out of those three, that's the french version of *Rock-Paper-Scissors*
- The bot repeat every sentences containing the word *"ping"* but replace it with the word *"pong"*
- Every command is erased from the channel after being processed by the bot *(the bot require the Administrator status on the server)*

### Morpion game
The morpion game, also known as Tic Tac Toe, draw a textual 3 by 3 grid. The bot start by placing a cross in a random cell of the grid, the player can
then place it's circle in the cell of his choice with the command **!morpion *pos*** with *pos* being the index of the cell, starting at 0 from top left to
8 on bottom right. After every player's actions, the bot check if there's a winner, if not, he procceed to randomly place a cross then check again for a winner,
until there's no empty cell left and the game end on a draw.

### Bataille game
The navalle battle game is a bit more complex than the morpion one since it's made of 2 different 'gamestate'. In the first one, the player have to place
his ships on the board, and only on the second one he can try and destroy those of the bot. At the begining of the game, the bot send the grid that will be
used as the battle field, it's a 9 columns by 4 rows grid (a1 to d9). The player can then place 6 ships on the field with the command **!bataille add *pos***
with *pos* being the name of the cell as shown on the grid shown earlier. The player can also directly add the 6 ships with one command by just adding each *pos*
one after another. Once the count of 6 ships is reached, the game switch to the second state and the player can now try to destroy the bot's ships with the 
command **!bataille try *pos***. Aftre each try, the bot tell the player if a ship as been hit or not, and then try to destroy one of the player's ships.

## How To Use
Just follow [this tutorial on how to create a discord bot](https://realpython.com/how-to-make-a-discord-bot-python/#creating-an-application) and then replace
*Bot_Access_Token* with your bot's access token in **discordBot.py**.
