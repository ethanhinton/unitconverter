import units
import conversiontables as ct
import tkinter as tk
from decimal import Decimal

class Window(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title("Unit Converter")
        self.pack()
        self.drawwidgets()

    def drawwidgets(self):
        #Labels
        self.L1 = tk.Label(self, text = "This is a simple unit converter")
        self.L1.grid(row=0, column=0, columnspan=5)
        self.L2 = tk.Label(self, text= "", bd=5, bg="white")
        self.L2.grid(row=1, column=4, padx=5)

        #Dropdown Menus
        self.options = [x for x in units.stringtoclass.keys()]
        self.var1 = tk.StringVar()
        self.var1.set(self.options[0])
        self.var1.trace_add("write", lambda *args: self.update_dropdown())
        self.Dropdown1 = tk.OptionMenu(self, self.var1, *self.options)
        self.Dropdown1.grid(row=1, column=1, padx=5)
        self.var2 = tk.StringVar()
        self.Dropdown2 = tk.OptionMenu(self, self.var2, *self.options)
        self.Dropdown2.grid(row=1, column=3, padx=5)



        #Entry Boxes
        self.E1 = tk.Entry(self)
        self.E1.grid(row=1, column=0, padx=10)

        #Convert Button
        self.B1 = tk.Button(self, text="CONVERT", command=lambda: self.conversion())
        self.B1.grid(row=1, column=2, padx=5)

    def conversion(self):
        startvar = units.stringtoclass[self.var1.get()](self.E1.get())
        output = startvar.convert(self.var2.get())
        try:
            self.L2["text"] = '%.5g' % output
        except TypeError:
            self.L2["text"] = output

    def update_dropdown(self):
        var1_str = self.var1.get()
        var1_obj_type = units.stringtoclass[var1_str].KIND
        self.options = [x for x in units.stringtoclass.keys() if units.stringtoclass[x].KIND == var1_obj_type]

        menu = self.Dropdown2["menu"]
        menu.delete(0, "end")
        for string in self.options:
            menu.add_command(label=string,
                             command=lambda value=string: self.var2.set(value))



root = tk.Tk()
app = Window(root)
root.mainloop()






