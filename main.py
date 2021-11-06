
from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3

from gtts import gTTS
import os
import time


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



mixer.init()
mixer.music.load("kbc.mp3")
mixer.music.play(-1)

def select(event):
    mixer.music.set_volume(1)
    callButton.place_forget()

    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    progressbarLabel.place_forget()
    progressbarLabel1.place_forget()
    progressbarLabel2.place_forget()
    progressbarLabel3.place_forget()

    b = event.widget
    value = b['text']

    for i in range(15):
        if value == correct_answers[i]:
            if value == correct_answers[14]:
                def close():
                    root2.destroy()
                    root.destroy()

                def playagain():
                    Lifeline50Button.config(state=NORMAL, image=image50)
                    audiencePoleButton.config(state=NORMAL, image=audience)
                    phoneLifelineButton.config(state=NORMAL, image=phoneImage)
                    root2.destroy()

                    questionArea.delete(1.0, END)
                    questionArea.insert(END, questions[0])
                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])

                    amountLabel.config(image=amountImage)
                    mixer.music.load('kbc.mp3')
                    mixer.music.play(-1)


                mixer.music.stop()
                mixer.music.load("Kbcwon.mp3")
                mixer.music.play()

                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.config(bg="black")
                root2.geometry("500x400+140+30")
                root2.title("You won 0 Pounds")
                imgLabel = Label(root2, image=centerImage, bd=0)
                imgLabel.pack(pady=30)
                amountLabel.config(image = images[14])
                winLabel = Label(root2, text="والله قدها", font=("arial", 30, "bold"), bg="black", fg="white")
                winLabel.pack()

                playagainButton = Button(root2, text="خدلك لفة ثانية", font=("arial", 20, "bold"), fg="yellow",
                                        bg="black", bd=0, activebackground="black",
                                        activeforeground="yellow", cursor='hand2', command=playagain)
                playagainButton.pack()

                closeButton = Button(root2, text="سكر اللعبة", font=("arial", 20, "bold"), fg="yellow",
                                     bg="black", bd=0, activebackground="black", activeforeground="yellow",
                                     cursor='hand2', command=close)
                closeButton.pack()

                happyimage = PhotoImage(file="happy.png")
                happyLabel = Label(root2, image=happyimage, bg="black")
                happyLabel.place(x=30, y=280)

                happyLabel1 = Label(root2, image=happyimage, bg="black")
                happyLabel1.place(x=400, y=280)

                root2.mainloop()
                break


            questionArea.delete(1.0,END)
            questionArea.insert(END,questions[i+1])

            optionButton1.config(text=first_option[i+1])
            optionButton2.config(text=second_option[i+1])
            optionButton3.config(text=third_option[i+1])
            optionButton4.config(text=fourth_option[i+1])

            amountLabel.config(image=images[i])

        if value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()

            def tryagain():
                Lifeline50Button.config(state=NORMAL,image=image50)
                audiencePoleButton.config(state=NORMAL,image=audience)
                phoneLifelineButton.config(state=NORMAL,image=phoneImage)

                root1.destroy()
                questionArea.delete(1.0,END)
                questionArea.insert(END,questions[0])
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])

                amountLabel.config(image=amountImage)
                mixer.music.load('kbc.mp3')
                mixer.music.play(-1)

            mixer.music.stop()
            mixer.music.load("lose.mp3")
            mixer.music.play()

            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.config(bg="black")
            root1.geometry("500x400+140+30")
            root1.title("You won 0 Pounds")
            imgLabel = Label(root1,image=centerImage,bd=0)
            imgLabel.pack(pady=30)

            loseLabel=Label(root1,text="خسرت يا كبير",font=("arial",30,"bold"),bg="black",fg="white")
            loseLabel.pack()

            tryagainButton = Button(root1,text= "جرب ثاني",font= ("arial",20,"bold"),fg="yellow",
                                    bg="black",bd=0,activebackground="black",
                                    activeforeground="yellow",cursor='hand2',command=tryagain)
            tryagainButton.pack()

            closeButton = Button(root1, text="سكر اللعبة", font=("arial", 20, "bold"), fg="yellow",
                                    bg="black", bd=0, activebackground="black", activeforeground="yellow",
                                    cursor='hand2',command=close)
            closeButton.pack()

            sadimage = PhotoImage(file="sad.png")
            sadLabel = Label(root1,image=sadimage,bg="black")
            sadLabel.place(x=30,y=280)

            sadLabel1 = Label(root1, image=sadimage,bg="black")
            sadLabel1.place(x=400, y=280)





            root1.mainloop()
            break

