import getch
import threading

class KeyWatcher(threading.Thread):
	def __init__(self, threadID, name):
		super(KeyWatcher,self).__init__()
		self.threadID = threadID
		self.name = name
		self.lastKey = 0;
		self._targets = []
		self._targetsLock = threading.RLock()

	def run(self):
		print("Starting " + self.name)
		self._exitFlag = False
		while not(self._exitFlag) :
			keyPressed = ord(getch.getch())
			if keyPressed ==224 or keyPressed == 0:
				keyPressed =ord(getch.getch())
			self.lastKey = keyPressed
			if len(self._targets) > 0 :
				for target in self._targets :
					target.keyPressed(keyPressed)
		print("Exiting thread " + self.name)

	def addTarget(self, target):
		self._targetsLock.acquire()
		self._targets.append(target)
		self._targetsLock.release()

	def exit(self):
		self._exitFlag = True
		print("ExitFlag set for " + self.name)