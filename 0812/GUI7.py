import tkinter
root = tkinter.Tk()
root.title("첫 번째 캔버스")          
canvas = tkinter.Canvas(root, width = 480, height = 300, bg = "skyblue")
canvas.pack()                   

park = tkinter.PhotoImage(file = "park.png")        #park에 이미지 로딩
canvas.create_image(240,150,image = park)
root.mainloop()
