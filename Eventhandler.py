from tkinter import Tk
window = Tk()

def handle_keypass(event):
    print(event.char)

window.bind("<Key>", handle_keypass)
window.mainloop()