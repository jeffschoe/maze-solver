from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)

    # cell tests
    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(300, 300, 500, 500)

    """
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

    """

    """
    # raw lines test
    p1 = Point(50, 50)
    p2 = Point(300, 500)
    line1 = Line(p1, p2)
    win.draw_line(line1, "red")

    p3 = Point(100, 200)
    p4 = Point(500, 400)
    line2 = Line(p3, p4)
    win.draw_line(line2, "blue")
    """
    



    win.wait_for_close()


if __name__ == "__main__": # evaluates to TRUE if this script/file is run directly, so code below executes. If you import it to something else, this will be FALSE, so code below will not run automatically
    main() # main function gets executed