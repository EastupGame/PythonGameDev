import tkinter
root = tkinter.Tk()
root.title("첫 번째 캔버스")          
canvas = tkinter.Canvas(root, width = 400, height = 600,    #캔버스 컴포넌트 생성
                        bg = "skyblue")
canvas.pack()                   #윈도우에 캔버스를 배치
root.mainloop()

