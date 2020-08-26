from tkinter import *
import pygame
import pyttsx3

pygame.init()
engine = pyttsx3.init()
#to low the speed of saying
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

root = Tk()
root.title("Alphabet Application")
root.geometry("1352x652+100+100")
root.config(bg = "white")

frame1 = Frame(root)
frame1.grid()

canvas = Canvas(frame1,height=120, width=160, bg='white')
canvas.grid(row=1,column=3)

#keeping image to canvas
img = PhotoImage(file = 'Icon.png')
image = canvas.create_image(85,62,image = img)

str1 = StringVar()
str1.set("Welcome to Rojivadiya Academy")

# heading in frame
display = Entry(frame1, textvariable = str1, font = ('Arial',44,'bold'),bg='blue',fg='white',bd=14,width=40,justify = CENTER)
display.grid(row=0,column=0,columnspan=7,pady=1)

#creating command for A
imgA = PhotoImage(file = 'Apple.png')
def A():
    str1.set('A for Apple')
    canvas.create_image(85, 62, image=imgA)
    engine.say('A for Apple')
    engine.runAndWait()


#creating command for B
imgB = PhotoImage(file = 'Banana.png')
def B():
    str1.set('B for Banana')
    canvas.create_image(85,62,image = imgB)
    engine.say('B for Banana')
    engine.runAndWait()

#creating command for A
imgC = PhotoImage(file = 'Cocoa.png')
def C():
    str1.set('C for Cocoa')
    canvas.create_image(85,62,image = imgC)
    engine.say('C for Cocoa')
    engine.runAndWait()

#creating command for B
imgD = PhotoImage(file = 'Damson.png')
def D():
    str1.set('D for Damson')
    canvas.create_image(85,62,image = imgD)
    engine.say('D for Damson')
    engine.runAndWait()

#creating command for A
imgE = PhotoImage(file = 'Elderberry.png')
def E():
    str1.set('E for Elderberry')
    canvas.create_image(85,62,image = imgE)
    engine.say('E for Elderberry')
    engine.runAndWait()

#creating command for B
imgF = PhotoImage(file = 'Fig.png')
def F():
    str1.set('F for Fig')
    canvas.create_image(85,62,image = imgF)
    engine.say('F for Fig')
    engine.runAndWait()

#creating command for A
imgG = PhotoImage(file = 'Guava.png')
def G():
    str1.set('G for Guava')
    canvas.create_image(85,62,image = imgG)
    engine.say('G for Guava')
    engine.runAndWait()

#creating command for B
imgH = PhotoImage(file = 'HuckleBerry.png')
def H():
    str1.set('H for HuckleBerry')
    canvas.create_image(85,62,image = imgH)
    engine.say('H for HuckleBerry')
    engine.runAndWait()

#creating command for A
imgI = PhotoImage(file = 'Ita palm.png')
def I():
    str1.set('I for Ita palm')
    canvas.create_image(85,62,image = imgI)
    engine.say('I for Ita palm')
    engine.runAndWait()

#creating command for B
imgJ = PhotoImage(file = 'Jujube.png')
def J():
    str1.set('J for Jujube')
    canvas.create_image(85,62,image = imgJ)
    engine.say('J for Jujube')
    engine.runAndWait()

#creating command for A
imgK = PhotoImage(file = 'Kumquat.png')
def K():
    str1.set('K for Kumquat')
    canvas.create_image(85,62,image = imgK)
    engine.say('K for Kumquat')
    engine.runAndWait()

#creating command for B
imgL = PhotoImage(file = 'Lime.png')
def L():
    str1.set('L for Lime')
    canvas.create_image(85,62,image = imgL)
    engine.say('L for Lime')
    engine.runAndWait()

#creating command for A
imgM = PhotoImage(file = 'Mango.png')
def M():
    str1.set('M for Mango')
    canvas.create_image(85,62,image = imgM)
    engine.say('M for Mango')
    engine.runAndWait()

#creating command for B
imgN = PhotoImage(file = 'Nance.png')
def N():
    str1.set('N for Nance')
    canvas.create_image(85,62,image = imgN)
    engine.say('N for Nance')
    engine.runAndWait()

#creating command for A
imgO = PhotoImage(file = 'Orange.png')
def O():
    str1.set('O for Orange')
    canvas.create_image(85,62,image = imgO)
    engine.say('O for Orange')
    engine.runAndWait()

#creating command for B
imgP = PhotoImage(file = 'Papaya.png')
def P():
    str1.set('P for Papaya')
    canvas.create_image(85,62,image = imgP)
    engine.say('P for Papaya')
    engine.runAndWait()

#creating command for A
imgQ = PhotoImage(file = 'Quince.png')
def Q():
    str1.set('Q for Quince')
    canvas.create_image(85,62,image = imgQ)
    engine.say('Q for Quince')
    engine.runAndWait()

#creating command for B
imgT = PhotoImage(file = 'Tamarind.png')
def T():
    str1.set('T for Tamarind')
    canvas.create_image(85,62,image = imgT)
    engine.say('T for Tamarind')
    engine.runAndWait()

