import tkinter
root = tkinter.Tk()
root.title("첫 번째 윈도우")
root.geometry("800x600")
label = tkinter.Label(root, text = "라벨 문자열", font = ("System",12))
label.place(x = 200, y = 500)
root.mainloop()
