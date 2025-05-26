import time
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
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_columns = num_columns
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = [[None for _ in range(num_rows)] for _ in range(num_columns)]
        self.__create_cells()

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
        self.animate()

    def animate(self):
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
        
