# XORIS
Xoris is a two-player guessing game often played on a board with 11 rows and 11 columns and two dimensions. The two players take turns "putting" their checkers or unique identifying markers in a board cell of their choosing. Through the program's prompt, the coordinates of a cell are entered for placement. It is modifiable to accommodate multiplayer games, program can handle any number between 2 and 5 players. In the case of 5 players, their respective checkers (or marks) are: X, O, R, I and S. Regardless of the number of game participants, a player needs 4 checkers appropriately placed in sequence to score a win.
The players take turns and each “places” her checker into a cell of choice, indicated by both a letter (row) and a number (column). The form of the input is: A9, C2, K10, etc. Any input either beyond the dimensions allowed or malformed are considered an invalid entry and the player should repeat her move. For example, B09, S9, M21 are all invalid entries. A player can never place his token on a cell already occupied as this is also an invalid entry. In all instances, the user input is validated before placing the checker.
Before the start of a game, a player between the 2 participants is randomly chosen to play first. If more players participate, the sequence of the play by all involved should be decided randomly before Xoris goes into game-phase.
By default game is set to 5 players mode where first turn is randomly selected and then next turn is given to the next player accordingly to the word of XORIS.
# Requirements
Python 3

