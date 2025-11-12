from tkinter import *
import random

# приделать сохранению и лидерборд
choice = int()
computer_choice = 0
rules = {0:1, 1:2, 2:0}

#Фунцкии
def choose_rock():
    global choice
    choice = 0
    nothing()
    ppic = Canvas(width=105, height=105)
    ppic.grid(column=1,row=1)
    ppic.create_image(0, 0, image=rock_image, anchor= NW)
    binput.configure(state="active", text="Выбрал!")   

def choose_scissors():
    global choice
    choice = 1
    nothing()
    ppic = Canvas(width=105, height=105)
    ppic.grid(column=1,row=1)
    ppic.create_image(0, 0, image=scissors_image, anchor= NW)  
    binput.configure(state="active", text="Выбрал!")       
    
def choose_paper():
    global choice
    choice = 2
    nothing()
    ppic = Canvas(width=105, height=105)
    ppic.grid(column=1,row=1)
    ppic.create_image(0, 0, image=paper_image, anchor= NW) 
    binput.configure(state="active", text="Выбрал!")     

def nothing():
    global choice
    choice = 0
    ppic = Canvas(width=105, height=105)
    ppic.grid(column=1,row=1)
    ppic.create_image(0, 0, image=nothing_image, anchor= NW) 
    cpic = Canvas(width=105, height=105)
    cpic.grid(column=1,row=0)
    cpic.create_image(0, 0, image=nothing_image, anchor= NW)

def game():
    global choice, counter, counter_all, computer_choice
    computer_choice = random.randint(0, 2)
    if rules[choice] == computer_choice:  
        binput.configure(text="Победа")
        computer_image()
        counter += 1
        counter_all += 1
        text.configure(text=f"Счетчик побед:\n {counter}")
        alltext.configure(text=f"Счетчик игр:\n {counter_all}")
        binput.configure(state="disabled")
    elif rules[computer_choice] == choice:
        binput.configure(text="Поражение")
        computer_image()
        counter_all += 1
        alltext.configure(text=f"Счетчик игр:\n {counter_all}")
        binput.configure(state="disabled")
    else:
        binput.configure(text="Ничья")
        computer_image()
        counter_all += 1
        alltext.configure(text=f"Счетчик игр:\n {counter_all}")
        binput.configure(state="disabled")

def computer_image():
    if computer_choice == 0:
        cpic = Canvas(width=105, height=105)
        cpic.grid(column=1,row=0)
        cpic.create_image(0, 0, image=rock_image, anchor= NW)
    elif computer_choice == 1:
        cpic = Canvas(width=105, height=105)
        cpic.grid(column=1,row=0)
        cpic.create_image(0, 0, image=scissors_image, anchor= NW)
    else:
        cpic = Canvas(width=105, height=105)
        cpic.grid(column=1,row=0)
        cpic.create_image(0, 0, image=paper_image, anchor= NW)
        
#Главная картинка
screen = Tk()
screen.title("Камень, ножницы, бумага!")
screen.minsize()
screen.resizable(0,0)

#Кнопки всякие
brock = Button(text="Камень", command=choose_rock)
bscissors = Button(text="Ножницы", command=choose_scissors)
bpaper = Button(text="Бумага", command=choose_paper)
brock.grid(column=0,row=3, ipadx=10, ipady=10, padx=10, pady=10)
bpaper.grid(column=2,row=3, ipadx=10, ipady=10, padx=10, pady=10)
bscissors.grid(column=1,row=3, ipadx=10, ipady=10, padx=10, pady=10)
binput = Button( text="Выбрал!", command=game, state=DISABLED)
binput.grid(column=0,columnspan=3,row=2, padx=10, pady=10, ipadx=100, ipady=10)

#Счетчик побед
counter = 0
counter_all = 0

#Тексты всякие
text = Label(text=f"Счетчик побед:\n {counter}")
text.grid(column = 2, row=1, padx=10, pady=10,)
alltext = Label(text=f"Счетчик игр:\n {counter_all}")
alltext.grid(column = 2, row=0, padx=10, pady=10)
chosentext = Label(text="Ваш выбор: ")
chosentext.grid(column = 0, row=1, padx=10, pady=10)
computertext = Label(text="Выбор\nкомпьютера: ")
computertext.grid(column = 0, row=0, padx=10, pady=10)

#Для картинок
rock_image = PhotoImage(file=r"Pics\paper1.png")
paper_image = PhotoImage(file=r"Pics\paper1.png")
scissors_image = PhotoImage(file=r"Pics\scissor1.png")
nothing_image = PhotoImage(file=r"Pics\question1.png")
cpic = Canvas(width=105, height=105)
cpic.grid(column=1,row=0)
cpic.create_image(0, 0, image=nothing_image, anchor= NW)
ppic = Canvas(width=105, height=105)
ppic.grid(column=1,row=1)
ppic.create_image(0, 0, image=nothing_image, anchor= NW)

#Делаем все ровным
for c in range(4): screen.columnconfigure(index= c, weight=1)
for r in range(4): screen.rowconfigure(index=r, weight=1)

screen.mainloop()


#Прикрутить кнопку выход, кнопку начать в самом начале, лидерборд сделать в начале ник запрашивает и в файле сохраняет

