# Contributors
[Andre Gonçalves](https://github.com/AndrePG98) ,
[Tiago Gonçalves](https://github.com/Tiago-Goncalves98)


# Connect-N
A console only connect 4 with a twist using python and MVC design pattern. (The game is all in portuguese)

# How to play/List of commands

To play Connect N you simply have to run the 'program.py' python file and start using these commands:

## RJ - Register players

Example: RJ _player name_

Note that there cannot be spaces in the player name.

![image](https://github.com/Tiago-Goncalves98/Connect-N/assets/81558370/b9033042-3d8a-442b-889e-ca8adf1fcc24)

## EJ - Remove player

Example: EJ _player name_

![image](https://github.com/Tiago-Goncalves98/Connect-N/assets/81558370/c458551d-c23b-41b2-82ce-db610589552e)

## LJ - List players

This will list of every player followed by their number of games and wins.

![image](https://github.com/Tiago-Goncalves98/Connect-N/assets/81558370/367001ee-855b-46a4-b849-2801064a0d53)

## IJ - Start game

To start a game you can enter _IJ_ followed by the two names to the players as such: 

![image](https://github.com/Tiago-Goncalves98/Connect-N/assets/81558370/70393efe-d39e-4e47-bb01-6df363cef928)

Next you need to enter dimensions of your desired grid and the N for the win condition as it can be different than 4!

![image](https://github.com/Tiago-Goncalves98/Connect-N/assets/81558370/b1ce30e7-31db-4839-b39b-825aef7af4ca)

Here I made a 10x10 grid and made it so that I have to connect 3 to win.

Next we can enter our special pieces.

Special pieces can have a length different to the tradicial 1 but cannot be equal of greater than any of the dimensions of the grid. 

![image](https://github.com/Tiago-Goncalves98/Connect-N/assets/81558370/f7b037c5-b455-4a56-b463-ce1c18e73aaa)

In this case as I entered _2_ four times both players will have four pieces of length _2_.

![image](https://github.com/Tiago-Goncalves98/Connect-N/assets/81558370/a88627a3-d904-4480-84bd-3d705688ae19)

## DJ - Forfeit game

Can be used for one or both players to forfeit the game. If both players forfeit none will have their wins increased in the _LJ_ command of course.

![image](https://github.com/Tiago-Goncalves98/Connect-N/assets/81558370/7340f462-c345-43f5-89b5-2f6149bacb7c)

Here only Player1 forfeited so Player2 was awarded the victory.

## V/VG - Two ways of visualizing the grid

* _V_ - Displays the coordenates of every point on the grid followed by the name of player that "owns" that point, if noone owns that point yet Empty(_Vazio_) is displayed.

![image](https://github.com/Tiago-Goncalves98/Connect-N/assets/81558370/b4048e0d-ee06-40a6-a5fd-e316b33d0711)

* _VG_ - Displays the actual grid, if noone owns that point yet 0 is displayed, otherwise it displays the name of the player.

![image](https://github.com/Tiago-Goncalves98/Connect-N/assets/81558370/b1169710-8500-48b5-8bde-3845cf03f6cc)

## DJ - Game details

It displays the dimensions of the currrent game, the players involved and the number of specials pieces available.

![image](https://github.com/Tiago-Goncalves98/Connect-N/assets/81558370/28ae24d5-ea1b-410b-9cdc-e1c246a04e7d)

Here is a 10x10 game, both players have one piece of size _2_ and two pieces of size _3_.

## CP - Place piece

To place a piece to have to indicate which player is placing it, followed by the size of the piece and the position of the column where its being placed.

![image](https://github.com/Tiago-Goncalves98/Connect-N/assets/81558370/ca7f7c35-d0e4-4f95-855d-970aea359ab8)

Here Player1 placed a piece of size 1 in the second column.

But we also have specials pieces.
And to use specials pieces we also need to specify the direction in which the piece is layed like so:

![image](https://github.com/Tiago-Goncalves98/Connect-N/assets/81558370/c3258b06-7ff8-46c2-a483-b6377bd9df22)

Here Player2 placed its special piece sized _3_ in the ninth column going left.
To specify the direction in which the piece is layed we need to add _E_ (left) or _D_ (right) after the position of the inicial piece.


## G/L - Save and load current game and players

You can save the current game (if there is one ongoing) and players by using: G _yourFileName_

![image](https://github.com/Tiago-Goncalves98/Connect-N/assets/81558370/5e1d53ae-ff5c-4496-96c6-c5b5b2706b6d)

You can also load data from this file withL: L _yourFileName_

![image](https://github.com/Tiago-Goncalves98/Connect-N/assets/81558370/f501fb9a-9c7f-4da9-8660-145cb5286961)

Here I tried to list all players but there were none registered.
After load my data I can now list them.

All data in recorded in a local file where you have the program.

## F - Close Program

Not much to say on this one it just close the terminal (not that it does not save).
