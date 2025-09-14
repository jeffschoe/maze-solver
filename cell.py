from graphics import Line, Point




class Cell:
    """
    Our maze is made up of little boxes in a grid. Each box we call a "Cell", and it has 4 potential walls. 
    The way the maze works, is that we start in one cell, and we're allowed to move to an adjacent cell 
    as long as there isn't a wall in the way.

    This Cell class that holds all the data about an individual cell. 
    It knows which walls it has, where it exists on the canvas in x/y coordinates, 
    and has access to the window so that it can draw itself.
    """

    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win

    def draw(self, x1, y1, x2, y2): # updates the cell's internal x/y coordinates, and draws itself on the canvas.
        # normalize the values...(cont below)
        left = min(x1, x2)
        right = max(x1, x2)
        top = min(y1, y2) # opposite of Cartesian graph
        bottom = max(y1, y2) # opposite of Cartesian graph

        # (cont) ... so that we can always be sure x1, y1 is top-left and x2, y2 is bottom-right 
        self.__x1 = left
        self.__y1 = top
        self.__x2 = right
        self.__y2 = bottom

        left_top_corner = Point(self.__x1, self.__y1)
        right_top_corner = Point(self.__x2, self.__y1)
        left_bottom_corner = Point(self.__x1, self.__y2)
        right_bottom_corner = Point(self.__x2, self.__y2)

        top_line = Line(left_top_corner, right_top_corner)
        bottom_line = Line(left_bottom_corner, right_bottom_corner)
        left_line = Line(left_top_corner, left_bottom_corner)
        right_line = Line(right_top_corner, right_bottom_corner)
            
        if self.has_top_wall:
            self.__win.draw_line(top_line, "black")
        if self.has_bottom_wall:
            self.__win.draw_line(bottom_line, "black")
        if self.has_left_wall:
            self.__win.draw_line(left_line, "black")
        if self.has_right_wall:
            self.__win.draw_line(right_line, "black")