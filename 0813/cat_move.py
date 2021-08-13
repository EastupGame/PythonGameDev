import tkinter
key = ""
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""
    
cx = 400
cy = 300
def main_proc():    #실시간 처리 수행할 함수
    global cx, cy
    if key == "Up":
        cy = cy - 20
    if key == "Down":
        cy = cy + 20
    if key == "Left":
        cx = cx - 20
    if key == "Right":
        cx = cx + 20        
    canvas.coords("MYCHR",cx, cy)   #캐릭터 이미지를 새로운 위치로 이동
    root.after(100,main_proc)
    
root = tkinter.Tk()
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>",key_up)
canvas = tkinter.Canvas(width = 800, height = 600, bg = "skyblue")
canvas.pack()
cat = tkinter.PhotoImage(file = "mimi.png")
canvas.create_image(cx,cy,image = cat, tag = "MYCHR")
main_proc()
root.mainloop()

#윈도우 PC에서 키 코드
#방향키 37,38,39,40
#스페이스 32
#엔터 13
#알파벳 A~Z 65 ~ 90
#숫자 48 ~ 57
