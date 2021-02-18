
from tkinter import *
import time

def Main():
    global root

    root = Tk()
    root.title("stopwatch made by sandeep")
    width = 500
    height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2)-(width / 2)
    
    
    y = (screen_height / 2)-(height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Top = Frame(root, width=400)
    Top.pack(side=TOP)
    stopwatch = StopWatch(root)
    stopwatch.pack(side=TOP)
    Buttom = Frame(root, width=400)
    Buttom.pack(side=BOTTOM)
    Start = Button(Buttom, text="START",command=stopwatch.Start,height=10,width=5)
    Start.pack(side=LEFT)
    stop = Button(Buttom, text="STOP",command=stopwatch.Stop,height=10,width=5)
    stop.pack(side=LEFT)
    Restet = Button(Buttom, text="RESET",command=stopwatch.Reset,height=10,width=5)
    Restet.pack(side=LEFT)
    Exit = Button(Buttom, text="CLOSEEXT",command=stopwatch.Exit,height=10,width=5)
    Exit.pack(side=LEFT)
    Title = Label(Top,text="this is textmmm title",font=("arial",24),fg="white",bg="black")
    Title.pack(fill=X)
    root.config(bg="black")
    root.mainloop()

class StopWatch(Frame):

    def __init__(self,parent=None,**kw):
        Frame.__init__(self,parent,kw)
        self.startTime = 0.0
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar()
        self.MakeWidget()

    def MakeWidget(self):
        timeText = Label(self,textvariable=self.timestr,font=("times new romean",45),fg="white",bg="black")
        self.SetTime(self.nextTime)        
        timeText.pack(fill=X,expand=NO,pady=5,padx=10)
        

    def Updater(self):
        self.nextTime = time.time()- self.startTime
        self.SetTime(self.nextTime)
        self.timer=self.after(50,self.Updater)
        


    def SetTime(self,nextElap):
        minutes=int(nextElap/60)
        seconds=int(nextElap-minutes*60.0)
        miliseconds=int((nextElap-minutes*60.0-seconds)*100)
        self.timestr.set('%02d:%02d:%02d' % (minutes,seconds,miliseconds))

    def Start(self):
        if not self.onRunning:
            self.startTime = time.time()-self.nextTime
            self.Updater()
            self.onRunning = 1
            
        
        
    def Stop(self):
        if self.onRunning:
            self.after_cancel(self.timer)
            self.nextTime = time.time()- self.startTime
            self.SetTime(self.nextTime)
            self.onRunning = 0

    def Exit(self):
        root.destroy()
        exit()
    def Reset(self):
        self.startTime = time.time()
        self.nextTime = 0.0
        self.SetTime(self.nextTime)
        
if __name__=='__main__':
    
    Main()
    


    
