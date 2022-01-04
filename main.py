from tkinter import *
import time
from threading import Thread

i = 0
j = 0
w = 0

def callback(sv):
    global i, j, w
    try:
        if sv.get()[-1] == story_list[j][i].lower():
            canvas.itemconfig(text3, text='')
            i += 1
            canvas.itemconfig(text, text=story_list[j])
            canvas.itemconfig(text2, text=story_list[j][:i])
            cpm_num.config(text=w)
            w += 1
        else:
            if sv.get() in story_list[j]:
                pass
            else:
                canvas.itemconfig(text3, text=story_list[j][:i])
    except IndexError:
        canvas.itemconfig(text3, text='')
        if len(story_list[j]) > 1:
            j += 1
            i = 0
            canvas.itemconfig(text, text=story_list[j])
            canvas.itemconfig(text2, text=story_list[j][:i])
            entry.delete(0, END)

def countdowntimer():
    global w
    times = int(sec.get())
    while times > -1:
        minute,second = (times // 60 , times % 60)        
        if minute > 60:
            minute = (minute // 60 , minute % 60)
        sec.set(second)
        root.update()
        time.sleep(1)
        if(times == 0):
            sec.set('00')
            canvas.itemconfig(text, text=f'Your typing speed is:\n{w - 1} CPM')
            canvas.itemconfig(text2, text='')
            canvas.itemconfig(text3, text='')
            entry.delete(0, END)
            entry.config(state=DISABLED)
            root.update()
        times -= 1

def start_count():
    if i == 1:
        Thread(target = countdowntimer).start()
    Thread(target = callback(sv)).start()

def restart_command():
    global i, j, w
    entry.config(state=NORMAL)
    entry.delete(0, END)
    i = 0
    j = 0
    w = 0
    sec.set('60')
    cpm_num.config(text='?')
    canvas.itemconfig(text, text=story_list[j])


story = "I stand in a perfectly,pristine kitchen,The counter tops,are covered in flour,She stands at them,waiting for me,She's rolling out,the cookie dough,in deepeven strokes,like the ocean kissing,the beach Her,soft humming,fills the kitchen,with love Her,hands lift me up,I'm in a navy blue,sundress with little,yellow sunflowers on,it “Here sweetie”,she hands me an,apron and I lift my little arms obediently,to her She ties it around my waist,A little teddy bear clutching a rolling,pin in one soft brown paw,is splashed across, my tummy And,beside me she,rolls I watch,the muscles in,his taunt arms,ripple with the pressure,The sunlight makes,the sugar glisten,and sparkle like,glitter The room,smells sweetly of,the confections we,are working so, diligently to create,She smiles at,me and gestures,at the cookie cutters"

story_list = story.split(',')

#Root
root = Tk()
root.title('Typing Speed Test')
root.config(padx=20, pady=20)

#StringVar
sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: start_count())

sec = StringVar()
sec.set('60')

#Labels
cpm = Label(text='CPM:')
cpm.grid(column=0, row=0)
cpm_num = Label(root, text='?', bg='white')
cpm_num.grid(column=1, row=0) 

time_left = Label(text='Time Left:')
time_left.grid(column=2, row=0)
time_left_num = Entry(root, textvariable=sec, width =2, font = 'Times 10', state=NORMAL)
time_left_num.grid(column=3, row=0)

#Button
restart = Button(root, text='Restart', command=restart_command)
restart.grid(column=4, row=0, padx=5)


#Canvas
canvas = Canvas(root, width=300, height=200, bg='white')
text = canvas.create_text(40,75,width=300,anchor=NW, fill='black', font='Times 20 bold', text=story_list[j])
text2 = canvas.create_text(40,75,width=300,anchor=NW, fill='green', font='Times 20 bold', text="")
text3 = canvas.create_text(40,75,width=300,anchor=NW, fill='red', font='Times 20 bold', text="")
canvas.grid(column=0, row=1, columnspan=5, pady=10)

#Entry
entry = Entry(root, width=40, textvariable=sv, state=NORMAL)
entry.grid(column=0, row=2, columnspan=5)


root.mainloop()
