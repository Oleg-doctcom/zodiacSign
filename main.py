import interface
import zodiac

def a():
    d=interface.e1.get()
    m=interface.e2.get()
    index=zodiac.define(int(d),int(m))
    interface.name.config(text=interface.zodiac_names[index])
    interface.gif.config(file=f'img/{interface.zodiac_files[index]}')

interface.button.config(command=a)

interface.window.mainloop()