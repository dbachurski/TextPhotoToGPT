from EdgeGPT.EdgeUtils import Query, Cookie
import json

class Chatbot:

    def askquestion(self, mode):

        with open('output.txt', 'r') as f:
            ask = f.read()
            if mode == 'test':
                message = "I'm going to check you with a single choice test with answers a, b, c, d. Its is important. Do not search for informations in web!\n" + ask
            elif mode == 'normal':
                message = "Its is important. Do not search for informations in web!\n" + ask
                #message =  ask  # allow to search in internet
        q = Query(
            message,
            style='precise',
            cookie_file="./bing_cookies_cos.json")

        print(q)


chatbot = Chatbot()