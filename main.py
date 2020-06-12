import units
import conversiontables as ct
import tkinter as tk

class Window(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.drawwidgets()

    def drawwidgets(self):
        self.master.title("Weight Converter")
        self.pack()

        #Labels
        L1 = tk.Label(self, text = "This is a simple unit converter")
        L1.grid(row=0, column=0, columnspan=5)
        L2 = tk.Label(self, text= "", bd=5, bg="white")
        L2.grid(row=1, column=4, padx=5)

        #Dropdown Menus
        var1 = tk.StringVar()
        var1.set("m")
        Dropdown1 = tk.OptionMenu(self, var1, *[x for x in units.stringtoclass.keys()])
        Dropdown1.grid(row=1, column=1, padx=5)
        var2 = tk.StringVar()
        Dropdown2 = tk.OptionMenu(self, var2, *[x for x in units.stringtoclass.keys()])
        Dropdown2.grid(row=1, column=3, padx=5)

        #Entry Boxes
        E1 = tk.Entry(self)
        E1.grid(row=1, column=0, padx=10)

        #Convert Button
        B1 = tk.Button(self, text="CONVERT", command=lambda: self.conversion(var1, var2, L2, E1))
        B1.grid(row=1, column=2, padx=5)




    def conversion(self, dd1, dd2, label, entry):
        startvar = units.stringtoclass[dd1.get()](entry.get())
        outputvar = units.stringtoclass[dd2.get()](20)
        output = startvar.convert(outputvar.name)
        label["text"] = str(output)





root = tk.Tk()
app = Window(root)
root.mainloop()






