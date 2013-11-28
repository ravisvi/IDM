from tkinter import *
from tkinter import ttk
from utilities import *
import download
import time
class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent,background="white")   
         
        self.parent = parent
        self.parent.title("Internet Download Manager")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
    


    def fetch(self):        #Extract URL From the Text field.
        global counter_entry,list_downloadObj
        url = self.area.get('1.0',END)
        url = url.strip('\n')
        #print(url)
        download_object = download.Download_object(url, 4)
        init_download(download_object)
        
        list_downloadObj.append(download_object)
        #send the url to respective function to download.
        downNow(download_object)


    def update(self):
        global counter_entry
        url = self.area.get('1.0',END)
        url = url.strip('\n')
        #print(url)
        download_object = download.Download_object(url, 4)
        init_download(download_object)
        counter_val = str(counter_entry)+'.'
        counter_entry+=1
        self.tree.insert('','end',values=(counter_val, download_object.fileName,
                                          download_object.size,time.ctime(),'Downloaded',download_object.noOfThreads))
        
    def centerWindow(self):

        width = 1000
        height = 750

        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()
        
        x = (screen_width - width)/2
        y = (screen_height - height)/2
        self.parent.geometry('%dx%d+%d+%d' % (width, height, x, y))

        #URL Field and label
        self.area = Text(self,height=2,width=50,bg='grey',fg='black')
        self.area.place(x=250,y=120)
        
        label_url = Label(self,text="Enter The URL:",bg='white',font=('Times New Roman',13))
        label_url.place(x=100,y=123)

        #List Entries
        listlabel = Label(self,text='Download List:',bg='white',font=('Times New Roman',13))
        listlabel.place(x=100,y=230)
        list_display = Label(self,text='Selected Entry:',bg='white',font=('Times New Roman',13))
        list_display.place(x=220,y=550)
        

        #Button List:
        play_button = Button(self,text= "PLAY",width=12,font=('Times New Roman',11),command=play) #add command keyargs
        play_button.place(x=280,y=60)
        pause_button = Button(self,text="PAUSE",width=12,font=('Times New Roman',11),command=pause)
        pause_button.place(x=440,y=60)
        remove_button = Button(self,text="REMOVE",width=12,font=('Times New Roman',11),command=remove)
        remove_button.place(x=600,y=60)
        update_button = Button(self,text='UPDATE',width = 12,font=('Times New Roman',11),command=self.update)
        update_button.place(x=300,y=190)
        download_button = Button(self,text="DOWNLOAD",width=14,font=('Times New Roman',11),command=self.fetch)
        download_button.place(x=570,y=190)
        #download_button.bind('<Button-1>',self.fetch(area))
        
        
        self.tree = ttk.Treeview(self,show='headings',height=10,selectmode='browse')
        self.tree['columns']=('0','1','2','3','4','5')
        self.tree.column('0',width=70)
        self.tree.column('1',width=200)
        self.tree.column('2',width=120)
        self.tree.column('3',width=150)
        self.tree.column('4',width=120)
        self.tree.column('5',width=120)
        self.tree.heading('0',text="Sl.No")
        self.tree.heading('1',text="Name")
        self.tree.heading('2',text='Size (Bytes)')
        self.tree.heading('3',text='Added On')
        self.tree.heading('4',text='Status')
        self.tree.heading('5',text='Threads')
        self.tree.place(x=120,y=280)
                
        self.tree.bind("<<TreeviewSelect>>", self.onSelect) #Virtual Events.
        self.var = StringVar()
        self.label = Label(self, text=0, textvariable=self.var,font=('Times New Roman',13),bg='white')        
        self.label.place(x=380, y=550)


        #Progress Bar
        prog_bar=ttk.Progressbar(self,orient=HORIZONTAL,length=500)
        prog_bar.place(x=250,y=600)
        #prog_bar.start(5000)
        #prog_bar.step(4.5)
        


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
    list_downloadObj = []
    main()  
