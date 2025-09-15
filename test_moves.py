from graphics import Window
from cell import Cell

import time

def draw_cell(win, x1, y1, x2, y2, walls):
    c = Cell(win)
    c.has_top_wall = walls.get("top", True)
    c.has_right_wall = walls.get("right", True)
    c.has_bottom_wall = walls.get("bottom", True)
    c.has_left_wall = walls.get("left", True)
    c.draw(x1, y1, x2, y2)
    return c

def main():
    win = Window(420, 420)
    size = 100
    margin = 20

    win.redraw()
    time.sleep(0.5)
    # Row 0
    c1 = draw_cell(win, margin, margin, margin+size, margin+size,
              {"top": True, "right": True, "bottom": True, "left": True})
    
    win.redraw()
    time.sleep(0.5)
    c2 = draw_cell(win, margin+size, margin, margin+2*size, margin+size,
              {"top": False, "right": True, "bottom": True, "left": True})

    win.redraw()
    time.sleep(0.5)
    # Row 1
    c3 = draw_cell(win, margin, margin+size, margin+size, margin+2*size,
              {"top": True, "right": True, "bottom": True, "left": False})
    
    win.redraw()
    time.sleep(0.5)
    c1.draw_move(c2)
    win.redraw()
    time.sleep(0.5)
    c2.draw_move(c3, True)
    




    win.wait_for_close()

if __name__ == "__main__":
    main()