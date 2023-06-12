import customtkinter as ctk
import tkinter as tk
import sys
import threading
from GrapScreen import grap
from ReadText import read
from Chatbot import chatbot

def redirect_output(text_widget):
    def write(text):
        text_widget.configure(state='normal')
        text_widget.insert('end', text)
        text_widget.configure(state='disabled')
    sys.stdout.write=write
    sys.stdout.flush=lambda: None

def set_mode(new_mode):
    global mode
    mode = new_mode
    redirect_output(text)
    thread = threading.Thread(target=main)
    thread.start()

def main():
    if not grap.start_listener():
        read.read(grap.file_name)
        chatbot.askquestion(mode)  # 'test' or 'normal'

root = ctk.CTk()

mode = 'Normal'

root=ctk.CTk()
root.geometry('900x600')
root.title('PhotoTextToGPT')
ctk.set_appearance_mode('dark')


title_label = ctk.CTkLabel(root, text='PhotoTextToGPT', font=ctk.CTkFont(size=30, weight='bold'))
title_label.pack(padx=10, pady=20)

label = ctk.CTkLabel(root, text='Set Mode:', font=ctk.CTkFont('Raleway', size=15))
label.pack(padx=10, pady=20)

#button = ctk.CTkButton(root, text='Test', fg_color = '#d156cf', hover_color='red', command=lambda: set_mode('test'))
#button.place(relx=0.2, rely=0.25, relheight=0.1, relwidth=0.2)
button = tk.Button(root, text='Test', font='Raleway', bg = '#d156cf', fg='white', command=lambda: set_mode('test'))
button.place(relx=0.2, rely=0.25, relheight=0.1, relwidth=0.2)

#button2 = ctk.CTkButton(root, text='Normal', fg_color = '#d156cf',  command=lambda: set_mode('normal'))
#button2.place(relx=0.6, rely=0.25, relheight=0.1, relwidth=0.2)
button2 = tk.Button(root, text='Normal', textvariable=tk.StringVar(), font='Raleway', bg = '#d156cf', fg='white', command=lambda: set_mode('normal'))
button2.place(relx=0.6, rely=0.25, relheight=0.1, relwidth=0.2)

text = tk.Text(root, fg='#00FF00', bg='black')
text.place(relx=0.05, rely=0.6 , relwidth = 0.9 , relheight=0.33)

root.mainloop()