def lifeLine50():
    Lifeline50Button.config(image=image50x,state=DISABLED)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        optionButton4.config(text='')
        optionButton1.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        optionButton2.config(text='')
        optionButton3.config(text='')

def audiencePoleLife():
    audiencePoleButton.config(image=audiencex,state=DISABLED)

    progressbarA.place(x=580,y=190)
    progressbarB.place(x=620, y=190)
    progressbarC.place(x=660, y=190)
    progressbarD.place(x=700, y=190)
    progressbarLabel.place(x=580,y=320)
    progressbarLabel1.place(x=620, y=320)
    progressbarLabel2.place(x=660, y=320)
    progressbarLabel3.place(x=700, y=320)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        progressbarA.config(value=30)
        progressbarB.config(value=60)
        progressbarC.config(value=40)
        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        progressbarA.config(value=30)
        progressbarB.config(value=80)
        progressbarC.config(value=40)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        progressbarA.config(value=60)
        progressbarB.config(value=80)
        progressbarC.config(value=50)
        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        progressbarA.config(value=30)
        progressbarB.config(value=70)
        progressbarC.config(value=90)
        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        progressbarA.config(value=80)
        progressbarB.config(value=30)
        progressbarC.config(value=40)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        progressbarA.config(value=80)
        progressbarB.config(value=10)
        progressbarC.config(value=40)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        progressbarA.config(value=80)
        progressbarB.config(value=30)
        progressbarC.config(value=20)
        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        progressbarA.config(value=10)
        progressbarB.config(value=30)
        progressbarC.config(value=50)
        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        progressbarA.config(value=90)
        progressbarB.config(value=80)
        progressbarC.config(value=70)
        progressbarD.config(value=20)

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        progressbarA.config(value=40)
        progressbarB.config(value=20)
        progressbarC.config(value=50)
        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        progressbarA.config(value=30)
        progressbarB.config(value=80)
        progressbarC.config(value=40)
        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        progressbarA.config(value=20)
        progressbarB.config(value=60)
        progressbarC.config(value=80)
        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        progressbarA.config(value=60)
        progressbarB.config(value=35)
        progressbarC.config(value=40)
        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        progressbarA.config(value=90)
        progressbarB.config(value=65)
        progressbarC.config(value=60)
        progressbarD.config(value=80)


def phoneLifeLine():
    mixer.music.stop()
    mixer.music.load('calling.mp3')
    mixer.music.play()
    callButton.place(x=70, y=260)
    phoneLifelineButton.config(image=phoneImagex,state=DISABLED)

