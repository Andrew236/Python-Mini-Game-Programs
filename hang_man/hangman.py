from tkinter import *

import random

from tkinter import messagebox

from word_list import words

from string import ascii_uppercase

from sys import exit

game_running = True

def quit_game():
    exit(0)

def play_again_no():
    exit(0)

def play_again_yes(game_running):
    game_running = True
    root.destroy()
    return game_running

while game_running:
    root = Tk()
    root.geometry("600x600")
    root.title("Andrew's Hangman")
   
    letter_text_color = "black"
    #game is going to use and that the user is going to guess
    game_word = random.choice(words).upper()
    letters_guessed = []
    wrong_letters = [1,1,1,1,1,1,1,1,1,1]
    def letter_click(letter,letters_guessed,wrong_letters):

        if letter == "A":
            a_button.config(state="disabled",bg="#909090")

        if letter == "B":
            b_button.config(state="disabled",bg="#909090")

        if letter == "C":
            c_button.config(state="disabled",bg="#909090")

        if letter == "D":
            d_button.config(state="disabled",bg="#909090")

        if letter == "E":
            e_button.config(state="disabled",bg="#909090")

        if letter == "F":
            f_button.config(state="disabled",bg="#909090")

        if letter == "G":
            g_button.config(state="disabled",bg="#909090")

        if letter == "H":
            h_button.config(state="disabled",bg="#909090")

        if letter == "I":
            i_button.config(state="disabled",bg="#909090")

        if letter == "J":
            j_button.config(state="disabled",bg="#909090")

        if letter == "K":
            k_button.config(state="disabled",bg="#909090")

        if letter == "L":
            l_button.config(state="disabled",bg="#909090")

        if letter == "M":
            m_button.config(state="disabled",bg="#909090")

        if letter == "N":
            n_button.config(state="disabled",bg="#909090")

        if letter == "O":
            o_button.config(state="disabled",bg="#909090")

        if letter == "P":
            p_button.config(state="disabled",bg="#909090")

        if letter == "Q":
            q_button.config(state="disabled",bg="#909090")

        if letter == "R":
            r_button.config(state="disabled",bg="#909090")

        if letter == "S":
            s_button.config(state="disabled",bg="#909090")

        if letter == "T":
            t_button.config(state="disabled",bg="#909090")

        if letter == "U":
            u_button.config(state="disabled",bg="#909090")

        if letter == "V":
            v_button.config(state="disabled",bg="#909090")

        if letter == "W":
            w_button.config(state="disabled",bg="#909090")

        if letter == "X":
            x_button.config(state="disabled",bg="#909090")

        if letter == "Y":
            y_button.config(state="disabled",bg="#909090")

        if letter == "Z":
            z_button.config(state="disabled",bg="#909090")

        letters_guessed.append(letter)

        #here I am going to display the words in a hidden fashion
        #then I am going to handle the input if the user
        #guesses the right letter, to be displayed
        if len(game_word) <=5:
            game_letter_x = 0.4
            game_letter_y = 0.6

        elif len(game_word) == 6:
            game_letter_x = 0.38
            game_letter_y = 0.6

        elif len(game_word) == 7:
            game_letter_x = 0.35
            game_letter_y = 0.6

        elif len(game_word) > 7:
            game_letter_x = 0.3
            game_letter_y = 0.6

        else:
            game_letter_x = 0.25
            game_letter_y = 0.6

        check_star_list = []
        for star in game_word:
            check_star_list.append("*")

        if letter not in game_word:
            wrong_letters.pop()

        user_lives = len(wrong_letters)

        print(game_word)
        for i in range(len(game_word)):

            if game_word[i] in letters_guessed:
                game_letter_label = Label(root, text=game_word[i], fg="black")
                game_letter_label.place(relx = game_letter_x, rely = game_letter_y)
                game_letter_label.config(font=("courier new",25))
                game_letter_x += 0.05
                check_star_list.remove("*")
            else:
                game_letter_label = Label(root, text="*", fg="black")
                game_letter_label.place(relx = game_letter_x, rely = game_letter_y)
                game_letter_label.config(font=("courier new",25))
                game_letter_x += 0.05

        lives_label = Label(root, text="Lives:")
        lives_label.place(relx = 0.5, anchor = "n", rely = 0.23)
        lives_label.config(font=("courier new",25))

        if user_lives == 0:
            num_of_lives_label = Label(root, text =user_lives,fg="black")
            num_of_lives_label.place(relx = 0.6, anchor = "n", rely = 0.23)
            num_of_lives_label.config(font=("courier new",25))
            messagebox.showinfo("LOSER", "You lost the game! The word was: {}".format(game_word))
            play_again_label = Label(root, text = "Play Hangman Again?")
            play_again_label.place(relx = 0.5, anchor = "n", rely = 0.43)
            play_again_label.config(font=("courier new",25))
            play_again_yes_button = Button(root,text="yes",width = 5, command = lambda:play_again_yes(game_running))
            play_again_yes_button.place(relx = 0.35,rely=0.5)
            play_again_no_button = Button(root,text="no",width = 5,command = play_again_no)
            play_again_no_button.place(relx = 0.5,rely=0.5)

        if user_lives > 3:

            num_of_lives_label = Label(root, text =user_lives,fg="green")
            num_of_lives_label.place(relx = 0.6, anchor = "n", rely = 0.23)
            num_of_lives_label.config(font=("courier new",25))

        else:
            num_of_lives_label = Label(root, text = user_lives,fg="red")
            num_of_lives_label.place(relx = 0.6, anchor = "n", rely = 0.23)
            num_of_lives_label.config(font=("courier new",25))
        if len(check_star_list) == 0:

                print("you win")
                messagebox.showinfo("WINNER", "CONGRATS\n""YOU MY FRIEND ARE A CHAMPION, AND A WINNER")
                play_again_label = Label(root, text = "Play Hangman Again?")
                play_again_label.place(relx = 0.5, anchor = "n", rely = 0.43)
                play_again_label.config(font=("courier new",25))
                play_again_yes_button = Button(root,text="yes",width = 5, command = lambda:play_again_yes(game_running))
                play_again_yes_button.place(relx = 0.35,rely=0.5)
                play_again_no_button = Button(root,text="no",width = 5,command = play_again_no)
                play_again_no_button.place(relx = 0.5,rely=0.5)
                


    welcome_title = Label(
        root,
        text="Welcome To Hangman",
        fg="#cc6600"
    )

    welcome_title.config(
        font=("Courier", 25)
    )

    welcome_title.place(
        anchor="n",
        relx=0.5,
        rely=0.02
    )

    quit_button = Button(
        root,
        text = "Quit",
        bg="#cc0000",
        fg="white",
        command = lambda: quit_game()
    )

    quit_button.place(
        relx = 0.5,
        rely = 0.95,
        anchor = "n",
        width = 100
    )
    #creation of buttons from a-z

    a_button = Button(root, text="A", width = 5, fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("A",letters_guessed,wrong_letters))
    a_button.place(relx=0.15,rely=0.8)

    b_button = Button(root, text="B", width = 5, fg=letter_text_color,
                    bg="#ff944d",
                    command=lambda: letter_click("B",letters_guessed,wrong_letters))
    b_button.place(relx=0.225,rely=0.8)

    c_button = Button(root, text="C",width=5, fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("C",letters_guessed,wrong_letters))
    c_button.place(relx=0.3,rely=0.8)

    d_button = Button(root, text="D", width = 5, fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("D",letters_guessed,wrong_letters))
    d_button.place(relx=0.375,rely=0.8)

    e_button = Button(root, text="E", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("E",letters_guessed,wrong_letters))

    e_button.place(relx=0.45,rely=0.8)

    f_button = Button(root, text="F", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("F",letters_guessed,wrong_letters))
    f_button.place(relx=0.525,rely=0.8)

    g_button = Button(root, text="G", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("G",letters_guessed,wrong_letters))
    g_button.place(relx=0.6,rely=0.8)

    h_button = Button(root, text="H", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("H",letters_guessed,wrong_letters))
    h_button.place(relx=0.675,rely=0.8)

    i_button = Button(root, text="I", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("I",letters_guessed,wrong_letters))
    i_button.place(relx=0.75,rely=0.8)

    j_button = Button(root, text="J", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("J",letters_guessed,wrong_letters))
    j_button.place(relx=0.15,rely=0.844)

    k_button = Button(root, text="K", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("K",letters_guessed,wrong_letters))
    k_button.place(relx=0.225,rely=0.844)

    l_button = Button(root, text="L",width=5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("L",letters_guessed,wrong_letters))
    l_button.place(relx=0.3,rely=0.844)

    m_button = Button(root, text="M", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("M",letters_guessed,wrong_letters))
    m_button.place(relx=0.375,rely=0.844)

    n_button = Button(root, text="N", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("N",letters_guessed,wrong_letters))
    n_button.place(relx=0.45,rely=0.844)

    o_button = Button(root, text="O", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("O",letters_guessed,wrong_letters))
    o_button.place(relx=0.525,rely=0.844)

    p_button = Button(root, text="P", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("P",letters_guessed,wrong_letters))
    p_button.place(relx=0.6,rely=0.844)

    q_button = Button(root, text="Q", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("Q",letters_guessed,wrong_letters))
    q_button.place(relx=0.675,rely=0.844)

    r_button = Button(root, text="R", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("R",letters_guessed,wrong_letters))
    r_button.place(relx=0.75,rely=0.844)

    s_button = Button(root, text="S", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("S",letters_guessed,wrong_letters))
    s_button.place(relx=0.15,rely=0.888)

    t_button = Button(root, text="T", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("T",letters_guessed,wrong_letters))
    t_button.place(relx=0.225,rely=0.888)

    u_button = Button(root, text="U",width=5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("U",letters_guessed,wrong_letters))
    u_button.place(relx=0.3,rely=0.888)

    v_button = Button(root, text="V", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("V",letters_guessed,wrong_letters))
    v_button.place(relx=0.375,rely=0.888)

    w_button = Button(root, text="W", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("W",letters_guessed,wrong_letters))
    w_button.place(relx=0.45,rely=0.888)

    x_button = Button(root, text="X", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("X",letters_guessed,wrong_letters))

    x_button.place(relx=0.525,rely=0.888)

    y_button = Button(root, text="Y", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("Y",letters_guessed,wrong_letters))
    y_button.place(relx=0.6,rely=0.888)

    z_button = Button(root, text="Z", width = 5,
                            fg=letter_text_color,
                            bg="#ff944d",
                            command=lambda: letter_click("Z",letters_guessed,wrong_letters))
    z_button.place(relx=0.675,rely=0.888)

    star_button = Button(root, text="*", width = 5)
    star_button.place(relx=0.75,rely=0.888)

    # end of the creation of the buttons from a-z


    letter_click('*',letters_guessed,wrong_letters)
    
    
    root.mainloop()
    

    