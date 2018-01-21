from activity import *
from keywatcher import *
from displaycontroller import *

class Core () :
	def __init__(self):	
		print("New Core")
		self.myActivity = showTimeActivity()

		self.keyWatcher = KeyWatcher(1,"keyWatcherThread")
		self.keyWatcher.addTarget(self)

		self.displayController = DisplayController(2,"displayThread")


	def keyPressed(self, button):
		self.myActivity.reactToButton(button)
		if button == 27:
			self.exit()

	def displayString(self, string):
		self.displaycontroller.setDisplayString(string)

	@property
	def myActivity(self):
		return self._myActivity

	@myActivity.setter
	def myActivity(self,activity):
		activity.core = self
		self._myActivity = activity

	def start(self):
		self.keyWatcher.start()
		self.displayController.start()
		self.displayController.join()

	def exit(self):
		self.displayController.exit()
		self.keyWatcher.exit()