def phoneClick():
    mixer.music.load('kbc.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0)
    for i in range(15):
        if questionArea.get(1.0, 'end-1c') == questions[i]:
            try:
                tts = gTTS(f'الاجابة هي {correct_answers[i]} ', lang='ar')
                tts.save('answer.mp3')
                os.system('answer.mp3')
                time.sleep(3.5)
            except :
                print("Could not play the voice")
        os.system('TASKKILL /F /IM wmplayer.exe')





correct_answers = ["روسيا", "366", "أبو بكر الصديق", "بيزا", "32", "فدرالي",
                   "فرنك", "بريطانيا", "المدينة المنورة", "الأطلسي", "الناصرة", "عنزة", "dz", "عمرو بن العاص",
                   "أزرق"]


questions = ["ما هي أكبر دولة في العالم ؟",
             "كم عدد أيام السنة الكبيسة ؟",
             "من هو أول الخلفاء الراشدين ؟",
             "المدينة الإيطالية التي تشتهر ببرجها المائل ؟",
             "كم عدد أسنان الإنسان العادي ؟",
             "ما هو نظام الحكم في أمريكا ؟",
             "ما هي عملة غينيا الاستوائية ؟",
             "في أي بلد ظهرت أول دبابة في العالم ؟",
             "ما هي المدينة التي كانت تدعى قديما (يثرب) ؟",
             "على أي محيط تطل مدينة نواكشوط ؟",
             "في أي بلد ولدت الأديبة الفلسطينية مي زيادة ؟",
             "ما هو أنثى الماعز ؟",
             "ما هو نطاق مواقع الإنترنت لدولة الجزائر ؟",
             "من أطلق على مصر لقب أرض الكنانة ؟",
             "لون الدم عادة أحمر ولكن عند حيوان الكركدن غير ذلك فما لون دمه ؟"]

first_option = ["الهند", "354",
                "علي بن أبي طالب", "جنوى",
                "32", "فدرالي",
                "فرنك", "ألمانيا", "الرياض", "الأطلسي",
                "حيفا", "قسعاء",
                "ja", "عبدالله بن مروان", "أزرق"]

second_option = ["أمريكا", "366",
                 "أبو بكر الصديق", "روما ",
                 "30", "ملكي",
                 "ليون", "فرنسا", "مكة المكرمة", "المتوسط",
                 "نابلس", "اتان",
                 "gz",
                 "عمر بن الخطاب", "أخضر"]

third_option = ["الصين", "365",
                "عثمان بن عفان", "بيزا",
                "28", "جمهوري",
                "كواشا", "أمريكا", "حائل", "الهادي",
                "بيت لحم", "أم قشعم",
                "dz",
                "أبو بكلر الصديق", "أصفر"]

fourth_option = ["روسيا", "420",
                 "عمر بن الخطاب", "فينيسيا",
                 "29", "إمارة",
                 "تاكا", "بريطانيا", "المدينة المنورة", "الهندي",
                 "الناصرة",
                 "عنزة",
                 "da", "عمرو بن العاص",
                 "أسود"]

root = Tk()

root.geometry('1270x652+0+0')
root.title("من سيربح المليون")

root.config(bg='black')

#The frames
leftframe = Frame(root,bg="black",padx=90)
leftframe.grid(row=0,column=0)

topframe = Frame(leftframe,bg="black",pady=15)
topframe.grid()

centerframe = Frame(leftframe,bg="black",pady=15)
centerframe.grid(row=1,column=0)

bottomframe = Frame(leftframe)
bottomframe.grid(row=2,column=0)

rightframe = Frame(root,pady=25,padx=50,bg="black")
rightframe.grid(row=0,column=1)

#Image for 50-50 choice
image50 = PhotoImage(file='50-50.png')
image50x = PhotoImage(file='50-50-X.png')
Lifeline50Button = Button(topframe,image = image50,bg="black",bd=0,activebackground = "black",width=180,height=80,command=lifeLine50)
Lifeline50Button.grid(row=0,column=0)

#Image for audience choice
audience = PhotoImage(file='audiencePole.png')
audiencex = PhotoImage(file='audiencePoleX.png')
audiencePoleButton = Button(topframe,image = audience,bg="black",bd=0,activebackground = "black",width=180,height=80,command=audiencePoleLife)
audiencePoleButton.grid(row=0,column=1)

#Image for friend call
phoneImage = PhotoImage(file='phoneAFriend.png')
phoneImagex = PhotoImage(file='phoneAFriendX.png')
phoneLifelineButton = Button(topframe,image = phoneImage,bg="black",bd=0,activebackground = "black",width=180,height=80,command=phoneLifeLine)
phoneLifelineButton.grid(row=0,column=2)

callImage= PhotoImage(file="phone.png")
callButton = Button(root,image=callImage,bd=0,bg="black",
                    activebackground="black",cursor="hand2",command=phoneClick)

#The logo for the game
centerImage = PhotoImage(file='center.png')
logoLabel = Label(centerframe,image = centerImage,bg="black",width=300,height=200)
logoLabel.grid(row=0,column=0)

#The Money Image
amountImage = PhotoImage(file="Picture0.png")
amountLabel = Label(rightframe,image=amountImage,bg="black")
amountLabel.grid(row=0,column=0)

image1 = PhotoImage(file='Picture1.png')
image2 = PhotoImage(file='Picture2.png')
image3 = PhotoImage(file='Picture3.png')
image4 = PhotoImage(file='Picture4.png')
image5 = PhotoImage(file='Picture5.png')
image6 = PhotoImage(file='Picture6.png')
image7 = PhotoImage(file='Picture7.png')
image8 = PhotoImage(file='Picture8.png')
image9 = PhotoImage(file='Picture9.png')
image10 = PhotoImage(file='Picture10.png')
image11 = PhotoImage(file='Picture11.png')
image12 = PhotoImage(file='Picture12.png')
image13 = PhotoImage(file='Picture13.png')
image14 = PhotoImage(file='Picture14.png')
image15 = PhotoImage(file='Picture15.png')

images = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12, image13
    , image14, image15]

