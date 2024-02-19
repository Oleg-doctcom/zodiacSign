# -*- coding: utf-8 -*-
from tkinter import *

window = Tk()
window.geometry('300x500')
window.title('Canvas')

zodiac_names=['Неправильная дата рождения!','Козерог','Водолей','Рыба','Овен','Телец','Близнецы','Рак','Лев','Дева','Весы','Скорпион','Стрелец']
zodiac_files=['start.gif','capricorn.gif','aquarius.gif','pisces.gif','aries.gif','taurus.gif','gemini.gif','cancer.gif','leo.gif','virgo.gif','libra.gif','scorpio.gif','sagittarius.gif']

loc=LabelFrame(text='Дата рождения')

n1=Label(loc,text='Введите день ')
n2=Label(loc,text='Введите месяц ')

e1=Entry(loc)
e2=Entry(loc)

button=Button(text='Определить знак')

name=Label(text='Сначала введите дату')

gif=PhotoImage(file='img/start.gif')

image=Label(image=gif)

loc.grid()
n1.grid(sticky=W,pady=5,padx=5)
n2.grid(sticky=W,pady=5,padx=5)
e1.grid(column=1,row=0,pady=5,padx=5)
e2.grid(column=1,row=1,pady=5,padx=5)
button.grid(pady=5,padx=5)
name.grid(pady=5,padx=5)
image.grid(pady=5,padx=20)

if __name__=='__main__':
    window.mainloop()