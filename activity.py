from core import *
import threading
import time

class Activity :
	def __init__(self) :
		print("New Activity")
		self.core = None

	def reactToButton(self, button) :
		print("Activity sees key: " +  str(button))

	def exit(self) :
		pass


#a timer, allows activities to update every x seconds.
class TimeKeeper(threading.Thread) :
	def __init__(self, threadID, name):
		super(TimeKeeper,self).__init__()
		self.threadID = threadID
		self.name = name
		self._exitFlag = False
		self.target = None
		self.sleepTime = 1

	def run(self) :
		print("Starting thread " + self.name)
		while not(self._exitFlag) :
			if not self.target is None :
				self.target.reactToTime()
			time.sleep(self.sleepTime)
			print("Sleepytime")
		print("Exiting thread " + self.name)

	def exit(self) :
		self._exitFlag = True
		print("ExitFlag set for " + self.name)


#activity that just shows the time, updates every second.
class ShowTimeActivity(Activity):
	def __init__(self) :
		super(ShowTimeActivity,self).__init__()
		self.colon = False
		# self.timeKeeper = TimeKeeper(3,'TimeKeeperThread')
		# self.timeKeeper.sleepTime = 1
		# self.timeKeeper.target = self
		# self.timeKeeper.start()

	def exit(self) :
		super(ShowTimeActivity,self).exit()
		# self.timeKeeper.exit()

	def reactToButton(self,button) :
		super(ShowTimeActivity,self).reactToButton(button)

	def reactToTime(self) :
		if not self.core is None :
			self.core.displayString(time.strftime("%H%M"))
			self.core.displayAttributes(colon = self.colon)
			self.colon = not self.colon