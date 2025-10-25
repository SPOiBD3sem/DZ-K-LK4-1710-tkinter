from tkinter import *

root = Tk()
root.title("example Tkinter")    
root.geometry("900x700")    

label = Label(text="Hello, World!") 
label.pack()   

canvas = Canvas(bg="white", width=848, height=632)
canvas.pack(anchor=CENTER, expand=1)
 
globe_image = PhotoImage(file="globe.png")
 
canvas.create_image(1, 1, anchor=NW, image=globe_image)


root.mainloop()