#The layout of the questions
layoutImage = PhotoImage(file="lay.png")
layoutLabel = Label(bottomframe,image=layoutImage,bg="black")
layoutLabel.grid(row=0,column=0)

#Question Area
questionArea = Text(bottomframe,font=('arial',18,'bold'),width=25,height=2,wrap="word",bg="black",fg="white",bd=0)
questionArea.place(x=170,y=10)

questionArea.insert(END,questions[0])

#Label of Choice A
labelA = Label(bottomframe,text="A: ",bg="black",fg="white",font=('arial',16,"bold"))
labelA.place(x=60,y=110)
optionButton1 = Button(bottomframe,text=first_option[0],font=("arial",18,"bold"),bg="black",fg="white",bd=0
                         ,activebackground="black",activeforeground="white",cursor="hand2")
optionButton1.place(x=100,y=100)

#Label of Choice B
labelB = Label(bottomframe,text="B: ",bg="black",fg="white",font=('arial',16,"bold"))
labelB.place(x=330,y=110)
optionButton2 = Button(bottomframe,text=second_option[0],font=("arial",18,"bold"),bg="black",fg="white",bd=0
                         ,activebackground="black",activeforeground="white",cursor="hand2")
optionButton2.place(x=370,y=100)

#Label of Choice C
labelC = Label(bottomframe,text="C: ",bg="black",fg="white",font=('arial',16,"bold"))
labelC.place(x=60,y=190)
optionButton3 = Button(bottomframe,text=third_option[0],font=("arial",18,"bold"),bg="black",fg="white",bd=0
                         ,activebackground="black",activeforeground="white",cursor="hand2")
optionButton3.place(x=100,y=180)

#Label of Choice D
labelD = Label(bottomframe,text="D: ",bg="black",fg="white",font=('arial',16,"bold"))
labelD.place(x=330,y=190)
optionButton4 = Button(bottomframe,text=fourth_option[0],font=("arial",18,"bold"),bg="black",fg="white",bd=0
                         ,activebackground="black",activeforeground="white",cursor="hand2")
optionButton4.place(x=370,y=180)

#Progress bar for the correct answer
progressbarA = Progressbar(root,orient=VERTICAL,length=120)
progressbarB = Progressbar(root,orient=VERTICAL,length=120)
progressbarC = Progressbar(root,orient=VERTICAL,length=120)
progressbarD = Progressbar(root,orient=VERTICAL,length=120)

progressbarLabel = Label(root,text="A",font=("arial",20,"bold"),bg="black",fg="white")
progressbarLabel1 = Label(root,text="B",font=("arial",20,"bold"),bg="black",fg="white")
progressbarLabel2 = Label(root,text="C",font=("arial",20,"bold"),bg="black",fg="white")
progressbarLabel3 = Label(root,text="D",font=("arial",20,"bold"),bg="black",fg="white")


optionButton1.bind('<Button-1>',select)
optionButton2.bind('<Button-1>',select)
optionButton3.bind('<Button-1>',select)
optionButton4.bind('<Button-1>',select)



root.mainloop()