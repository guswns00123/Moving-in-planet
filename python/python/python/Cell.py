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
from abc import abstractmethod

class Cell:
    def __init__(self, row=0, col=0):
        self._row = row
        self._col = col
        self._occupant = None
        self._color = None 
        self._hours = 0
    
    # TODO: hours getter
    def get_hours(self):
        return self._hours
    
    def set_occupant(self, obj):
        # TODO: set occupant for the Plain cell 
        #       return whether success or not
        if self.occupant == None or self.occupant.interact_with(obj):
            self._occupant = obj
            return True
        else:
            return False

  
        # END TODO

    def remove_occupant(self):
        # TODO: remove the occupant 
        self._occupant = None
        # END TODO

    @property 
    def occupant(self):
        return self._occupant

    def display(self):
        # TODO: print a string to display the cell 
        #       and the occupant in the cell 
        if self.occupant != None:
            if self.occupant.get_name() == "Trap":
                #print(1)
                print("{0}   \033[0m   ".format(self._color), end = "")
            elif self.occupant.get_name() == "Goblin" or "Player":
                print("{0} {1}{2} \033[0m   ".format(self._color, self._occupant.display(), self._color), end = "")
            
                #print("{0}   \033[0m   ".format(self._color), end = " ")
                #self._occupant.display()
                #print("{0} {1}{2} \033[0m   ".format(self._color, self._occupant.display(), self._color), end = " ")
        else:
            print("{0}   \033[0m   ".format(self._color), end = "")
        # END TODO

class Plain(Cell):
    def __init__(self, row, col):
        Cell.__init__(self, row, col)
        self._color = '\033[1;32;42m'
        self._hours = 1

class Mountain(Cell):
    def __init__(self, row, col):
        Cell.__init__(self, row, col)
        self._color = '\033[1;37;47m'

    def set_occupant(self, obj):
        # TODO: return False
        self._occupant = None
        return False
        # END TODO
    
class Swamp(Cell):
    def __init__(self, row, col):
        Cell.__init__(self, row, col)
        self._color = '\033[1;34;44m'
        self._hours = 2
