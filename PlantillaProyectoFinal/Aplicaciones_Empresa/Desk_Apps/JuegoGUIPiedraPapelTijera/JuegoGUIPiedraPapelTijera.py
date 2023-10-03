import tkinter as tk 
from tkinter import Tk 
from PIL import ImageTk, Image 
import random


root = Tk()
root.geometry("550x350")
root.title("Rock Paper Scissors Game")

# images links
# https://pixabay.com/vectors/certificate-paper-parchment-roll-154169/
# https://pixabay.com/vectors/stone-rock-nature-pebble-zen-576268/
# https://pixabay.com/vectors/scissors-cut-hairdresser-1297454/
# https://pixabay.com/vectors/rock-paper-scissors-rock-hand-296854/


rock = "/home/pablo/Documentos/ParaProyectos/CTPAMM/EmpresaFabricaSoftwareEducativo/PlantillaProyectoFinal/Aplicaciones_Empresa/Desk_Apps/JuegoGUIPiedraPapelTijera/rock-v.png"
paper = "/home/pablo/Documentos/ParaProyectos/CTPAMM/EmpresaFabricaSoftwareEducativo/PlantillaProyectoFinal/Aplicaciones_Empresa/Desk_Apps/JuegoGUIPiedraPapelTijera/paper-v.png"
scissors = "/home/pablo/Documentos/ParaProyectos/CTPAMM/EmpresaFabricaSoftwareEducativo/PlantillaProyectoFinal/Aplicaciones_Empresa/Desk_Apps/JuegoGUIPiedraPapelTijera/scissors-v.png"
rock_hand = "/home/pablo/Documentos/ParaProyectos/CTPAMM/EmpresaFabricaSoftwareEducativo/PlantillaProyectoFinal/Aplicaciones_Empresa/Desk_Apps/JuegoGUIPiedraPapelTijera/rock.png"

player_wins = 0
computer_wins = 0

img1 = Image.open(rock)
img1 = img1.resize((100,100), Image.ANTIALIAS)
img_rock = ImageTk.PhotoImage(img1)
lbl_rock = tk.Label(root,image=img_rock, borderwidth=1, relief="solid")

img2 = Image.open(paper)
img2 = img2.resize((100,100), Image.ANTIALIAS)
img_paper = ImageTk.PhotoImage(img2)
lbl_paper = tk.Label(root,image=img_paper, borderwidth=1, relief="solid")

img3 = Image.open(scissors)
img3 = img3.resize((100,100), Image.ANTIALIAS)
img_scissors = ImageTk.PhotoImage(img3)
lbl_scissors = tk.Label(root,image=img_scissors, borderwidth=1, relief="solid")

img4 = Image.open(rock)
img4 = img4.resize((200,200), Image.ANTIALIAS)
img_rock_200 = ImageTk.PhotoImage(img4)

img5 = Image.open(paper)
img5 = img5.resize((200,200), Image.ANTIALIAS)
img_paper_200 = ImageTk.PhotoImage(img5)

img6 = Image.open(scissors)
img6 = img6.resize((200,200), Image.ANTIALIAS)
img_scissors_200 = ImageTk.PhotoImage(img6)

img7 = Image.open(rock_hand)
img7 = img7.resize((200,200), Image.ANTIALIAS)
img_rock_hand = ImageTk.PhotoImage(img7)

lbl_player = tk.Label(root,image=img_rock_hand)
lbl_computer = tk.Label(root,image=img_rock_hand)
lbl_score = tk.Label(root,text="0 / 0", font=("Arial",24))


lbl_player.grid(row=0,column=0)
lbl_score.grid(row=0,column=1)
lbl_computer.grid(row=0,column=2)

lbl_rock.grid(row=1,column=0)
lbl_paper.grid(row=1,column=1)
lbl_scissors.grid(row=1,column=2)


pics_list = [img_rock_200,img_paper_200,img_scissors_200]

# create a function to get the winner
def getWinner(pic1,pic2):
    global player_wins, computer_wins
    if pic1 == pic2:
        print("Draw")
    elif pic1 == img_rock_200:
        if pic2 == img_scissors_200:
            print("Player Win")
            player_wins += 1
        elif pic2 == img_paper_200:
            print("Computer Win")
            computer_wins += 1

    elif pic1 == img_paper_200:
        if pic2 == img_rock_200:
            print("Player Win")
            player_wins += 1
        elif pic2 == img_scissors_200:
            print("Computer Win")
            computer_wins += 1
    
    elif pic1 == img_scissors_200:
        if pic2 == img_paper_200:
            print("Player Win")
            player_wins += 1
        elif pic2 == img_rock_200:
            print("Computer Win")
            computer_wins += 1

    lbl_score['text'] = str(player_wins) + ' / ' + str(computer_wins)


# create a function to display the image selected by the player
# display a random pic from the list for the computer
def displayImage(img):
    if img == 'r':
        lbl_player['image'] = img_rock_200
        computer_pic = random.choice(pics_list)
        lbl_computer['image'] = computer_pic
        getWinner(img_rock_200, computer_pic)
    
    elif img == 'p':
        lbl_player['image'] = img_paper_200
        computer_pic = random.choice(pics_list)
        lbl_computer['image'] = computer_pic
        getWinner(img_paper_200, computer_pic)
        
    elif img == 's':
        lbl_player['image'] = img_scissors_200
        computer_pic = random.choice(pics_list)
        lbl_computer['image'] = computer_pic
        getWinner(img_scissors_200, computer_pic)




lbl_rock.bind("<Button-1>", lambda abc : displayImage('r'))
lbl_paper.bind("<Button-1>", lambda abc : displayImage('p'))
lbl_scissors.bind("<Button-1>", lambda abc : displayImage('s'))


root.mainloop()