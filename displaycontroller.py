import threading
import time

class DisplayController(threading.Thread):
	def __init__(self, threadID, name):
		super(DisplayController,self).__init__()
		self.threadID = threadID
		self.name = name
		self._exitFlag = False
		self._displayString = ""
		self._displayStringLock = threading.RLock()
	def run(self):
		print("Starting" + self.name)
		while not(self._exitFlag) :
			timeString = time.strftime("%H:%M:%S")
			dateString = time.strftime("%d-%m")
			self._displayStringLock.acquire()
			print(timeString + "  " + dateString + " : " + self._displayString)
			self._displayStringLock.release()
			time.sleep(1)
		print("Exiting thread " + self.name)

	def setDisplayString(self, displayString):
		self._displayStringLock.acquire()
		self._displayString = displayString
		self._displayStringLock.release()

	def exit(self) :
		self._exitFlag = True
		print("ExitFlag DisplayController set")