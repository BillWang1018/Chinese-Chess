# ChineseChess
A Chinese chess game in console, writen in python.

## How To Play:

Use format `[a-j][1-9] [a-j][1-9] ` to move the chess
`ctrl + c` will stop the program.

```
   1   2   3   4   5   6   7   8   9   

a  車━━馬━━象━━士━━將━━士━━象━━馬━━車
   ┃   │   │   │ ╲ │ ╱ │   │   │   ┃
b  ┠───┼───┼───┼───┼───┼───┼───┼───┨
   ┃   │   │   │ ╱ │ ╲ │   │   │   ┃
c  ┠───砲──┼───┼───┼───┼───┼───砲──┨
   ┃   │   │   │   │   │   │   │   ┃
d  卒──┼───卒──┼───卒──┼───卒──┼───卒
   ┃   │   │   │   │   │   │   │   ┃
e  ┠═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══┨
   ┃       楚河         漢界       ┃
f  ┠═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══┨
   ┃   │   │   │   │   │   │   │   ┃
g  兵──┼───兵──┼───兵──┼───兵──┼───兵
   ┃   │   │   │   │   │   │   │   ┃
h  ┠───炮──┼───┼───┼───┼───┼───炮──┨
   ┃   │   │   │ ╲ │ ╱ │   │   │   ┃
i  ┠───┼───┼───┼───┼───┼───┼───┼───┨
   ┃   │   │   │ ╱ │ ╲ │   │   │   ┃
j  俥━━傌━━相━━仕━━帥━━仕━━相━━傌━━俥

   1   2   3   4   5   6   7   8   9   
```
> example: `c2 c5` moves "砲" 3 steps right.

The one who takes down the oppient's general wins!



## Parameters

In `main.py`, adding parameters in `startGame()` will change how the board is printed.

### Usable parameters:

`color: bool` -> whether the chesses is printed with color effect

`autoReverse: bool` -> whether the board is printed upside down according to who's playing (the board will always be south-facing the player)