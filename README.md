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


## CP - Place piece

To place a piece to have to indicate which player is placing it, followed by the size of the piece and the position of the collumn where its being placed.

