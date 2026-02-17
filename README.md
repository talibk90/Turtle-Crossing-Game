# Turtle Crossing Game

A classic arcade-style game recreated in Python using the Turtle module. Help the turtle cross the busy road without getting hit by cars!

![Turtle Game Demo](TurtleGame.gif)


## How to Play
- **Move Up**: Press the `Up Arrow` key.
- **Restart**: If you crash, press `R` to restart the game immediately.
- **Goal**: Reach the top of the screen to level up and increase the game speed.

## Features
- **Endless Levels**: The game gets faster and harder with each successful crossing.
- **Score Tracking**: Displays your current level.
- **Restart Mechanism**: No need to restart the program; just press 'R' to try again!
- **Sound Effects**: Includes collision sounds.

## Requirements
- Python 3.x
- `turtle` module (included in standard Python library)
- `winsound` module (Windows specific, for sound effects)

## How to Run
1.  Clone the repository.
2.  Navigate to the project folder.
3.  Run the game:
    ```bash
    python main.py
    ```

## Recent Fixes & Updates
- **Fixed Bug**: Player position logic now correctly resets after completing a level.
- **Fixed Bug**: Score no longer updates continuously on the finish line.
- **New Feature**: Added functionality to restart the game by pressing 'R' after a "Game Over".
