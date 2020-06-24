from tkinter import *
from PIL import ImageTk,Image
myApp = Tk()

canvas = Canvas(myApp,width = 640, height = 360)
canvas.pack

background_image = ImageTk.PhotoImage(Image.open("C:/Users/risha/Downloads/Background.png"))
label = Label(image = background_image)
label.pack()

searchButton = Button(myApp,text = "Get Sentiment")
searchButton.pack()
myApp.mainloop()