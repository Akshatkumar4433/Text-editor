from tkinter import *
class Text_editor:
    def __init__(self,window):
        self.window = window
        window.geometry("500x500")

        frame = Frame(master = window)
        save = Button(master = frame, text = 'Save', height = '1', width = '5')
        save.pack(side = LEFT)


        save_as = Button(master = frame,text = 'Save as', height = '1', width = '5')
        save_as.pack(side = LEFT)

        find = Button(master = frame, text = 'Find', height = '1', width = '5')
        find.pack(side = LEFT)

        fonts = Button(master = frame, text = 'Fonts', height = '1', width = '5')
        fonts.pack(side = LEFT)

        frame.pack()

        self.text = StringVar()

        page = Text(window,   width = 100, height = 200)
        page.pack(fill = BOTH)





        #def Save(self):
            #self.SAVE = tk.Button(
                #text = 'Save',
                #width = 25,
                #height = 5)
            #print('hello')
            #self.SAVE.pack()


#These are instances
window = Tk()
Text_editor(window)
window.mainloop()
