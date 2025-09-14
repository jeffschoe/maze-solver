from graphics import Window, Point, Line


def main():
    win = Window(800, 600)

    p1 = Point(50, 50)
    p2 = Point(300, 500)
    line1 = Line(p1, p2)
    win.draw_line(line1, "red")

    p3 = Point(100, 200)
    p4 = Point(500, 400)
    line2 = Line(p3, p4)
    win.draw_line(line2, "blue")

    win.wait_for_close()


if __name__ == "__main__": # evaluates to TRUE if this script/file is run directly, so code below executes. If you import it to something else, this will be FALSE, so code below will not run automatically
    main() # main function gets executed