#creating command for A
imgR = PhotoImage(file = 'RaspBerry.png')
def R():
    str1.set('R for RaspBerry')
    canvas.create_image(85,62,image = imgR)
    engine.say('R for RaspBerry')
    engine.runAndWait()


#creating command for B
imgS = PhotoImage(file = 'StrawBerry.png')
def S():
    str1.set('S for StrawBerry')
    canvas.create_image(85,62,image = imgS)
    engine.say('S for StrawBerry')
    engine.runAndWait()

#creating command for A
imgU = PhotoImage(file = 'Ugli.png')
def U():
    str1.set('U for Ugli')
    canvas.create_image(85,62,image = imgU)
    engine.say('U for Ugli')
    engine.runAndWait()

#creating command for B
imgV = PhotoImage(file = 'Vanilla.png')
def V():
    str1.set('V for Vanilla')
    canvas.create_image(85,62,image = imgV)
    engine.say('V for Vanilla')
    engine.runAndWait()

#creating command for A
imgW = PhotoImage(file = 'Watermelon.png')
def W():
    str1.set('W for Watermelon')
    canvas.create_image(85,62,image = imgW)
    engine.say('W for Watermelon')
    engine.runAndWait()

#creating command for B
imgX = PhotoImage(file = 'Xigua.png')
def X():
    str1.set('X for Xigua')
    canvas.create_image(85,62,image = imgX)
    engine.say('X for Xigua')
    engine.runAndWait()

#creating command for A
imgY = PhotoImage(file = 'Yuzu.png')
def Y():
    str1.set('Y for Yuzu')
    canvas.create_image(85,62,image = imgY)
    engine.say('Y for Yuzu')
    engine.runAndWait()

#creating command for B
imgZ = PhotoImage(file = 'Zucchini.png')
def Z():
    str1.set('Z for Zucchini')
    canvas.create_image(85,62,image = imgZ)
    engine.say('Z for Zucchini')
    engine.runAndWait()

#creating clear command
def clear1():
    str1.set('Welcome to Rojivadiya Academy')
    canvas.create_image(85,62,image = img)
    engine.say('Welcome to Rojivadiya Academy')
    engine.runAndWait()


#creating buttons from a to f
btnA = Button(frame1,height=3,width=10,text = 'A',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = A).grid(row=1,column=0)
btnB = Button(frame1,height=3,width=10,text = 'B',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = B).grid(row=1,column=1)
btnC = Button(frame1,height=3,width=10,text = 'C',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = C).grid(row=1,column=2)
btnD = Button(frame1,height=3,width=10,text = 'D',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = D).grid(row=1,column=4)
btnE = Button(frame1,height=3,width=10,text = 'E',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = E).grid(row=1,column=5)
btnF = Button(frame1,height=3,width=10,text = 'F',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = F).grid(row=1,column=6)

#creating buttons from g to m
btnG = Button(frame1,height=3,width=10,text = 'G',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = G).grid(row=2,column=0)
btnH = Button(frame1,height=3,width=10,text = 'H',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = H).grid(row=2,column=1)
btnI = Button(frame1,height=3,width=10,text = 'I',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = I).grid(row=2,column=2)
btnJ = Button(frame1,height=3,width=10,text = 'J',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = J).grid(row=2,column=3)
btnK = Button(frame1,height=3,width=10,text = 'K',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = K).grid(row=2,column=4)
btnL = Button(frame1,height=3,width=10,text = 'L',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = L).grid(row=2,column=5)
btnM = Button(frame1,height=3,width=10,text = 'M',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = M).grid(row=2,column=6)

#creating buttons from n to t
btnN = Button(frame1,height=3,width=10,text = 'N',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = N).grid(row=3,column=0)
btnO = Button(frame1,height=3,width=10,text = 'O',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = O).grid(row=3,column=1)
btnP = Button(frame1,height=3,width=10,text = 'P',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = P).grid(row=3,column=2)
btnQ = Button(frame1,height=3,width=10,text = 'Q',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = Q).grid(row=3,column=3)
btnR = Button(frame1,height=3,width=10,text = 'R',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = R).grid(row=3,column=4)
btnS = Button(frame1,height=3,width=10,text = 'S',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = S).grid(row=3,column=5)
btnT = Button(frame1,height=3,width=10,text = 'T',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = T).grid(row=3,column=6)

#creating buttons from u to z and clear button
btnU = Button(frame1,height=3,width=10,text = 'U',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = U).grid(row=4,column=0)
btnV = Button(frame1,height=3,width=10,text = 'V',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = V).grid(row=4,column=1)
btnW = Button(frame1,height=3,width=10,text = 'W',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = W).grid(row=4,column=2)
btnX = Button(frame1,height=3,width=10,text = 'X',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = X).grid(row=4,column=3)
btnY = Button(frame1,height=3,width=10,text = 'y',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = Y).grid(row=4,column=4)
btnZ = Button(frame1,height=3,width=10,text = 'Z',bg='orange',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = Z).grid(row=4,column=5)
btnclear = Button(frame1,height=3,width=10,text = 'Clear',bg='blue',fg='white',bd=4,pady=1,font = ('Arial',21,'bold'), command = clear1).grid(row=4,column=6)


root.mainloop()
