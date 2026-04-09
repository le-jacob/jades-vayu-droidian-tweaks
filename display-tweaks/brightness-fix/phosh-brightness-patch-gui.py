import tkinter, os, tkinter.ttk

#Configuration
file_path = "/tmp/phosh-brightness-level"

root = tkinter.Tk(":0")
root.title("Brightness Changer")
root.config(bg="Black")

value = tkinter.IntVar()
slider = tkinter.ttk.Scale(root, from_=1, to=100, orient="horizontal", variable=value, length=200)

level = open(file_path, "r")
brightness = level.read()
value.set(brightness)
level.close()

def update_brightness(nothing=""):
    level = open(file_path, "w")
    level.write(str(value.get()))
    level.close()
    slider_level.config(text=f"Current Brightness: {str(value.get())}")

update_button = tkinter.Button(text="Update Brightness", bg="Black", fg="White", command=update_brightness, font=("Arial", 24))
update_button.pack()

slider_level = tkinter.Label(text=f"Current Brightness: {value.get()}", bg="Black", fg="White", font=("Arial", 24))
slider_level.pack()
slider.set(value.get())

slider.pack()


root.mainloop()
