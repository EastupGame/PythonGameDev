import tkinter
num = 0       #num을 전역변수로 선언   
def count_up():
    global num          #num을 전역변수로 취급하기 위한 선언
    num = num + 1
    label["text"] = num
    root.after(1000, count_up)
    
root = tkinter.Tk()
label = tkinter.Label(font = ("System",80))
label.pack()
root.after(1000, count_up)
root.mainloop()




