from tkinter import *
from tkinter import ttk

class tkinterforms():
    def next_widget(self , event):
        event.widget.tk_focusNext().focus()        
        return "break"
    


            
    def get_data(self):
        return self.result

    def set_input(self):
        self.result.append(self.Combo.get())      
        for i in self.ent:
            self.result.append(i.get())
        self.root.destroy()
        
    def set_input1(self):            
        for i in self.ent:
            self.result.append(i.get())
        self.root.destroy()       


    def __init__(self):
        self.result=[]        
        self.ent=[]
        self.root = Tk()
        self.root.geometry("300x200")
        self.root.eval('tk::PlaceWindow . center')
#         self.frame=Frame(self.root)
        
        
#         self.Combo.set("Pick an Option")
    def CreateComboFunc(self,num,vlist):
        self.Combo = ttk.Combobox(self.root,justify='left', values =vlist,width=30)
        self.Combo.focus()
        
        self.Combo.bind("<Return>", self.next_widget)
        self.Combo.pack(side=TOP,fill=X,pady=5)  
        for i in range(num):            
            self.label = Label(self.root,text = 'item'+str(i+1))
            self.label.pack()
            self.label.config(justify = CENTER)            
            self.entry = Entry(self.root, width = 30)
            self.ent.append(self.entry )
#             self.ent[0].focus()
            self.entry.bind("<Return>", self.next_widget)
            self.entry.pack()
        button1 = Button(self.root, text = 'ADD TO LIST', bg="lightblue", fg="blue")
        button1.pack() 
        button1.config(command = self.set_input)
        self.root.bind('<Return>', lambda event=None: button1.invoke())        
        self.root.mainloop()
        return self.result
    
    def CreateEntryFunc(self,num):            
            for i in range(num):            
                self.label = Label(self.root,text = 'item'+str(i+1))
                self.label.pack()
                self.label.config(justify = CENTER)            
                self.entry = Entry(self.root, width = 30)
                self.ent.append(self.entry )
                self.ent[0].focus()
                self.entry.bind("<Return>", self.next_widget)
                self.entry.pack()
            button1 = Button(self.root, text = 'ADD TO LIST', bg="lightblue", fg="blue")
            button1.pack() 
            button1.config(command = self.set_input1)
            self.root.bind('<Return>', lambda event=None: button1.invoke())        
            self.root.mainloop()
            return self.result
# tkinterforms().CreateEntryFunc(2)
# tkinterforms().CreateComboFunc(1,option)