from tkinter import *
from tkinter import filedialog
import os
from PIL import Image
from PIL import ImageDraw
import pathlib


WIDTH = 256
HEIGHT = 256

class MyPaint():
    
    paint_filetypes = [('all files', '.*'), ('JPEG Files', '.jpg')]
    
    def __init__(self, window, canvas, width, height):
        self.window = window
        self.width = width
        self.height = height
        self.canvas = canvas
        self.img = Image.new("RGB", (width, height), "white")
        self.draw = draw = ImageDraw.Draw(self.img)
        
    def clear_canvas(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, self.width, self.height],
                          fill = (255, 255, 255, 255))
    
    def save_canvas(self):
        fname = filedialog.asksaveasfilename(parent = self.window,
                                             initialdir = os.getcwd(),
                                             title = "Filename for saving the image:",
                                             filetypes = MyPaint.paint_filetypes)
        self.img.save(fname, format="jpeg")

    def paint(self, event):
        x1, y1 = ( event.x - 1 ), ( event.y - 1 )
        x2, y2 = ( event.x + 1 ), ( event.y + 1 )
        self.canvas.create_line(x1, y1, x2, y2, width = 5, capstyle=ROUND, smooth=TRUE, fill = "black")
        self.draw.line([x1, y1, x2, y2], width = 10, fill = "black")
        
    def exit_loop(self):
        self.window.destroy()

master = Tk()
master.title("Paiting BMP")
canvas = Canvas(master, width = WIDTH, height = HEIGHT)
canvas.pack(expand = YES, fill = BOTH)

mypaintapp = MyPaint(master, canvas, WIDTH, HEIGHT)
canvas.bind( "<B1-Motion>", mypaintapp.paint)

pane = Frame(master) 
pane.pack(fill = BOTH, expand = True) 

clear_button = Button(pane, text = "Clear", command = mypaintapp.clear_canvas)
clear_button.pack(side = LEFT, expand = True, fill = BOTH)

save_button = Button(pane, text = "Save", command = mypaintapp.save_canvas)
save_button.pack(side = LEFT, expand = True, fill = BOTH)

exit_button = Button(pane, text = "Exit", command = mypaintapp.exit_loop)
exit_button.pack(side = LEFT, expand = True, fill = BOTH)

message = Label(master, text = "Press and Drag the mouse to draw")
message.pack(side = BOTTOM)

mainloop()
