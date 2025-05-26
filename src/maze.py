import time
import random

from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_columns,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_columns = num_columns
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = [[None for _ in range(num_rows)] for _ in range(num_columns)]
        if seed:
            random.seed(seed)
        
        # Generate maze
        self.__create_cells()
        self.__break_entrace_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self):
        # fills in cells, 2D list/array of Cell objects
        # uses number of columns and rows to determine size
        for col in range(self.__num_columns):
            for row in range(self.__num_rows):
                self.__cells[col][row] = Cell(self.__win)
                self.__draw_cell(col, row)

    def __draw_cell(self, i, j):
        cell = self.__cells[i][j]
        cell_x1 = self.__x1 + (self.__cell_size_x * i)
        cell_y1 = self.__y1 + (self.__cell_size_y * j)
        cell_x2 = cell_x1 + self.__cell_size_x
        cell_y2 =  cell_y1 + self.__cell_size_y
        cell.draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self.__animate()

    def __animate(self):
        if self.__win == None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrace_and_exit(self):
        start_cell = self.__cells[0][0]
        end_cell = self.__cells[self.__num_columns - 1][self.__num_rows - 1]
        start_cell.has_top_wall = False
        end_cell.has_bottom_wall = False
        self.__draw_cell(0, 0)
        self.__draw_cell(self.__num_columns - 1, self.__num_rows - 1)
        
    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            not_visited = []
            if i > 0 and self.__cells[i - 1][j].visited == False:
                not_visited.append((i - 1, j))

            if i < self.__num_columns - 1 and self.__cells[i + 1][j].visited == False:
                not_visited.append((i + 1, j))
            
            if j > 0 and self.__cells[i][j - 1].visited == False:
                not_visited.append((i, j - 1))

            if j < self.__num_rows - 1 and self.__cells[i][j + 1].visited == False:
                not_visited.append((i, j + 1))
           
            if len(not_visited) == 0:
                self.__draw_cell(i,j)
                return
            next_cell_coords = random.choice(not_visited)
            next_cell_i = next_cell_coords[0]
            next_cell_j = next_cell_coords[1]
            
            # North
            if next_cell_i == i - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[next_cell_i][next_cell_j].has_bottom_wall = False
            # South
            if next_cell_i == i + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[next_cell_i][next_cell_j].has_top_wall = False
            # West
            if next_cell_j == j - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[next_cell_i][next_cell_j].has_right_wall = False
            
            # East
            if next_cell_j == j + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[next_cell_i][next_cell_j].has_left_wall = False
            
            self.__break_walls_r(next_cell_i, next_cell_j)
            
    def __reset_cells_visited(self):
        for col in self.__cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0,0)


    def _solve_r(self, i, j):
        self.__animate()

        # vist the current cell
        self.__cells[i][j].visited = True

        # if we are at the end cell, we are done!
        if i == self.__num_columns - 1 and j == self.__num_rows - 1:
            return True

        # move left if there is no wall and it hasn't been visited
        if (
            i > 0
            and not self.__cells[i][j].has_left_wall
            and not self.__cells[i - 1][j].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i - 1][j], True)

        # move right if there is no wall and it hasn't been visited
        if (
            i < self.__num_columns - 1
            and not self.__cells[i][j].has_right_wall
            and not self.__cells[i + 1][j].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i + 1][j], True)

        # move up if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self.__cells[i][j].has_top_wall
            and not self.__cells[i][j - 1].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j - 1], True)

        # move down if there is no wall and it hasn't been visited
        if (
            j < self.__num_rows - 1
            and not self.__cells[i][j].has_bottom_wall
            and not self.__cells[i][j + 1].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j + 1], True)

        # we went the wrong way let the previous cell know by returning False
        return False
