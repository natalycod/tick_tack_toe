# tick_tack_toe
Console TickTackToe with Minimax algorithm

The main goal of the project - create TickTackToe on Python 3 to play it in Console. Program can never lose.

The game process:
* run main.py file
* choose number of rows (number of columnes is the same, since we are playing on a square field)
* choose the first player (you or the computer)
* play :)

Every step is just entering the field you want to make step in. When the game is ended, computer will automatically write the results. It was considered impossible to win the game (computer is playing the most optimal way), but you can try.

### About file navigation:

* tick_tack_toe_utils.py

Contains enums for Cells, Players and Game States. Also there are some methods with those enums for convenience.

* tick_tack_toe_field.py

Contains class for TickTackToe Field with empty initialization and needed methods: getting and putting values for cells and calculating game state (win, lose, draw or not ended)

* tick_tack_toe.py

Contains class for TickTackToe game. It's initialization of all the data we need for the game (field, player, symbol, etc) and needed methods: field printing, game result calculating, making step, printing rules.
Also contains smart algorithm Minimax to find the best step for the computer (it recursively brute forcing all the possibilities of next movements and finding the winning position. If can't find the winning position, make a step to draw position). Minimax doesn't really work fast on fields 4x4 and bigger.

* main.py

Calling function run_game, which imitates the game process. While the game is not ended, ask about next step from the User or make the best Minimax step for Computer.

* unit_tests.py

Contains tests for TickTackToe methods.
