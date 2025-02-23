from tkinter import *
from PIL import ImageTk, Image

def Stock_main():
    st = Toplevel()

    img =Image.open('./A.gif')
    bg = ImageTk.PhotoImage(img)

    st.geometry("650x450")

    # 배경을 Label을 이용하여 처리
    label = Label(st, image=bg)
    label.place(x = -2,y = -2)

    #button_gambling = Button(st, text='도박', fg='white', bg='black', font=15, width=15, height=3, command=Gambling)

    # Tkinter 수행
    st.mainloop()

     

    # 배경 이미지의 좌표를 0, 0 으로 하면 약간의 빈 공간이 나타난다.

    label.place(x =0,y =0)
