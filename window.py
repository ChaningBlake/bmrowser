from tkinter import *



class bmrowser:
    def __init__(self, master):
        # navbar is container for buttons above content (back/forward/refresh/addressbar/etc.)
        navbar = Frame(master)
        navbar.pack()
        self.backbtn = Button(navbar, text="🡄", command=self.backpage)
        self.backbtn.pack(side=LEFT)

        self.forwardbtn = Button(navbar, text="🡆", command=self.forwardpage)
        self.forwardbtn.pack(side=LEFT)

        self.refreshbtn = Button(navbar, text="⟳", command=self.refreshpage)
        self.refreshbtn.pack(side=LEFT)

        self.homebtn = Button(navbar, text="⌂", command=self.homepage)
        self.homebtn.pack(side=LEFT)

        self.adrbar = Text(navbar, height=1, width=30)
        self.adrbar.pack(side=LEFT)

        self.menubtn = Button(navbar, text="☰", command=self.showmenu)
        self.menubtn.pack(side=RIGHT)

        contentbox = Frame(master)
        contentbox.pack()
        self.button3 = Button(contentbox, text="this btn in content area", fg="blue", command=self.refreshpage)
        self.button3.pack(side=LEFT)

    def backpage(self):
        print("test string")
    def forwardpage(self):
        print("test string")
    def refreshpage(self):
        print("test string")
    def homepage(self):
        print("test string")
    def showmenu(self):
        print("test string")

root = Tk()
app = bmrowser(root)
root.mainloop()
root.destroy()
