"""
/∗
∗ CSCI3180 Principles of Programming Languages
∗
∗ --- Declaration ---
∗
∗ I declare that the assignment here submitted is original except for source
∗ material explicitly acknowledged. I also acknowledge that I am aware of
∗ University policy and regulations on honesty in academic work, and of the
∗ disciplinary guidelines and procedures applicable to breaches of such policy
∗ and regulations, as contained in the website
∗ http://www.cuhk.edu.hk/policy/academichonesty/
∗
∗ Assignment 2
∗ Name : Yoo Hyun Jun
∗ Student ID : 1155100531
∗ Email Addr : hjyoo8@cse.cuhk.edu.hk
∗/
"""
from xml.etree import ElementInclude
from Cell import Cell


class Map:
    def __init__(self, rows, cols):
        self._rows = rows #height
        self._cols = cols #width
        self._cells = [[Cell() for x in range(cols)] for y in range(rows)]
    
    #TODO: rows getter
    def get_rows(self):
        
        return self._rows
    
    #TODO: cols getter
    def get_cols(self):
        return self._cols
    
    def get_cell(self, row, col):
        # TODO: check whether the position is out of boundary 
        #       if not, return the cell at (row, col)
        #       return None otherwise
        if row >= self._rows or col >= self._cols or row < 0 or col < 0: 
            print("\033[1;31;46mNext move is out of boundary!\033[0;0m")
            return None
        
        else:
            # return a cell
            
            return self._cells[row][col]
        # END TODO 

    def build_cell(self, row, col, cell):
        # TODO: check whether the position is out of boundary 
        #       if not, add a cell (row, col) and return True
        #       return False otherwise 
        if row > self._rows or col > self._cols or row < 0 or col < 0: 
            print("\033[1;31;46mThe position (%d, %d) is out of boundary!\033[0;0m" %(row, col))
            return False 
        else:
            self._cells[row][col] = cell

            return True
            # return a cell 
        # END TODO

    # return a list of cells which are neighbours of cell (row, col) 
    def get_neighbours(self, row, col):
        return_cells = []
        # TODO: return a list of neighboring cells of cell (row, col)
        if row-1 >= 0 and col-1 >= 0:
            return_cells.append(self.get_cell(row-1,col-1))
        if row-1 >= 0:
            return_cells.append(self.get_cell(row-1,col))
        if row-1 >= 0 and col+1 < self._cols:
            return_cells.append(self.get_cell(row-1,col+1))
        if col-1 >= 0:
            return_cells.append(self.get_cell(row,col-1))
        if col+1 < self._cols:
            return_cells.append(self.get_cell(row,col+1))
        if row+1 < self._rows and col-1 >=0:
            return_cells.append(self.get_cell(row+1,col-1))
        if row+1 < self._rows:
            return_cells.append(self.get_cell(row+1,col))
        if row+1 < self._rows and col+1 < self._cols:
            return_cells.append(self.get_cell(row+1,col+1))
        return return_cells
        # END TODO
        

    def display(self):
        # TODO: print the map by calling diplay of each cell
        print("  ", end = " ")
        for i in range(self._cols):
            print("{0}    ".format(i), end = " ")
        print()
        for i in range(self._rows):
            print("{0} ".format(i),end = "")
            for j in range(self._cols):
                    self._cells[i][j].display()
                    #print("\033[0m", end = " ")
                    if j == self._cols - 1:
                        print()
            print()
        
        return True      
        # END TODO
