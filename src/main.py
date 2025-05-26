from window import Window

from maze import Maze

def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 5, 5, 50, 50, win)
    maze._Maze__break_entrace_and_exit()

    win.wait_for_close()


if __name__ == '__main__':
    main()