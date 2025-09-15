from graphics import Window
from cell import Cell


def main():
    # more cell tests
    win = Window(300, 300)
    size = 100
    margin = 20

    cells = [
        (0, 0, {"top": True, "right": True, "bottom": True, "left": True}),
        (0, 1, {"top": False, "right": True, "bottom": True, "left": True}),
        (1, 0, {"top": True, "right": True, "bottom": True, "left": False}),
        (1, 1, {"top": True, "right": False, "bottom": False, "left": True}),
    ]

    for r, c, walls in cells:
        x1 = margin + c * size
        y1 = margin + r * size
        x2 = x1 + size
        y2 = y1 + size

        cell = Cell(win)
        cell.has_top_wall = walls["top"]
        cell.has_right_wall = walls["right"]
        cell.has_bottom_wall = walls["bottom"]
        cell.has_left_wall = walls["left"]
        cell.draw(x1, y1, x2, y2)

   

    



    win.wait_for_close()


if __name__ == "__main__": # evaluates to TRUE if this script/file is run directly, so code below executes. If you import it to something else, this will be FALSE, so code below will not run automatically
    main() # main function gets executed