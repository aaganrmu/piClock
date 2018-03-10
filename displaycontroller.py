import threading
import time

class DisplayController(threading.Thread):
	def __init__(self, threadID, name):
		super(DisplayController,self).__init__()
		self.threadID = threadID
		self.name = name
		self._exitFlag = False
		self._displayString = "0000"
		self._displayStringLock = threading.RLock()
		self.leftDot = False;
		self.rightDot = False;
		self.colon = False;
	def run(self):
		print("Starting " + self.name)
		while not(self._exitFlag) :
			#timeString = time.strftime("%H:%M:%S")
			#dateString = time.strftime("%d-%m")
			if self.leftDot :
				leftDot = '.'
			else :
				leftDot = ' '
			
			if self.rightDot :
				rightDot = '.'
			else :
				rightDot = ' '
			
			if self.colon :
				colon = ":"
			else :
				colon = " "

			self._displayStringLock.acquire()
			#print(timeString + "  " + dateString + " : " + self._displayString)

			print(leftDot + self._displayString[0:2] + colon + self._displayString[2:4] + rightDot)
			self._displayStringLock.release()
			time.sleep(0.1)
		print("Exiting thread " + self.name)


	def setDisplayString(self, displayString):
		self._displayStringLock.acquire()
		self._displayString = displayString
		self._displayStringLock.release()

	def exit(self) :
		self._exitFlag = True
		print("ExitFlag set for " + self.name)