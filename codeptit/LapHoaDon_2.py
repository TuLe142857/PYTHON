from datetime import date as Date
import datetime

def toDate(text):
	date_object = datetime.strptime(text, "%d/%m/%Y")
	return date_object.date()

class Customer:
	def __init__(self, name, roomID, checkin, checkout, extraCost):
		self.name = name
		self.roomID = roomID
		self.checkin = checkin
		self.checkout = checkout
		self.extraCost = extraCost

	def getDaysStayed(self):
		d = checkout - checkin
		return d.days + 1

	def totalCost(self):
		return 
