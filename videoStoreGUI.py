"""
Program: videoStoreGUI.py
Author:  Dominick  7/10/2023

GUI-based version of the Video Store project from chapter 2

NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports go here

# Class header (application name will change project to project)
class VideoStore(EasyFrame):
	# Definition of our class constructor method
	def __init__(self):
		# Call to the Easy Frame constructor method
		EasyFrame.__init__(self, title = "Five Star Video", width = 280, height = 220, resizable = False, background = "lightyellow")
		self.normalFont = Font(family = "Tahoma", size = 12)

		# Add the various components to the window
		self.addLabel(text = "Five Star Video", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "darkred", foreground = "lightyellow", font = Font(family = "Arial", size = 26))
		self.addLabel(text = "New Rentals: $3.00\n Old Rentals: $2.00", row = 1, column = 0, columnspan = 2, sticky = "NSEW", background = "lightyellow", font = self.normalFont)
		self.addLabel(text = "# of New Rentals:", row = 2, column = 0, sticky = "NE", background = "lightyellow", font = self.normalFont)
		self.newRentals = self.addIntegerField(value = 0, row = 2, column = 1, sticky = "NW", width = 4)
		self.addLabel(text = "# of Old Rentals:", row = 3, column = 0, sticky = "NE", background = "lightyellow", font = self.normalFont)
		self.oldRentals = self.addIntegerField(value = 0, row = 3, column = 1, sticky = "NW", width = 4)

		self.button = self.addButton(text = "Calculate Total", row = 4, column = 0, columnspan = 2, command = self.calculate)

		self.addLabel(text = "The total for the order is: ", row = 5, column = 0, sticky = "NE", background = "darkred", foreground = "white", font = self.normalFont)
		self.total = self.addFloatField(value = 0.0, row = 5, column = 1, sticky = "NW", precision = 2, state = "readonly", width = 10)

	# Definition of the calculate() function
	def calculate(self):
		# grab the user input from the GUI window
		new = self.newRentals.getNumber()
		old = self.oldRentals.getNumber()

		# processing phase
		result = (new * 3.00) + (old * 2.00)

		#output phase
		self.total.setNumber(result)

# Global definition of the main() method
def main():
	# Instantiate an object from the class into mainloop()
	VideoStore().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()