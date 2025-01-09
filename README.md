# Maze Path Planning Using BFS

This project implements a solution for navigating a 2D maze using the Breadth-First Search (BFS) algorithm. It preprocesses a maze image, adds clearance around walls for safe navigation, computes the shortest path from a start point to a goal point, and visualizes the result.

## Features
- **Maze Preprocessing**: Converts a maze image into a binary representation.
- **Wall Clearance**: Adds a safety buffer around walls to prevent collisions.
- **Shortest Path Calculation**: Uses the BFS algorithm to compute the shortest path from the start to the goal.
- **Visualization**: Overlays the computed path on the maze for easy visualization.

## Requirements
- Python 3
- Libraries:
  - [Pillow](https://pillow.readthedocs.io/en/stable/)
  - [NumPy](https://numpy.org/)
  - [Matplotlib](https://matplotlib.org/)

## Installation
1. Clone the repository or download the source code.
2. Install the required Python libraries:
   ```bash
   pip install pillow numpy matplotlib
   ```
3. Place the maze image in the project directory (default: `maze.png`).

## Usage
1. Modify the `maze_path`, `start`, and `goal` variables in the script to specify the maze image and the start/goal coordinates.
2. Run the script:
   ```bash
   python maze_code.py
   ```
3. The result will be displayed as a plot, showing the shortest path in red and the start/goal points.

## Functions
### `preprocess_maze(image_path, threshold=128, margin=2)`
- Converts the maze image to grayscale, thresholds it to create a binary maze, and crops unnecessary margins.

### `add_wall_clearance(binary_maze, clearance=1)`
- Expands walls in the binary maze to create a safety buffer around obstacles.

### `bfs_solver(binary_maze, start, goal)`
- Finds the shortest path in the maze using the BFS algorithm.

### `plot_maze_with_path(maze, start, goal, path)`
- Visualizes the maze with the shortest path overlaid.

## Example
Input Maze:
![Maze](maze.png)

Output:
The BFS algorithm computes the shortest path from the start to the goal, and the result is visualized as:
![Maze Solution](maze_solution_visualization.png)

## References
- [Python Documentation](https://docs.python.org/3/)
- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Maze-Solving Algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Maze-solving_algorithm)
- [Breadth-First Search (Wikipedia)](https://en.wikipedia.org/wiki/Breadth-first_search)
