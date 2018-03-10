from activity import *
from keywatcher import *
from displaycontroller import *

class Core () :
	def __init__(self):	
		print("New Core")
		self.myActivity = ShowTimeActivity()

		self.keyWatcher = KeyWatcher(1,"keyWatcherThread")
		self.keyWatcher.addTarget(self)

		self.displayController = DisplayController(2,"displayThread")


	def keyPressed(self, button):
		self.myActivity.reactToButton(button)
		if button == 27:
			self.exit()

	def displayString(self, string):
		self.displayController.setDisplayString(string)

	def displayAttributes(self, leftDot = None, rightDot = None, colon = None) :
		if not leftDot is None :
			self.displayController.leftDot = leftDot
		if not rightDot is None :
			self.displayController.rightDot = rightDot
		if not colon is None :
			self.displayController.colon = colon

	@property
	def myActivity(self):
		return self._myActivity

	@myActivity.setter
	def myActivity(self,activity):
		if hasattr(self, '_myActivity') :
			self._myActivity.exit()
		activity.core = self
		self._myActivity = activity

	def start(self):
		self.keyWatcher.start()
		self.displayController.start()
		self.displayController.join()

	def exit(self):
		self.myActivity.exit()
		self.displayController.exit()
		self.keyWatcher.exit()