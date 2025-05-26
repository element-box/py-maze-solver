from window import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.__win is None:
            return
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line, "white")

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line, "white")

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line, "white")

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line, "white")
        

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        center_x = self.__x1 + abs(self.__x2 - self.__x1) // 2
        center_y = self.__y1 + abs(self.__y2 - self.__y1) // 2
        center = Point(center_x, center_y)
        center_other_x = to_cell.__x1 + abs(to_cell.__x2 - to_cell.__x1) // 2
        center_other_y = to_cell.__y1 + abs(to_cell.__y2 - to_cell.__y1) // 2
        center_other = Point(center_other_x, center_other_y)

        line = Line(center, center_other)
        self.__win.draw_line(line, color)