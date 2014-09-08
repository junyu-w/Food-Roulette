from Tkinter import *
import Tkinter
import tkMessageBox
import PriceGUI

food_type = {}

def get_food_type():
	return food_type

def backToPrice(top):
		top.destroy()
		PriceGUI.main()

def processType(foodVar, top):
		if foodVar.get() == 1:
			foodType = 'Chinese'
			top.destroy()
			food_type['type'] = 'Chinese'
		elif foodVar.get() == 2:
			foodType = 'Italian'
			top.destroy()
			food_type['type'] = 'Italian'
		elif foodVar.get() == 3:
			foodType = 'Korean'
			top.destroy()
			food_type['type'] = 'Korean'
		elif foodVar.get() == 4:
			foodType = 'Japanese'
			top.destroy()
			food_type['type'] = 'Japanese'
		elif foodVar.get() == 5:
			foodType ='Mexican'
			top.destroy()
			food_type['type'] = 'Mexican'
		else:
			foodType = OtherEntry.get()
			top.destroy()
			food_type['type'] = OtherEntry.get()

def build_gui():
	top = Tkinter.Tk()
	foodList = ['Chinese', 'Italian', 'Korean', 'Japanese', 'Mexican', 'Other']
	foodVar = IntVar()
	
	backButton = Tkinter.Button(top, text = "Back", command = lambda: backToPrice(top))
	backButton.pack(anchor = W)
	
	typeText = Text(top, height = 1, width = 32)
	typeText.insert(INSERT, "Now, choose a type of food: ")
	typeText.pack()
	#typeEntry = Entry(top, bd = 3)
	#ypeEntry.pack(anchor = W)
	R1 = Radiobutton(top, text=foodList[0:1], variable=foodVar, value=1)
	R1.pack(anchor = W)
	R2 = Radiobutton(top, text=foodList[1:2], variable=foodVar, value=2)
	R2.pack(anchor = W)
	R3 = Radiobutton(top, text=foodList[2:3], variable=foodVar, value=3)
	R3.pack(anchor = W)
	R4 = Radiobutton(top, text=foodList[3:4], variable=foodVar, value=4)
	R4.pack(anchor = W)
	R5 = Radiobutton(top, text=foodList[4:5], variable=foodVar, value=5)
	R5.pack(anchor = W)
	R6 = Radiobutton(top, text=foodList[5:6], variable=foodVar, value=6)
	R6.pack(anchor = W, side = LEFT)
	OtherEntry = Entry(top, bd = 5)
	OtherEntry.pack(side = LEFT)

	bottomframe = Frame(top)
	bottomframe.pack(side = BOTTOM)

	doneButton = Tkinter.Button(bottomframe, text = "Done", command = lambda: processType(foodVar, top))
	doneButton.pack(anchor = W, side = BOTTOM)

	top.mainloop()

def main():
	build_gui()


