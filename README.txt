CECS3210 - Advanced Programming
SP21

Project 01: Simple Python Game

	This project recreates the simple game of Rock, Paper, Scissors
	in Python using the graphics.py library. The GUI is first constructed
	with the "buttons" for the player's choice on the bottom and the
	opposing CPU's options on top but blacked out. The game first 
	scans any of the player's clicks and validates it's position on the
	window. Messages can pop up during the validation process, asking the
	user to click on the "buttons" to properly make their choice. Once
	the player inputs their choice for the round, the program then 
	randomly generates it's own choice using random number generators.
	The screen then flashes through both the player's and CPU's "buttons"
	as a sort of count down to then reveal each choice and ultimately
	determine that round's winner.