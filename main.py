from GrapScreen import grap
from ReadText import read
from Chatbot import chatbot

grap.start_listener()
read.read(grap.file_name)
chatbot.askquestion('test')  # 'test' or 'normal'
