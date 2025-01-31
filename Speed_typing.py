from tkinter import *
import random
from tkinter import ttk
from time import sleep
import threading

# FUNCTIONALITIES
def start():
    thread1 = threading.Thread(target=start_timer)
    thread1.start()

    thread2 = threading.Thread(target=count)
    thread2.start()

# Global declarations
totaltime = 60
time = 0
wrong_words = 0
elapsedtimeinminutes = 0

def reset():
    global time, elapsedtimeinminutes, wrong_words
    time = 0
    elapsedtimeinminutes = 0
    wrong_words = 0
    start_button.config(state=NORMAL)
    reset_button.config(state=DISABLED)  
    textarea.config(state=NORMAL)
    textarea.delete(1.0, END)
    textarea.config(state=DISABLED)
    timer_label.config(text='60')
    accuracy_percent_label.config(text='0%')
    total_words_count_label.config(text='0')
    wrong_words_count_label.config(text='0')
    wpm_count_label.config(text='0')

def start_timer():
    start_button.config(state=DISABLED)
    global time
    textarea.config(state=NORMAL)
    textarea.focus()

    for time in range(1, 61):
        remainingtime = totaltime - time
        timer_label.config(text=remainingtime)
        sleep(1)
        root.update()

    textarea.config(state=DISABLED)
    reset_button.config(state=NORMAL)

def count():
    global wrong_words
    while time != totaltime:
        entered_paragraph = textarea.get(1.0, END).split()
        totalwords = len(entered_paragraph)

    total_words_count_label.config(text=totalwords)
    para_word_list = label_paragraph['text'].split()

    for pair in list(zip(para_word_list, entered_paragraph)):
        if pair[0] != pair[1]:
            wrong_words += 1

    wrong_words_count_label.config(text=wrong_words)

    elapsedtimeinminutes = time / 60
    wpm = int((totalwords - wrong_words) / elapsedtimeinminutes)
    wpm_count_label.config(text=wpm)
    
    gross_wpm = totalwords / elapsedtimeinminutes
    accuracy = (wpm / gross_wpm) * 100 if gross_wpm > 0 else 0
    accuracy = round(accuracy)
    accuracy_percent_label.config(text=f"{accuracy}%")

# GUI SECTION
root = Tk()
root.title("Speed Typing Test")
root.geometry('850x600+200+10')
root.resizable(False, False)

mainframe = Frame(root, bd=4)
mainframe.grid()

titleframe = Frame(mainframe, bg='grey')
titleframe.grid()

titleLabel = Label(titleframe, text='SPEED TYPING', font=('times', 28, 'bold'), bg='black', fg='white', width=38)
titleLabel.grid(pady=5)

paragraph_frame = Frame(mainframe)
paragraph_frame.grid(row=1, column=0)

paragraph_list = [
    'The sun dipped below the horizon, painting the sky in hues of orange and pink...',
    'The waves crashed against the shore, a rhythmic melody of the sea...',
    "The city streets hummed with activity, a constant stream of people and cars...",
    "The jagged peaks of the mountains soared into the sky, their snow-capped summits...",
    "The aroma of freshly brewed coffee filled the cozy café as patrons chatted...",
    "The ancient castle loomed majestically against the backdrop of the rugged mountains...",
    "The waves crashed against the rocky shore, sending plumes of spray into the air...",
    "Amidst the quiet of the library, the scent of old books hung in the air..."
]

random.shuffle(paragraph_list)

label_paragraph = Label(paragraph_frame, text=paragraph_list[0], wraplength=840, justify=LEFT, font=('times', 16))
label_paragraph.grid(row=0, column=0, pady=8)

textarea_frame = Frame(mainframe)
textarea_frame.grid(row=2, column=0, pady=10)

textarea = Text(textarea_frame, font=('times', 12), width=100, height=10, bd=4, relief=GROOVE, wrap='word', state=DISABLED)
textarea.grid()

frame_output = Frame(mainframe)
frame_output.grid(row=3, column=0)

labels = ["Time", "WPM", "Total Words", "Wrong Words", "Accuracy"]
values = ["60", "0", "0", "0", "0%"]
value_labels = []

for i, label_text in enumerate(labels):
    Label(frame_output, text=label_text, font=('Tahoma', 12, 'bold'), fg='red').grid(row=0, column=i * 2, padx=5)
    lbl = Label(frame_output, text=values[i], font=('Tahoma', 12, 'bold'))
    lbl.grid(row=0, column=i * 2 + 1, padx=5)
    value_labels.append(lbl)

timer_label, wpm_count_label, total_words_count_label, wrong_words_count_label, accuracy_percent_label = value_labels

buttons_frame = Frame(mainframe)
buttons_frame.grid(row=4, column=0)

start_button = ttk.Button(buttons_frame, text='Start', command=start)
start_button.grid(row=0, column=0, padx=10, pady=10)

reset_button = ttk.Button(buttons_frame, text='Reset', state=DISABLED, command=reset)
reset_button.grid(row=0, column=1, padx=10, pady=10)

exit_button = ttk.Button(buttons_frame, text='Exit', command=root.destroy)
exit_button.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()
