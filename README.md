# Sideshooter-Game-Python
## Description 
A game where you can shoot at enemies on the right side of the screen in a scenario that is scrolling horizontally. 

It's also a simple example of how to use [Object-oriented programming (OOP) Principles](https://en.wikipedia.org/wiki/Object-oriented_programming) while coding a game in Python.

### Download
If you have windows, you can [download here the final executable game](https://github.com/igor-lirussi/Sideshooter-Game-Python/releases/latest/download/Sideshooter-Game-Python.exe).

You can [download here the final code of the game](https://github.com/igor-lirussi/Sideshooter-Game-Python/archive/refs/heads/main.zip)

You can [download here the code at checkpoint1](https://github.com/igor-lirussi/Sideshooter-Game-Python/releases/download/Release_1.0.0_2022-12-30_18-22/checkpoint1.zip)


### Topics:
- Classes 
- Basic Game Loop
- Sprites
- Key Inputs & Events
- Movements:
	- Controlled
	- Autonomous
- Collisions
- Game Mechanics
- Health system, score and stats
- Music

## Result
![Result](./img/result.gif)

## Requirements
- Python 3
- Pygame

## Run
if your environment has already the [`Requirements`](#requirements) you can start the game typing with the terminal in the folder: 
```bash
python game.py
```
otherwise see the  [`Installation`](#installation) below

## Installation
If you use Python with [Anaconda](https://www.anaconda.com/download). (I suggest Anaconda program to create isolated sandbox "environments" with python and your desired packages that you can easily delete or modify) 

in *Anaconda Prompt*:
```bash
conda create -n pygame python=3.10 #creates environment called "pygame" with python (needed just once)
conda activate pygame  #activates the environment (you need to activate the environment every time you open the prompt)
pip install pygame #installs the pygame package (needed just once)
```

If you don't use Anaconda:
```bash
pip install pygame #installs the pygame package (needed just once)
```
Now you can  [`Run`](#run) the game!

## Class Diagram
To understand how all the entities have concepts in common:
![ClassDiagram](./diagrams/SimpleClassDiagram.png)

## Authors
* **Igor Lirussi** @ BOUN Boğaziçi University - CoLoRs Lab

## License
This project is licensed under License - see the [LICENSE](LICENSE) file for details

### Useful Resources

For starting, and to understand the game loop:
 http://pygametutorials.wikidot.com/tutorials-basic

Design patterns and games in Python
 https://www.patternsgameprog.com/series/discover-python-and-patterns/

A complete Guide on Pygame and Python
 https://coderslegacy.com/python/pygame-tutorial-part-3/

Physics with spheres and radius collider
 http://www.youtube.com/watch?v=7AKatTpNSNQ&list=PLE3D1A71BB598FEF6

Sentdex calculates box boundaries (but only vertical)
 https://www.youtube.com/playlist?list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO

Simple Sidescrolling Shooter in Pygame (checking hardcoded distance between points)
 https://www.youtube.com/watch?v=MvQU2ZVfSOo

Checking the examples in the pygame repo
 https://github.com/pygame/pygame/blob/main/examples/aliens.py
 
Extra tutorials for scrolling bg, parallax, menu, and buttons
 https://github.com/russs123/pygame_tutorials
