import tkinter
from tkinter import *

questions = [
    "1.Depressed mood most of the day, nearly every day",
    "2.Markedly diminished interest or pleasure in all, or almost all, activities most of the day, nearly every day.",
    "3.Significant weight loss when not dieting or weight gain, or decrease or increase in appetite nearly every day.",
    "4.A slowing down of thought and a reduction of physical movement (observable by others, not merely subjective feelings of restlessness or being slowed down).",
    "5.Fatigue or loss of energy nearly every day.",    
    "6.Insomnia or Hypersomnia nearly everyday",
    "7.Feelings of worthlessness or excessive or inappropriate guilt nearly every day.",
    "8.Diminished ability to think or concentrate, or indecisiveness, nearly every day.", 
    "9.Recurrent thoughts of death, recurrent suicidal ideation without a specific plan, or a suicide attempt or a specific plan for committing suicide.",
]

answers_choice = [
#1
    ["Symptom Absent.", 
     "Symptom Present",],
#2
    ["Symptom Absent.", 
     "Symptom Present",],
#3
    ["Symptom Absent.", 
     "Symptom Present",],
#4
    ["Symptom Absent.", 
     "Symptom Present",],
#5
    ["Symptom Absent.", 
     "Symptom Present",],
#6
    ["Symptom Absent.", 
     "Symptom Present",],
#7
    ["Symptom Absent.", 
     "Symptom Present",],
#8
    ["Symptom Absent.", 
     "Symptom Present",],
#9
    ["Symptom Absent.", 
     "Symptom Present",],   
] 

user_answer = []

indexes = [0,1,2,3,4,5,6,7,8]
def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "#ffffff",
    )
    labelresulttext.pack()
    if (score > 4):
        img = PhotoImage(file="r2.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Symptoms Of Major Depressive Disorder\n Might Be Present")
    else:
        img = PhotoImage(file="r1.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="No Sign of Depression")


def calc():
    global indexes,user_answer
    x = 0
    score = 0
    for i in indexes:
        x=x+user_answer[i];
        
    showresult(x)


ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 9:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        ques += 1
    else:
        calc()
    




def startquiz():
    global lblQuestion,r1,r2
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("Consolas", 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Times", 12),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Times", 12),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    startquiz()



root = tkinter.Tk()
root.title("Depression DSM-5 Diagnostic Criteria")
root.geometry("800x600")
root.config(background="#ffffff")
root.resizable(0,0)


img1 = PhotoImage(file="quiz.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(10))

labeltext = Label(
    root,
    text = "Depression DSM-5 Diagnostic Criteria",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,10))

img2 = PhotoImage(file="button.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Click Start To Check The Symptoms",
    background = "white",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack()
lblRules = Label(
    root,
    text = "The DSM-5 outlines the following criterion to make a diagnosis of depression. The individual must be\n experiencing five or more symptoms during the same 2-week period and at least one of the\n symptoms should be either (1) depressed mood or (2) loss of interest or pleasure.",
    width = 100,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRules.pack()

root.mainloop()
