# Duck Typing
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
class Trap:
    def __init__(self, row, col):
        self._row = row
        self._col = col
        self._occupying = None
        self._name = "Trap"

    # TODO: _occupying get and setter
    def get_occupying(self):
        return self._occupying
    def set_occupying(self, obj):
        self._occupying = obj
        return True

    # TODO: _name getter
    def get_name(self):
        return self._name

    def interact_with(self, comer):
        # TODO: Add game logic.
        self._occupying.remove_occupant()
        if comer.get_name() == "Goblin":
            print("\033[1;31;43mA goblin entered a trap at (%d, %d)and died.\033[0;0m" % (self._row, self._col))
            # TODO: Add game logic.
            comer.set_active(False)
            return False

        elif comer.get_name() == "Player":
            print("\033[1;31;43mYou entered a trap at (%d, %d)! HP - 1.\033[0;0m" % (self._row, self._col))
            # TODO: Add game logic.
            comer._hp = comer.get_hp() - 1
            comer._oxygen = comer.get_oxygen() - 1
            return True
        else:
            return False

    def display(self):
        # TODO: Add display logic.
        print("\033[2;97m ", end = " ")
        
     
