from window import Point, Line, Square
import time
import random

class Conway():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
    ):
        self._cells = []
        self._alive_cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        self.seed = seed if seed else random.seed(seed) 


    def _create_cells(self):
        if self._num_rows < 1 or self._num_cols < 1:
            raise ValueError('Number of rows and columns needs to be a positive integer')
        if self._cell_size_x < 1 or self._cell_size_y < 1:
            raise ValueError('Size of cells needs to be a positive integer')
        for col in range(self._num_cols):
            col_cells = []
            for row in range(self._num_rows):
                a_cell = Cell(self._win)
                a_cell.alive = random.choices([True, False], weights=[0.08, 0.92])[0]
                if a_cell.alive:
                    self._alive_cells.append((col,row))
                col_cells.append(a_cell)
            self._cells.append(col_cells)
        
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._set_cell(col, row)
                self._fill_cell(col, row)
                self._draw_cell(col, row)

        
    def start_game(self):
        while True:
            for col, row in self._check_alive_cell():
                self._fill_cell(col, row)
                self._draw_cell(col, row)
            self._animate()
    
    def _draw_cell(self, i, j):
        self._cells[i][j].draw()

    def _fill_cell(self, i, j):
        if self._cells[i][j].alive:
            self._cells[i][j].fill('#5EAF33')
        else:
            self._cells[i][j].fill()
    
    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        time.sleep(0.10)
    
    def _set_cell(self, i, j):
        x1 = self._x1 + (self._cell_size_x * i),
        y1 = self._y1 + (self._cell_size_y * j),
        x2 = self._x1 + (self._cell_size_x * (i + 1)),
        y2 = self._y1 + (self._cell_size_y * (j + 1)),
        self._cells[i][j].set(x1, y1, x2, y2)

    
    def _check_alive_cell(self):
        lst = []
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                neighbours = 0
                directions = [(col-1, row), (col-1, row-1), (col, row-1), (col+1, row-1), (col+1, row), (col+1, row+1), (col, row+1), (col-1, row+1)]
                for new_col, new_row in directions:
                    if new_col >= 0 and new_col < self._num_cols and new_row >= 0 and new_row < self._num_rows:
                        if self._cells[new_col][new_row].alive:
                                neighbours +=1
                if self._cells[col][row].alive:
                    if neighbours < 2 or neighbours > 3:
                        self._cells[col][row].alive = False
                        lst.append((col, row))
                    else:
                        lst.append((col, row))
                else:
                    if neighbours == 3:
                        self._cells[col][row].alive = True
                        lst.append((col, row))
        return lst
    

    def __repr__(self):
        print_statement = ''
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                print_statement += f"{self._cells[i][j]},"
            print_statement += "\n"
        return print_statement
        
 
class Cell():
    def __init__(self, window=None):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window
        self.alive = False
    
    def set(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def draw(self, fill_collor='black'):
        if not self._win:
            return

        if not self._x1 and not self._x2 and not self._y1 and not self._y2:
            return

        point_tl = Point(self._x1, self._y1)
        point_tr = Point(self._x2, self._y1)
        point_bl = Point(self._x1, self._y2)
        point_br = Point(self._x2, self._y2)

        left_line = Line(point_tl, point_bl)
        right_line = Line(point_tr, point_br)
        top_line = Line(point_tl, point_tr)
        bottom_line = Line(point_bl, point_br)

        self._win.draw_line(left_line, fill_collor)
        self._win.draw_line(right_line, fill_collor)
        self._win.draw_line(top_line, fill_collor)
        self._win.draw_line(bottom_line, fill_collor)
    
    def fill(self, fill_color='#d9d9d9'):
        if not self._win:
            return
        if not self._x1 and not self._x2 and not self._y1 and not self._y2:
            return

        point_tl = Point(self._x1, self._y1)
        point_br = Point(self._x2, self._y2)
        square = Square(point_tl, point_br)
        self._win.draw_rectangle(square, fill_color)
    
    def __repr__(self):
        return '1' if self.alive else '0'
