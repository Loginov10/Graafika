from tkinter import*  #Графическая оболочка
k=0
def klikker():
    global k
    k+=1
    nupp.configure(text=k)

tekst="Aken"
aken=Tk()
aken.geometry("500x700")  #разрешение экрана
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

pealkiri.pack()       #упаковка элементов
nupp.pack()

aken.mainloop()      