from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=height) # create canvas widget for drawing graphics
       
        # fill=BOTH: lets the canvas expand to fill all available space horizontally and vertically inside its container.
        # expand=True: tells the geometry manager to allocate extra space to this widget when the window grows, so it actually gets that extra room to fill.
        # Together: when the window is resized, the canvas grows/shrinks in both directions. Without them, it would keep its requested size and might not stretch.
        self.__canvas.pack(fill=BOTH, expand=True) # so it's ready to be drawn
        
        self.__running = False

        # the close protocol (so clicking the window’s X calls the close method later): 
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        # needs to redraw all the graphics in the window
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
            )
