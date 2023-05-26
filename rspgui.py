from tkinter import *
import random

class rsp:

    def rock():

        if count != 5:

            display_label_player.config(text = "👊", font = font)
            vs_label.config(text = "vs", font = font)
            display_label_bot.config(text = random.choice(bot_list), font = font)
            display_label_player.after(1000, clear_label)
            check_win(display_label_player["text"], display_label_bot["text"]) 

        else :
            Result_button.place(x = 125, y = 150)

    def scissors():

        if count != 5:
            display_label_player.config(text = "✌️", font = font)
            vs_label.config(text = "vs", font = font)
            display_label_bot.config(text = random.choice(bot_list), font = font)
            display_label_player.after(1000, clear_label)
            check_win(display_label_player["text"], display_label_bot["text"])

        else :
            Result_button.place(x = 125, y = 150)

    def paper():

        if count != 5:

            display_label_player.config(text = "🖐️", font = font)
            vs_label.config(text = "vs", font = font)
            display_label_bot.config(text = random.choice(bot_list), font = font)
            display_label_player.after(1000, clear_label)
            check_win(display_label_player["text"], display_label_bot["text"])

        else :
            Result_button.place(x = 125, y = 150)

def clear_label():
    display_label_player.config(text = "")
    display_label_bot.config(text = "")
    vs_label.config(text = "")

def check_win(x, y):

    global score_bot, score_player, count

    if x == y:
        result_label.config(text = "It's a tie!!", font = font)
        result_label.after(1000, lambda:result_label.config(text = ""))
        count += 1
    
    elif x == "👊" and y == "✌️":
        result_label.config(text = "You win!!", font = font)
        result_label.after(1000, lambda:result_label.config(text = ""))
        score_player += 1
        count += 1

    elif x == "👊" and y == "🖐️":
        result_label.config(text = "You lose!!", font = font)
        result_label.after(1000, lambda:result_label.config(text = ""))
        score_bot += 1
        count += 1
    
    elif x == "✌️" and y == "👊":
        result_label.config(text = "You lose!!", font = font)
        result_label.after(1000, lambda:result_label.config(text = ""))
        score_bot += 1
        count += 1

    elif x == "✌️" and y == "🖐️":
        result_label.config(text = "You win!!", font = font)
        result_label.after(1000, lambda:result_label.config(text = ""))
        score_player += 1
        count += 1

    elif x == "🖐️" and y == "👊":
        result_label.config(text = "You win!!", font = font)
        result_label.after(1000, lambda:result_label.config(text = ""))
        score_player += 1
        count += 1

    elif x == "🖐️" and y == "✌️":
        result_label.config(text = "You lose!!")
        result_label.after(1000, lambda:result_label.config(text = ""))    
        score_bot += 1
        count += 1

def show_result():
    Result_button.destroy()
    if score_player > score_bot:
        result_label.config(text = "You are winner", font = ("system", 27, "bold"))
        score_label.config(text = str(score_player) + " - " + str(score_bot), font = ("system", 27, "bold"))
        result_label.place(x = 93, y = 150)
        score_label.place(x = 148, y = 190)

    elif score_bot > score_player:
        result_label.config(text = "You are loser", font = ("system", 27, "bold"))
        score_label.config(text = str(score_player) + " - " + str(score_bot), font = ("system", 27, "bold"))
        result_label.place(x = 93, y = 150)
        score_label.place(x = 148, y = 190)

    else:
        result_label.config(text = "It's a tie!!\nno one win", font = ("system", 27, "bold"))
        score_label.config(text = str(score_player) + " - " + str(score_bot), font = ("system", 27, "bold"))
        result_label.place(x = 93, y = 150)
        score_label.place(x = 148, y = 190)


bot_list = ["👊", "✌️", "🖐️"]
font = ("System", 30, "bold")
score_player = 0
score_bot = 0
count = 0

app = Tk()
app.minsize(350, 450)
app.maxsize(350, 450)
app.title("Rock Scissors Paper Game")

# All label
title_label = Label(app, text = "Choose your choice", pady = 10, font = ("System", 30, "bold"))
display_label_player = Label(app, text = "")
display_label_bot = Label(app, text = "")
vs_label = Label(app, text = "")
result_label = Label(app, text = "")
score_label = Label(app, text = "")

# All button 
Rock_button = Button(app, text = "👊", width = 1, font = font, command = rsp.rock)
Scissors_button = Button(app, text = "✌️", width = 1, font = font, command = rsp.scissors)
Paper_button = Button(app, text = "🖐️", width = 1, font = font, command = rsp.paper)
Result_button = Button(app, text = "Show reult",font = ("system", 15, "bold"), command = show_result)

# Label place 
title_label.pack()
display_label_player.place(x = 128, y = 130)
display_label_bot.place(x = 193, y = 130)
vs_label.place(x = 162, y = 130)
result_label.place(x = 117, y = 170)

# Button place
Rock_button.place(x = 72, y = 70)
Scissors_button.place(x = 152, y = 70)
Paper_button.place(x = 232, y = 70)

app.mainloop()