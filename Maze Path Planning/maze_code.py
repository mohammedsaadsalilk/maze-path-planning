from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

# Function to preprocess the maze image
def preprocess_maze(image_path, threshold=128, margin=2):
    """
        Preprocesses the maze image by converting it to grayscale,
        thresholding to create a binary maze, and cropping the edges.

        Parameters:
            image_path: str, Path to the maze image file
            threshold: int, Pixel intensity threshold for binary conversion
            margin: int, Number of pixels to crop from the edges

        Returns:
            A 2D binary numpy array representing the maze (1: path, 0: wall)
        """

    maze_image = Image.open(image_path).convert("L")  # Convert to grayscale
    maze_array = np.array(maze_image)        # Convert image to numpy array
    binary_maze = (maze_array > threshold).astype(int)  # 1 = Free path, 0 = Wall
    return binary_maze[margin:-margin, margin:-margin]  # Crop margins

# Function to add clearance around walls
def add_wall_clearance(binary_maze, clearance=1):
    """
        Expands walls in the binary maze to create a buffer zone (clearance) around them.

        Parameters:
            binary_maze: 2D numpy array, The binary maze (1: path, 0: wall)
            clearance: int, Number of pixels for the buffer around walls

        Returns:
            A new 2D binary maze with added clearance around walls
        """

    padded_maze = binary_maze.copy()        # Copy the maze to avoid modifying the original
    rows, cols = binary_maze.shape          # Get dimensions of the maze
    for x in range(rows):                           # Iterate over each row
        for y in range(cols):                       # Iterate over each column
            if binary_maze[x, y] == 0:              # Wall
                # Add buffer around the wall
                for dx in range(-clearance, clearance + 1):
                    for dy in range(-clearance, clearance + 1):
                        nx, ny = x + dx, y + dy             # Calculate neighboring coordinates
                        if 0 <= nx < rows and 0 <= ny < cols:
                            padded_maze[nx, ny] = 0  # Mark as wall
    return padded_maze

# BFS function to find the shortest path
def bfs_solver(binary_maze, start, goal):
    """
        Finds the shortest path in the maze using Breadth-First Search (BFS).

        Parameters:
            binary_maze: 2D numpy array, The binary maze (1: path, 0: wall)
            start: tuple, Starting point in (row, col)
            goal: tuple, Goal point in (row, col)

        Returns:
            A list of tuples representing the shortest path from start to goal, or None if no path exists
        """

    rows, cols = binary_maze.shape          # Get maze dimensions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    queue = deque([start])              # Initialize queue with the starting point
    visited = set([start])              # Track visited cells
    parent = {}                         # Dictionary to reconstruct the path

    while queue:        # While there are cells to explore
        x, y = queue.popleft()      # Dequeue the current cell
        if (x, y) == goal:
            # Reconstruct path
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            return [(start)] + path[::-1]  # Reverse path to start-to-goal order
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and binary_maze[nx, ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))
    return None

# Function to plot the maze with the path
def plot_maze_with_path(maze, start, goal, path):
    """
        Plots the maze with the safe path, start, and goal points.

        Parameters:
            maze: 2D numpy array, The binary maze
            start: tuple, Starting point in (row, col)
            goal: tuple, Goal point in (row, col)
            path: list of tuples, The shortest path from start to goal
        """

    plt.figure(figsize=(7, 7))
    plt.imshow(maze, cmap="gray", origin="upper")

    # Plot the path
    if path:
        path_x, path_y = zip(*path)
        centered_x = [x + 0.5 for x in path_x]
        centered_y = [y + 0.5 for y in path_y]
        plt.plot(centered_y, centered_x, color="red", linewidth=2, label="Safe Path")
    else:
        print("No path found.")

    # Mark Start and Goal
    plt.plot(start[1] + 0.5, start[0] + 0.5, 'gx', markersize=15 , label='Start')
    plt.plot(goal[1] + 0.5, goal[0] + 0.5, 'bx', markersize=14, label='Goal')

    # Add labels
    plt.title("Maze with Safe Path (Clearance Added)")
    plt.axis('off')
    plt.legend()
    plt.gca().invert_yaxis()
    plt.show()

''' ############################################ '''

# Main Code
maze_path = "maze.png"   # Path to the maze image file
cropped_maze = preprocess_maze(maze_path)

# Define start and goal points
start = (400, 210)  # (row, col) for Start
goal = (5, 190)  # (row, col) for Goal

# Add clearance to the binary maze
clearance = 5  # Buffer size around walls
maze_with_clearance = add_wall_clearance(cropped_maze, clearance)

# Solve the maze
safe_path = bfs_solver(maze_with_clearance, start, goal)

# Plot the maze with the safe path
plot_maze_with_path(cropped_maze, start, goal, safe_path)
