CECS3210 - Advanced Programming
SP21

Project 01: Simple Python Game

/////////////////////////////////////////////////////////////
/// Be sure to run the game with the included .gif icons! ///
/////////////////////////////////////////////////////////////

	This project recreates the simple game of Rock, Paper, Scissors
	in Python using the graphics.py library. 

	This program prompts the user to enter how many rounds of the 
	game they would like to play. It then constructs the GUI containing 
	the "buttons" for the player's choice on the bottom and the opposing 
	CPU's options on top . The player's clicks are validated for their 
	position on the window. Messages can pop up during the validation process,
	asking the user to click on the right "buttons". Once the player inputs 
	their choice for the round, the program then randomly generates it's own 
	using a random number generator. The screen then flashes through both 
	the player's and CPU's "buttons" until it reveals each choice and 
	ultimately determine the round's winner. A .txt transcript is printed
	once the game closes with all of the round results. 