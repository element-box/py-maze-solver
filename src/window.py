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

    def draw_line(self, line, fill_color="black"):
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
