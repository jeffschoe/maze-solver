from graphics import Window
from cell import Cell

def draw_cell(win, x1, y1, x2, y2, walls):
    c = Cell(win)
    c.has_top_wall = walls.get("top", True)
    c.has_right_wall = walls.get("right", True)
    c.has_bottom_wall = walls.get("bottom", True)
    c.has_left_wall = walls.get("left", True)
    c.draw(x1, y1, x2, y2)

def main():
    win = Window(420, 420)
    size = 100
    margin = 20

    # Row 0
    draw_cell(win, margin, margin, margin+size, margin+size,
              {"top": True, "right": True, "bottom": True, "left": True})
    draw_cell(win, margin+size, margin, margin+2*size, margin+size,
              {"top": False, "right": True, "bottom": True, "left": True})

    # Row 1
    draw_cell(win, margin, margin+size, margin+size, margin+2*size,
              {"top": True, "right": True, "bottom": True, "left": False})
    # Reversed inputs on purpose (tests normalization)
    draw_cell(win, margin+2*size, margin+2*size, margin+size, margin+size,
              {"top": True, "right": False, "bottom": False, "left": True})

    # Non-square cell
    draw_cell(win, 250, 50, 380, 140,
              {"top": True, "right": True, "bottom": True, "left": True})

    win.wait_for_close()

if __name__ == "__main__":
    main()