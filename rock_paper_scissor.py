from tkinter import *
from PIL import Image,ImageTk
from random import randint

#main window
root=Tk()
root.title("Rock Paper Scissor")
root.configure(background="purple")
#canvas=Canvas(root,width=200,height=200)
#canvas.pack()
width=200
height=200

#pictures
rock_img=ImageTk.PhotoImage(Image.open("C:\\Users\\varsh\\Desktop\\images\\rock.jpg").resize((width,height),Image.ANTIALIAS))
paper_img=ImageTk.PhotoImage(Image.open("C:\\Users\\varsh\\Desktop\\images\\paper.jpg").resize((width,height),Image.ANTIALIAS))
scissor_img=ImageTk.PhotoImage(Image.open("C:\\Users\\varsh\\Desktop\\images\\scissor.jpg").resize((width,height),Image.ANTIALIAS))


#insert picture
user_label=Label(root, image=rock_img)
comp_label=Label(root, image=rock_img)
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
        updateMessage("It is a Tie!!")
    elif player=="rock":
        if computer=="paper":
            updateMessage("computer gets a point!")
            updateCompScore()
        else:
            updateMessage("you get a point!")
            updateUserScore()
    elif player=="paper":
        if computer=="scissor":
            updateMessage("computer gets a point!")
            updateCompScore()
        else:
            updateMessage("you get a point!")
            updateUserScore() 
    elif player=="scissor":
        if computer=="rock":
            updateMessage("computer gets a point!") 
            updateCompScore() 
        else:
            updateMessage("you get a point!") 
            updateUserScore()
    else:
        pass                    



#update choices
choices=["rock","paper","scissor"]
def updateChoice(x):


#for computer
    compChoice=choices[randint(0,2)]
    if compChoice=="rock":
        comp_label.configure(image=rock_img)
    elif compChoice=="paper":
        comp_label.configure(image=paper_img)
    elif compChoice=="scissor":
        comp_label.configure(image=scissor_img)
    

#for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    elif x=="scissor":
        user_label.configure(image=scissor_img)
    
    checkWin(x,compChoice)    




#buttons
rock=Button(root,width=10,height=2,text="ROCK",bg="green",fg="white",command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper=Button(root,width=10,height=2,text="PAPER",bg="green",fg="white",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissor=Button(root,width=10,height=2,text="SCISSOR",bg="green",fg="white",command=lambda:updateChoice("scissor")).grid(row=2,column=3)






root.mainloop()