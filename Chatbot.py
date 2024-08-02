import re
import random
import long_responses as long
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry('700x500+0+0')
        self.root.bind('<Return>', self.enter_func)

        main_frame = Frame(self.root, bd=4, bg='powder blue', width=500)
        main_frame.pack()

        img_chat = Image.open('img.png')
        img_chat = img_chat.resize((150, 70), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img_chat)
        title_lable = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=700, compound=LEFT, image=self.photoimg,
                            text='Chat Me', font=('arial', 30, 'bold'), fg='green', bg='white')
        title_lable.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=('arial', 14),
                         yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root, bd=4, bg='white', width=700)
        btn_frame.pack()

        label1 = Label(btn_frame, text=" Ask Something", font=('arial', 13, 'bold'), fg='green', bg='white')
        label1.grid(row=0, column=0, padx=5, sticky=W)

        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame, textvariable=self.entry, width=40, font=('arial', 17, 'bold'))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)

        self.send = Button(btn_frame, text="Send", command=self.send, font=('arial', 16, 'bold'), width=7, bg='green')
        self.send.grid(row=0, column=2, padx=5, sticky=W)

        self.clear = Button(btn_frame, text="Clear Data", command=self.clear, font=('arial', 16, 'bold'), width=7,
                            bg='green')
        self.clear.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ''
        self.label11 = Label(btn_frame, text=self.msg, font=('arial', 14, 'bold'), fg='red', bg='white')
        self.label11.grid(row=0, column=0, padx=5, sticky=W)

    def message_probability(self, user_message, recognised_words, single_response=False, required_words=[]):
        message_certainty = 0
        has_required_words = True

        for word in user_message:
            if word in recognised_words:
                message_certainty += 1

        percentage = float(message_certainty) / float(len(recognised_words))

        for word in required_words:
            if word not in user_message:
                has_required_words = False
                break

        if has_required_words or single_response:
            return int(percentage * 100)
        else:
            return 0

    def check_all_messages(self, message):
        highest_prob_list = {}

        # Simplifies response creation / adds it to the dict
        def response(bot_response, list_of_words, single_response=False, required_words=[]):
            nonlocal highest_prob_list
            highest_prob_list[bot_response] = self.message_probability(message,list_of_words, single_response,required_words)

        # 1. Informal -----------------------------------------------------------------------------------------------------
        response('Hello!, How can I help you ?', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
        response('See you!', ['bye', 'goodbye'], single_response=True)
        response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
        response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
        response('Hello I am AI Bot.', required_words=['who', 'are', 'you'])

        # 2. Formal ---------------------------------------------------------------------------------------------------------
        response('You can get admissions via CAP round on the basis of your mht-cet or jee score',
                 ['how', 'can', 'I', 'get', 'admission', 'in', 'viit'])
        response('VIIT comes under SPPU university', ['which', 'university', 'viit', 'belong'])
        response('VIIT is an Autonomous Engineering College', ['autonomous', 'viit'])
        response("VIIT has it's  own ground for playing ", ['has', 'ground', 'viit'])
        response(
            'NSS,I2IC,ACM,Rotaract,Entrepreneurship Development cell,TEDx,Compitive Exam Cell,Women Empowerment cell,',
            ['clubs'])
        response('Every year 1076 students get admission in VIIT', ['how', 'much', 'students', 'intake'])
        response('VIIT comes under top 5 Engineering institutes of Maharashtra', ['rank', 'in', 'maharashtra', 'viit'])
        response("VIIT don't have it's bus transport", ['transport', 'facility', 'viit'])
        response('There are 5 cafeterias in Campus', ['how', 'many', 'cafeteria'])
        response(
            'There are 11 types of sports that include Cricket, Football, Volleyball, Badminton, Table Tennis, Chess, Carrom, Tug of war, Basketball, Handball and  Kho-kho ',
            ['what', 'different', 'sports'])
        response("VIIT has a lot more space for parking", ['parking'])
        response("VIIT don't have it's bus transport", ['transport', 'facility', 'viit'])
        response("VIIT has 6 departments that include Comp,Civil,AIDS,IT,Mech,and ENTC department ",
                 ['how', 'many', 'departments'])
        response('VIIT organises two massive events Gandharva and Avishkar', ['how', 'many', 'events'])
        response('VIIT organises Perception Robocon ,Supra, Baja , Hackathon,Scitech',
                 ['what', 'Technical', 'Activities', 'viit', 'organise'])
        response('VIIT has good average package of 7 LPA', ['average', 'package', 'viit'])
        response("The intake of computer department of VIIT  is 240 ", ['intake', 'computer', 'deparment'])
        response("VIIT has it's own library which has almost 5000 books ", ['Library', 'has'])

        response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
        response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
        response(long.R_NAME, ['what', 'is', 'your', 'name'], required_words=['your', 'name'])
        response(long.R_SEM, ['how', 'many', 'semesters', 'are', 'there', 'in', 'a', 'year', 'one', 'should', 'study'])
        response(long.R_CLASS,
                 ['how', 'many', 'classes', 'will', 'be', 'there', 'in', 'a', 'day', 'long', 'are', 'the', 'classes'])
        response(long.R_EXAM, ['what', 'are', 'the', 'exams', 'like', 'is', 'exam', 'pattern'])
        response(long.R_FACILITY,
                 ['what', 'facilities', 'are', 'provided', 'by', 'the', 'college', 'for', 'students', 'college',
                  'infrastructures'])
        response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
        response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

        best_match = max(highest_prob_list, key=highest_prob_list.get)
        return self.unknown() if highest_prob_list[best_match] < 1 else best_match

    def unknown(self):
        response = ["Sorry , I didn't get that", "...", "What does that mean?"][random.randrange(4)]
        return response

    def enter_func(self, event):
        self.send.invoke()
        self.entry.set(' ')

    def clear(self):
        self.text.delete('1.0', END)
        self.entry.set('')

    def send(self):
        send = 'You : ' + self.entry.get()
        self.text.insert(END, '\n' + send)
        self.text.yview(END)
        split_message = re.split(r'\s+|[,;?!.-]\s*', send.lower())
        response = 'Bot: ' + self.check_all_messages(split_message)
        self.text.insert(END,'\n'+response)
        self.text.yview(END)


if __name__ == '__main__':
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()
