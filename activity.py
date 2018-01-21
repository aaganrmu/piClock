from core import *


class Activity :
	def __init__(self) :
		print("New Activity")
		self.core = []

	def reactToButton(self, button) :
		print(button)

class showTimeActivity(Activity):
	def __init__(self) :
		super(showTimeActivity,self).__init__()
		
	def reactToButton(self,button) :
		super(showTimeActivity,self).reactToButton(button)
