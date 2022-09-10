from tkinter import *
from PIL import Image,ImageTk
from random import randint

#main window
root=Tk()
root.title("Hand Cricket")
root.configure(background="purple")
#canvas=Canvas(root,width=200,height=200)
#canvas.pack()
width=200
height=200

#pictures
one_img=ImageTk.PhotoImage(Image.open("C:\\Users\\varsh\\Desktop\\images\\one.png").resize((width,height),Image.ANTIALIAS))
two_img=ImageTk.PhotoImage(Image.open("C:\\Users\\varsh\\Desktop\\images\\two.png").resize((width,height),Image.ANTIALIAS))
three_img=ImageTk.PhotoImage(Image.open("C:\\Users\\varsh\\Desktop\\images\\three.png").resize((width,height),Image.ANTIALIAS))
four_img=ImageTk.PhotoImage(Image.open("C:\\Users\\varsh\\Desktop\\images\\four.png").resize((width,height),Image.ANTIALIAS))
five_img=ImageTk.PhotoImage(Image.open("C:\\Users\\varsh\\Desktop\\images\\five.png").resize((width,height),Image.ANTIALIAS))
six_img=ImageTk.PhotoImage(Image.open("C:\\Users\\varsh\\Desktop\\images\\six.png").resize((width,height),Image.ANTIALIAS))

#insert picture
user_label=Label(root, image=one_img)
comp_label=Label(root, image=one_img)
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=6)

#canvas.create_image(0,0, anchor=NW, image=one_img)
#canvas.create_image(10,10, anchor=NW, image=two_img)

#scores
playerScore=Label(root,text=0,font=200,bg="yellow",fg="black")
computerScore=Label(root,text=0,font=200,bg="yellow",fg="black")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicators
user_indicator=Label(root,font=50,text="You")
comp_indicator=Label(root,font=50,text="Computer")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg=Label(root,font=50,bg="yellow",fg="black",text="lets begin!!")
msg.grid(row=4,column=2)

#update message
def updateMessage(x):
    msg["text"]=x

#update user score
def updateUserScore():
    score=int(playerScore["text"])
    score+=1
    playerScore["text"]=str(score)

#update computer score
def updateCompScore():
    score=int(computerScore["text"])
    score+=1
    computerScore["text"]=str(score)

 #check winner
def checkWin(player,computer):
    if player==computer:
        updateMessage("you are out!!")
        updateCompScore()
    else:
        updateMessage("keep scoring")
        updateUserScore()
    return player 

#update choices
choices=["one","two","three","four","five","six"]
def updateChoice(x):


#for computer
    compChoice=choices[randint(0,5)]
    if compChoice=="one":
        comp_label.configure(image=one_img)
    elif compChoice=="two":
        comp_label.configure(image=two_img)
    elif compChoice=="three":
        comp_label.configure(image=three_img)
    elif compChoice=="four":
        comp_label.configure(image=four_img)
    elif compChoice=="five":
        comp_label.configure(image=five_img)
    else:
        comp_label.configure(image=six_img)







#for user
    if x=="one":
        user_label.configure(image=one_img)
    elif x=="two":
        user_label.configure(image=two_img)
    elif x=="three":
        user_label.configure(image=three_img)
    elif x=="four":
        user_label.configure(image=four_img)
    elif x=="five":
        user_label.configure(image=five_img)
    else:
        user_label.configure(image=six_img)
    checkWin(x,compChoice)    




#buttons
one=Button(root,width=10,height=2,text="ONE",bg="green",fg="white",command=lambda:updateChoice("one")).grid(row=2,column=1)
two=Button(root,width=10,height=2,text="TWO",bg="green",fg="white",command=lambda:updateChoice("two")).grid(row=2,column=2)
three=Button(root,width=10,height=2,text="THREE",bg="green",fg="white",command=lambda:updateChoice("three")).grid(row=2,column=3)
four=Button(root,width=10,height=2,text="FOUR",bg="green",fg="white",command=lambda:updateChoice("four")).grid(row=3,column=1)
five=Button(root,width=10,height=2,text="FIVE",bg="green",fg="white",command=lambda:updateChoice("five")).grid(row=3,column=2)
six=Button(root,width=10,height=2,text="SIX",bg="green",fg="white",command=lambda:updateChoice("six")).grid(row=3,column=3)






root.mainloop()