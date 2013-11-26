from tkinter import *
from tkinter import ttk
class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent,background="white")   
         
        self.parent = parent
        self.parent.title("Internet Download Manager")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
       
    def centerWindow(self):

        global counter_entry
        width = 1000
        height = 750

        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()
        
        x = (screen_width - width)/2
        y = (screen_height - height)/2
        self.parent.geometry('%dx%d+%d+%d' % (width, height, x, y))

        #Button List:
        play_button = Button(self,text= "PLAY",width=12,font=('Times New Roman',11)) #add command keyargs
        play_button.place(x=330,y=60)
        pause_button = Button(self,text="PAUSE",width=12,font=('Times New Roman',11))
        pause_button.place(x=470,y=60)
        remove_button = Button(self,text="REMOVE",width=12,font=('Times New Roman',11))
        remove_button.place(x=610,y=60)
        download_button = Button(self,text="DOWNLOAD",width=14,font=('Times New Roman',11))
        download_button.place(x=820,y=153)
        #URL Field and label
        area = Text(self,height=2,width=50,bg='grey',fg='black')
        area.place(x=300,y=150)
        label_url = Label(self,text="Enter The URL:",bg='white',font=('Times New Roman',13))
        label_url.place(x=150,y=153)

        #List Entries
        listlabel = Label(self,text='Download List:',bg='white',font=('Times New Roman',13))
        listlabel.place(x=150,y=230)
        list_display = Label(self,text='Selected Entry:',bg='white',font=('Times New Roman',13))
        list_display.place(x=150,y=550)
        entries = ['Hello World','Grammar Nzi']

        # Use if treeview widget fails
        lb = Listbox(self,width=70,bg='grey')
        for i in entries:
            i = str(counter_entry)+". "+i
            lb.insert(END, i)
            counter_entry+=1
            
        lb.bind("<<ListboxSelect>>", self.onSelect)    
            
        #lb.place(x=250,y=280)

        tree = ttk.Treeview(self,show='headings',height=10,selectmode='browse')
        tree['columns']=('0','1','2','3','4','5')
        tree.column('0',width=70)
        tree.column('1',width=200)
        tree.column('2',width=120)
        tree.column('3',width=150)
        tree.column('4',width=120)
        tree.column('5',width=120)
        tree.heading('0',text="Sl.No")
        tree.heading('1',text="Name")
        tree.heading('2',text='Size')
        tree.heading('3',text='Modified')
        tree.heading('4',text='Status')
        tree.heading('5',text='Threads')
        tree.place(x=150,y=280)
        tree.insert("",'end','',values=("1.","Max","299"))
        tree.insert("",'end','',values=("2.","Sam","199"))
        tree.insert("",'end','',values=("3.","Kim","99"))
        
        tree.bind("<<TreeviewSelect>>", self.onSelect) #Virtual Events.
        self.var = StringVar()
        self.label = Label(self, text=0, textvariable=self.var,font=('Times New Roman',13),bg='white')        
        self.label.place(x=350, y=550)


        #Progress Bar
        prog_bar=ttk.Progressbar(self,orient=HORIZONTAL,length=500)
        prog_bar.place(x=250,y=600)
        
    def onSelect(self, val):
        sender = val.widget
        idx = sender.selection()
        display_value = sender.focus()[1:]
        self.var.set(display_value)
        
def main():
  
    root = Tk()
    ex = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    counter_entry = 1
    main()  
