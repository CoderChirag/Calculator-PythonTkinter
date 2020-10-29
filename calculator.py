from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import *

class Calculator(Tk):
    def __init__(self):                     
        super().__init__()
        self.wm_iconbitmap("CalCJ.ico")
        self.geometry("430x653")
        self.minsize(430, 653)
        self.maxsize(430, 653)
        self.title("CalCJ")
        self.configure(background="#0EA74B")
        self.inputValue = StringVar()
        self.inputValue.set("")
        self.problem = ""
        self.result = ""
    def createButton(self, text, bg):
        self.b = Button(self,text=text, height=3, width=10, bg=bg, fg="white", overrelief="flat", font="comicsansms 9 bold")
        self.b.bind("<Button-1>", self.click)
        if bg == "#7CFC17":
            self.b.configure(fg="black")
            self.b.update()
        return self.b
    def outputBox(self):
        self.screen = Entry(self, bg="#0FF4F4", font="comicsansms 12", width=41, textvariable=self.inputValue)
        return self.screen.grid(row=1,column=1,columnspan=41, ipady=10)
    def blankspace(self, height, width):
        return Label(self,height=height, width=width, bg="#0EA74B")
    def menubar(self):
        root_menu = Menu(self)
        menu_file = Menu(root_menu, tearoff=0)
        menu_file.add_command(label="New Calculation", command= lambda :self.inputValue.set(""))
        menu_file.add_command(label="Save as", command=self.save)
        menu_file.add_command(label="Exit", command= self.destroy)
        root_menu.add_cascade(label="File", menu=menu_file)
        menu_help = Menu(root_menu, tearoff=0)
        menu_help.add_command(label="Credits", command=self.Credits)
        
        root_menu.add_cascade(labe="Help", menu=menu_help)
        self.config(menu=root_menu)
    def Credits(self):
        tmsg.showinfo("Credits", "Developed by - Chirag Jain")

    def click(self, event):
        text = event.widget.cget("text")
        if text=="✕":
            text = "*"
        print(f"{text} got Clicked")
        if text == "=":
            if self.inputValue.get().isdigit():
                self.problem = self.inputValue.get()
                print("Problem Saved in cache")
                value = int(self.inputValue.get())
            else:
                try:
                    value = eval(self.inputValue.get())
                    self.problem = self.inputValue.get()
                    print("Problem Saved in cache")
                except Exception as e:
                    print(e)
                    value = "ERROR"
            self.inputValue.set(value)
            self.screen.update()
            self.result = self.inputValue.get()
            print("Result Saved in cache")
        elif text=="DEL":
            self.screen.delete(len(self.inputValue.get())-1, END)
        elif text=="AC":
            self.inputValue.set("")
        else:
            operations = ["+", "-", "/", "%", "✕"]
            Index = len(self.inputValue.get())
            if Index!=0:
                prev_value =  self.inputValue.get()[-1]
                if (prev_value not in operations) or ((prev_value in operations) and text not in operations):
                    self.inputValue.set(self.inputValue.get() +text)
                    self.screen.update()
            else:
                self.inputValue.set(self.inputValue.get() +text)
                self.screen.update()
    def save(self):
        files = [('Text Document', '*.txt'),('Python Files', '*.py'),('All Files', '*.*')]
        # file = asksaveasfile(filetypes = files, defaultextension = files)
        name=asksaveasfile(mode='w',defaultextension=files, filetypes = files)
        text2save=f"{self.problem} = {self.result}"
        name.write(text2save)
        name.close
        tmsg.showinfo("Save Successfull", "Your file was saved successfully")
        
    
        
root = Calculator()

menu_bar = root.menubar()

root.blankspace(1,3).grid(row=0,column=0)
root.blankspace(1,3).grid(row=1,column=0)
root.outputBox()

root.blankspace(2,3).grid(row=2,column=0)
root.createButton("(", "#2F7832").grid(row=3,column=1, sticky="w")
root.createButton(".", "#2F7832").grid(row=3,column=22, sticky="w")
root.createButton(")", "#2F7832").grid(row=3,column=41, sticky="e")
root.blankspace(1,3).grid(row=4,column=0)

root.createButton("9", "#F80F2B").grid(row=5,column=1, sticky="w")
root.createButton("8", "#F80F2B").grid(row=5,column=22, sticky="w")
root.createButton("7","#7CFC17").grid(row=5,column=41, sticky="e")
root.blankspace(1,3).grid(row=6,column=0)

root.createButton("6","#F80F2B").grid(row=7,column=1, sticky="w")
root.createButton("5","#2F7832").grid(row=7,column=22, sticky="w")
root.createButton("4","#7CFC17").grid(row=7,column=41, sticky="e")
root.blankspace(1,3).grid(row=8,column=0)

root.createButton("3","#F80F2B").grid(row=9,column=1, sticky="w")
root.createButton("2","#2F7832").grid(row=9,column=22, sticky="w")
root.createButton("1","#7CFC17").grid(row=9,column=41, sticky="e")
root.blankspace(1,3).grid(row=10,column=0)

root.createButton("0","#F80F2B").grid(row=11,column=1, sticky="w")
root.createButton("✕","#2F7832").grid(row=11,column=22, sticky="w")
root.createButton("+","#7CFC17").grid(row=11,column=41, sticky="e")
root.blankspace(1,3).grid(row=12,column=0)

root.createButton("%","#F80F2B").grid(row=13,column=1, sticky="w")
root.createButton("/","#7CFC17").grid(row=13,column=22, sticky="w")
root.createButton("-","#7CFC17").grid(row=13,column=41, sticky="e")
root.blankspace(1,3).grid(row=14,column=0)

root.createButton("DEL","#F80F2B").grid(row=15,column=1, sticky="w")
root.createButton("=","#F80F2B").grid(row=15,column=22, sticky="w")
root.createButton("AC","#2F7832").grid(row=15,column=41, sticky="e")
root.mainloop()

