import tkinter
from tkinter import *

questions = [
    "1.DEPRESSED MOOD(Gloomy attitude, pessimism about the future, feeling of sadness, tendency to weep",
    "2.FEELINGS OF GUILT",
    "3.SUICIDE",
    "4.WORK AND INTERESTS",
    "5.RETARDATION(Slowness of thought, speech, and activity; apathy; stupor)",    
    "6.ANXIETY-PSYCHIC",
    "7.ANXIETY-SOMATIC(Gastrointestinal,indigestion,Cardiovascular,palpitation,Headaches,Respiratory,Genito-urinary,etc.",
    "8.HYPOCHONDRIASIS", 
    "9.INSOMNIA-Initial(Difficulty in falling asleep)",
    "10.INSOMNIA-Middle(Complains of being restless and disturbed during the night. Walking during the night.)",
    "11.INSOMNIA-Delayed(Walking in early hours of the morning and  unable to fall asleep again)",
    "12.AGITATION(Restlessness associated with anxiety.)",
    "13.SOMATIC SYMPTOMS-GASTROINTESTINAL(Loss of appetite, heavy feeling in abdomen,constipation)",
    "14.SOMATIC SYMPTOMS-GENERAL(Heaviness in limbs, back or head; diffuse backache; loss of energy and fatiguability)",
    "15.GENITAL SYMPTOMS(Loss of libido,menstrual disturbances)",
    "16.WEIGHT LOSS",
    "17.INSIGHT(Insight must be interpreted in terms of patient's understanding and background)",
]

answers_choice = [
    #1
    ["0.Absent", 
     "1.Sadness, etc.", 
     "2.Occasional weeping", 
     "3.Frequent weeping",
     "4.Extreme symptoms",],
#2
    ["0.Absent", 
    "1.Self-reproach,feels he/she has let people down", 
    "2.Ideas of guilt",
    "3.Present illness is a punishment; delusions of guilt",
    "4.Hallucinations of guilt",],
#3
    ["0.Absent", 
    "1.Feels life is not worth living", 
    "2.Wishes he/she were dead",
    "3.Suicidal ideas or gestures",
    "4.Attempts at suicide",],
#7
    ["0.No difficulty", 
    "1.Feelings of incapacity, listlessness, indecision and vacillation", 
    "2.Loss of interest in hobbies, decreased social activites", 
    "3.Productivity decreased",
    "4.Unable to Work.Stopped Working because of present illness only",],
#8
    ["0.Absent", 
    "1.Slight retardation at interview", 
    "2.Obvious retardation at interview", 
    "3.Interview difficult",
    "4.Complete stupor",],
#10
    ["0.No difficulty", 
    "1.Tension and irritability", 
    "2.Worrying about minor matters", 
    "3.Apprehensive attitude",
    "4.Fears",],
#11
    ["0.Absent", 
    "1.Mild", 
    "2.Moderate", 
    "3.Severe",
    "4.Incapacitating",],
#15
    ["0.Not present", 
    "1.Self-absorption(bodily)", 
    "2.Preoccupation with health", 
    "3.Querulous attitude",
    "4.Hypochondriacal delusions",],
#4
    ["0.Absent", 
    "1.Occasional", 
    "2.Frequent",],
#5
    ["0.Absent", 
    "1.Occasional", 
    "2.Frequent",],
#6
    ["0.Absent", 
    "1.Occasional", 
    "2.Frequent",],
#9
    ["0.Absent", 
    "1.Occasional", 
    "2.Frequent",],
#12
    ["0.Absent", 
    "1.Mild", 
    "2.Severe",],
#13
    ["0.Absent", 
    "1.Mild", 
    "2.Severe",],
#14
    ["0.Absent", 
    "1.Mild", 
    "2.Severe",],
#16
    ["0.No Weight loss", 
    "1.Slight", 
    "2.Obvious or severe",],
#17
    ["0.No loss", 
    "1.Partial or doubtfull loss", 
    "2.Loss of insight",],    
] 

user_answer = []

indexes = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    r5.destroy()
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
    if (score >= 0 and score<8):
        img = PhotoImage(file="r1.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="No Need To Worry\n These Ups and Downs are Normal")
    elif (score >= 8 and score < 14):
        img = PhotoImage(file="r2.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Mild Depression")        
    elif (score >= 14 and score < 19):
        img = PhotoImage(file="r4.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Moderate Depression Level")
    elif (score >= 19 and score < 23):
        img = PhotoImage(file="r5.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Severe Level Of Depression")
    else:
        img = PhotoImage(file="r6.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Very Severe Depression")


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
    global lblQuestion,r1,r2,r3,r4,r5
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 17:
        lblQuestion.config(text= questions[indexes[ques]])
        if ques>7:
            r1['text'] = answers_choice[indexes[ques]][0]
            r2['text'] = answers_choice[indexes[ques]][1]
            r3['text'] = answers_choice[indexes[ques]][2]
            r4.destroy()
            r5.destroy()
        else:        
            r1['text'] = answers_choice[indexes[ques]][0]
            r2['text'] = answers_choice[indexes[ques]][1]
            r3['text'] = answers_choice[indexes[ques]][2]
            r4['text'] = answers_choice[indexes[ques]][3]
            r5['text'] = answers_choice[indexes[ques]][4]

        ques += 1
    else:
        calc()
    




def startquiz():
    global lblQuestion,r1,r2,r3,r4,r5
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

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Times", 12),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Times", 12),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)
    r5 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][4],
        font = ("Times", 12),
        value = 4,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r5.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    btnStart.destroy()
    startquiz()



root = tkinter.Tk()
root.title("HAM-D Questions")
root.geometry("700x600")
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
    text = "HAM-D Questionnaire",
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
    text = "Click Start Once You Are Ready",
    background = "white",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack()

root.mainloop()
