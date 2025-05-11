from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width: int, height: int):
        # Root variables
        self.__root = Tk()
        self.__root.title("Python Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        # Canvas variables
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        # Is Running
        self.__running = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self) -> None:
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas: Canvas, fill_color: str = "black") -> None:
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)


class Cell:
    def __init__(self):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = 0
        self._x2 = 0
        self._y1 = 0
        self._y2 = 0

    def draw(self, canvas: Canvas, x1, y1, x2, y2) -> None:
        if self.has_left_wall:
            canvas.create_line(x1, y1)
        if self.has_right_wall:

        if self.has_top_wall:

        if self.has_bottom_wall:
