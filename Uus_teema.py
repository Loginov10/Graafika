from tkinter import*  #Графическая оболочка
k=0
def klikker():
    global k
    k+=1
    nupp.configure(text=k)
    if k%2==0:
        raam.itemconfig(pildid,image=pilt)
    else:
        raam.itemconfig(pildid,image=pilt2)

def text_to_lbl(event):
    text=tekst_kast.get()
    pealkiri.configure(text=text)
    tekst_kast.delete(0,END)

tekst="Aken"
aken=Tk()
aken.geometry("800x900")  #разрешение экрана
aken.title(tekst)          #заголовок
aken.iconbitmap("mush.ico")       #иконка


pealkiri=Label(aken,
               text="Tkinteri põhielemendid",
               bg="purple",          #цвет background
               fg="#e36319",         #другой цвет
               font="Algerian 20",  #шрифт и размер
               height=3,   #высота
               width=20)   #размер
nupp=Button(aken,
            text="Vajuta mind",
            bg="lightblue",          #цвет background
            fg="#4f1fd1",         #другой цвет
            font="Dubai 20",  #шрифт и размер
            activebackground="orange",
            activeforeground="red",
            height=3,    
            width=20,
            command=klikker)           
raam=Canvas(aken,
            width=481,
            height=621,
            bg="black",)
pilt=PhotoImage(file="among.png")
pilt2=PhotoImage(file="among2.png")
pildid=raam.create_image(2,2,image=pilt,anchor=NW)    #растояние пикселей(отступ от начала),   anchor - якорь,начало картинки
tekst_kast=Entry(aken,
                 fg="lightblue",
                 bg="grey",
                 font="Dubai 20",
                 width=20,
                 justify=CENTER)

tekst_kast.bind("<Return>",text_to_lbl) #Enter

pealkiri.pack()  #упаковка элементов
tekst_kast.pack() #side=LEFT,RIGHT
nupp.pack()           #pack отображает
raam.pack()
aken.mainloop()      
