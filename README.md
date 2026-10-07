# Grid Navigation Agent

## Description

This Python program demonstrates a simple **Grid Navigation Agent**. The agent starts from a starting position and moves through a 5×5 grid until it reaches the goal.

The agent avoids obstacles and follows a simple movement strategy:

1. Move **down** if the next position is valid.
2. Otherwise, move **right** if the next position is valid.
3. If neither movement is possible, the agent gets stuck.

The program also displays the grid after every movement and shows the complete path taken by the agent.

## Features

* 5×5 grid environment
* Defined start and goal positions
* Obstacles placed in the grid
* Agent movement and navigation
* Obstacle avoidance
* Valid position checking
* Displays the grid after each move
* Displays the complete path taken

## Grid Representation

The grid uses the following symbols:

* `S` → Starting position
* `G` → Goal position
* `A` → Current position of the agent
* `X` → Obstacle
* `.` → Empty space

## Initial Configuration

```text
Grid Size: 5×5

Start: (0,0)
Goal: (4,4)

Obstacles:
(1,2)
(2,2)
(3,2)
```

## How It Works

The program begins with the agent at the starting position `(0,0)`.

At every step, the agent checks:

### 1. Move Down

The program first checks whether the position below the agent is valid.

```python
if valid(x+1,y):
    agent=(x+1,y)
```

If the position is inside the grid and is not an obstacle, the agent moves down.

### 2. Move Right

If moving down is not possible, the agent checks the position to the right.

```python
elif valid(x,y+1):
    agent=(x,y+1)
```

If the position is valid, the agent moves right.

### 3. Agent Gets Stuck

If neither down nor right is possible, the program displays:

```text
AGENT IS STUCK!!!
```

and stops the movement.

## Valid Position Checking

The `valid()` function checks whether the agent can move to a particular position.

```python
def valid(x,y):
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and (x,y) not in OBSTACLES
```

It ensures that:

* The position is inside the grid.
* The position is not an obstacle.

## Example Path

For the given grid, the agent follows a path similar to:

```text
(0,0)
(1,0)
(2,0)
(3,0)
(4,0)
(4,1)
(4,2)
(4,3)
(4,4)
```

The agent successfully reaches the goal while avoiding the obstacles.

## Sample Grid

The initial grid looks like:

```text
A . . . .
. . X . .
. . X . .
. . X . .
. . . . G
```

Here:

* `A` is the agent.
* `G` is the goal.
* `X` represents obstacles.

## Technologies Used

* Python
* Basic conditional statements
* Functions
* Loops
* Tuples
* Lists

## How to Run

1. Install Python on your system.
2. Save the program as:

```text
grid_navigation.py
```

3. Open Command Prompt or Terminal.
4. Navigate to the folder containing the file.
5. Run:

```bash
python grid_navigation.py
```

## Learning Outcome

This program helps understand the basic concepts of:

* Artificial Intelligence agents
* Grid-based environments
* State representation
* Obstacle avoidance
* Rule-based decision making
* Path navigation
* Python functions and loops

## Conclusion

The Grid Navigation Agent is a simple example of an intelligent agent operating in an environment. It observes the available positions, avoids obstacles, chooses a valid movement, and continues until it reaches the goal or becomes stuck.
