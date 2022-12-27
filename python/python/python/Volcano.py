from Cell import Mountain 
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
class Volcano(Mountain):
	def __init__(self, row, col, freq):
		Mountain.__init__(self, row, col)
		self._countdown = freq 
		self._frequency = freq
		self._color = '\u001b[41m'
		self._active = True 

	# TODO: _active getter
	def get_active(self):
		return self._active

	def act(self, map):
		# TODO:
		self._countdown -=1
		if self._countdown == 0:
			print("\033[1;33;41mVolcano erupts! \033[0;0m")
			self._countdown = self._frequency
			cells = map.get_neighbours(self._row, self._col)
			for i in range(len(cells)):
				occ = cells[i].occupant
				if occ != None:
					if occ._name == "Goblin":
						occ.set_active(False)
						occ.get_occupying().remove_occupant()
					elif occ._name == "Player":
						occ.set_hp(occ.get_hp() - 1)


			
        	# add game logic 
        # END TODO 
	

	def display(self):
		# TODO: return a string representing the Volcano 
		print("{0} \033[2;97m{1}{2} \033[0m   ".format(self._color, self._countdown, self._color), end = "")
        # END TODO 
