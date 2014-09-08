from Tkinter import *
import Tkinter
import tkMessageBox
import TypeGUI

rating_level = {}


def get_rating_level():
	return rating_level


def processPricing(ratingVar, top):
    #Transition to the next option which is the input for cuisine type
    if ratingVar.get() != 0:
    	rating = ratingVar.get()
    	rating_level['level'] = rating
    	top.destroy()
    	TypeGUI.main()
    else:
    	tkMessageBox.showinfo("Error", "You didn't select a rating")

def build_gui():
	top = Tkinter.Tk()
	ratingVar = IntVar()

	welcomeMsg = Text(top, height = 1, width = 30)
	welcomeMsg.insert(INSERT, "Welcome to Food Roulette: ")
	welcomeMsg.pack()
	priceOption = Text(top, height = 1, width = 30)
	priceOption.insert(END, "Choose a rating")
	priceOption.pack()

	R1 = Radiobutton(top, text = "Rating: *", variable=ratingVar, value=1)
	R1.pack(anchor = W)
	R2 = Radiobutton(top, text = "Rating: **", variable=ratingVar, value=2)
	R2.pack(anchor = W)
	R3 = Radiobutton(top, text = "Rating: ***", variable=ratingVar, value=3)
	R3.pack(anchor = W)
	R4 = Radiobutton(top, text = "Rating: ****", variable=ratingVar, value=4)
	R4.pack(anchor = W)
	R5 = Radiobutton(top, text = "Rating: *****", variable=ratingVar, value=5)
	R5.pack(anchor = W)

	doneButton = Tkinter.Button(top, text = "Done", command = lambda: processPricing(ratingVar, top))
	doneButton.pack()

	top.mainloop()


def main():
	build_gui()


if __name__ == "__main__":
	main()