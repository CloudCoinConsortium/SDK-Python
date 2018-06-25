from System.Threading.Tasks import *

class ICloudBankAccessable(object):
	def LoadKeysFromFile(self, filepath):
		pass

	def get_CloudBankUtils(self):

	CloudBankUtils = property(fget=get_CloudBankUtils)

class ICloudBankUtils(object):
	def get_onesInBank(self):

	onesInBank = property(fget=get_onesInBank)

	def get_fivesInBank(self):

	fivesInBank = property(fget=get_fivesInBank)

	def get_twentyFivesInBank(self):

	twentyFivesInBank = property(fget=get_twentyFivesInBank)

	def get_hundredsInBank(self):

	hundredsInBank = property(fget=get_hundredsInBank)

	def get_twohundredfiftiesInBank(self):

	twohundredfiftiesInBank = property(fget=get_twohundredfiftiesInBank)

	def showCoins(self):
		pass

	def loadStackFromFile(self, filepath):
		pass

	def saveStackToFile(self, filepath):
		pass

	def getStackName(self):
		pass

	def sendStackToCloudBank(self):
		pass

	def getStackFromCloudBank(self, amountToWithdraw):
		pass

	def getReceipt(self):
		pass

	def getReceiptFromCloudBank(self):
		pass

	def transferCloudCoins(self, toPublicKey, coinsToSend):
		pass

class IKeys(object):
	def get_publickey(self):

	def set_publickey(self, value):

	publickey = property(fget=get_publickey, fset=set_publickey)

INCOMPLETE 
