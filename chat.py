import os
import keyboard
import time
from enum import Enum

class Direction(Enum):
    UP = "w"
    DOWN = "s"
    LEFT = "a"
    RIGHT = "d"

class Maze:
    def __init__(self):
        # Initialization code

    def is_in_bound(self, y, x):
        # Check if position is within bounds

    def print_maze(self):
        # Print maze

    def print_end(self):
        # Print end message

    def move(self, direction):
        # Move player based on the direction
        # Returns True if the game should continue, False if it's over

    def solve_maze(self):
        # Automatic solver using depth-first search
        visited = [[False for _ in range(len(self.maze[0]))] for _ in range(len(self.maze))]
        self.depth_first_search(self.ply, visited)

    def depth_first_search(self, current_pos, visited):
        if not self.is_in_bound(current_pos.y, current_pos.x) or visited[current_pos.y][current_pos.x]:
            return False

        visited[current_pos.y][current_pos.x] = True
        self.maze[current_pos.y][current_pos.x] = "P"
        self.print_maze()
        time.sleep(0.25)

        if current_pos == self.end:
            self.print_end()
            return True

        for direction in Direction:
            next_pos = self.get_next_position(current_pos, direction)
            if self.depth_first_search(next_pos, visited):
                return True

        self.maze[current_pos.y][current_pos.x] = " "
        return False

    def get_next_position(self, current_pos, direction):
        if direction == Direction.UP:
            return Pos(current_pos.y - 1, current_pos.x)
        elif direction == Direction.DOWN:
            return Pos(current_pos.y + 1, current_pos.x)
        elif direction == Direction.LEFT:
            return Pos(current_pos.y, current_pos.x - 1)
        elif direction == Direction.RIGHT:
            return Pos(current_pos.y, current_pos.x + 1)

if __name__ == '__main__':
    maze_game = Maze()
    maze_game.print_maze()

    while True:
        if keyboard.is_pressed("q"):
            print("Quit Program")
            break

        if keyboard.is_pressed("a"):
            maze_game.solve_maze()
            break
