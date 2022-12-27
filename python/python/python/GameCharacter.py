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


class GameCharacter:
    def __init__(self, row, col):
        self._row = row
        self._col = col
        self._occupying = None
        self._name = None
        self._active = True
        self._character = None 
        self._color = "\033[1;31m"
    
    #TODO: name getter
    def get_name(self):
        return self._name
    
    #TODO: row getter
    def get_row(self):
        return self._row

    #TODO: col getter
    def get_col(self):
        return self._col
    
    #TODO: active getter and setter
    def get_active(self):
        return self._active
    
    def set_active(self, active):
        self._active = active

    #TODO: occupying getter and setter
    def get_occupying(self):
        return self._occupying

    def set_occupying(self, occupying): #which cell
        self._occupying = occupying
    

    def cmd_to_pos(self, char):
        next_pos = [self._row, self._col]
        if char == "L":
            next_pos[1] -= 1
        elif char == "R":
            next_pos[1] += 1
        elif char == "U":
            next_pos[0] -= 1
        elif char == "D":
            next_pos[0] += 1
        
        return next_pos
    
    def display(self):
        # TODO: return _color followed by _character for displaying
        if self._character == None:
            return None
        else:
            return self._color + self._character 
        # END TODO 


    @abstractmethod
    def act(self, map):
        pass

    @abstractmethod
    def interact_with(self, comer):
        pass




class Player(GameCharacter):
    def __init__(self, row, col, hp=10, oxygen=10):
        GameCharacter.__init__(self, row, col)
        self._valid_actions = ["U", "D", "R", "L"]
        self._hp = hp
        self._oxygen = oxygen
        self._name = "Player"
        self._character = "A"

    #TODO: hp getter and setter
    def get_hp(self):
        return self._hp
    def set_hp(self, hp):
        self._hp = hp


    #TODO: oxygen getter and setter
    def get_oxygen(self):
        return self._oxygen
    def set_oxygen(self, oxygen):
        self._oxygen = oxygen

    def act(self, map):
        next_cell = None
        next_pos = [0, 0]
        flag = 0
        while next_cell == None:
                action = input("Next move (U, D, R, L): ".format(self._row, self._col))
                # TODO: act method               
                next_pos = self.cmd_to_pos(action)
                if action not in self._valid_actions:
                    print("Invalid command. Please enter one of {U, D, R, L}.") #a part
                    continue
                
                next_cell = map.get_cell(next_pos[0], next_pos[1])
                
                if next_cell != None and next_cell.set_occupant(self):
                    self._row = next_pos[0]
                    self._col = next_pos[1]
                    self._oxygen = self._oxygen - self.get_occupying().get_hours()
                    self.get_occupying().remove_occupant()
                    self.set_occupying(next_cell)
             #c part
                else:
                    next_cell = None   
            
            
                    
        if self._active == False:
            map.get_cell(self._row, self._col).remove_occupant()
            
            
            # END TODO 

   # return whether comer entering the cell successfully
    def interact_with(self, comer):
        if comer._name == "Goblin":
           # print(comer._active)
            print('\033[1;31;46mPlayer meets a Goblin! Player\'s HP - %d.\033[0m' %(comer._damage))
             # TODO: interact_with method 
            self._hp -= comer.get_damage()
            comer.set_active(False)
            return False
            
            # END TODO 


class Goblin(GameCharacter):
    def __init__(self, row, col, actions):
        GameCharacter.__init__(self, row, col)
        self._actions = actions
        self._cur_act = 0
        self._damage = 1
        self._name = "Goblin"
        self._character = "G"

    #TODO: damage getter
    def get_damage(self):
        return self._damage

    def act(self, map):
        # TODO: act method of a Goblin 
        # get the next cell according to _actions and _cur_act
        next_cell = None
        next_pos = [0,0]
        next_pos = self.cmd_to_pos(self._actions[self._cur_act])

        self._cur_act += 1
        if self._cur_act == len(self._actions):
            self._cur_act = 0

        next_cell = map.get_cell(next_pos[0], next_pos[1]) 
    
        if next_cell != None and next_cell.set_occupant(self):
            self._row = next_pos[0]
            self._col = next_pos[1]
            self.get_occupying().remove_occupant()
            self.set_occupying(next_cell)
            print("\033[1;31;46mGoblin enters the cell (%d, %d).\033[0;0m" % (self._row, self._col))
                
        if self._active == False:
            map.get_cell(self._row, self._col).remove_occupant()
            print("\033[1;31;46mGoblin dies right after the movement.\033[0;0m")


        # END TODO 

    # return whether comer entering the cell successfully or not
    def interact_with(self, comer):
        if comer._name == "Player":
            print(
                "\033[1;31;46mA goblin at cell (%d, %d) meets Player. The goblin died. Player's HP - 1.\033[0;0m"
                % (self._row, self._col)
            )
            self.set_active(False)
            comer._hp -= self.get_damage()
                
                
            return True  
                
            # TODO: update properties of the player and the Goblin 
            #       return whether the Player successfully enter the cell 

            # END TODO

