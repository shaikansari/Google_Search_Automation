#Import Libraries

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup as soup
import webbrowser as wb
import time, random
from tkinter import *
import tkinter.messagebox

fb = ['www.facebook.com', 'facebook.com', 'facebook']
youtube = ['www.youtube.com', 'youtube.com', 'youtube']

questions = [' Hello Buddy!!! What do you want to search today? ', 
          ' Hello, My friend!! Enter your Query please... ' , 
          ' Hi Dude!!!, What are you going to google today!!! ',
          ' Hello Buddy, How can I help you!! ']


rand_ques = random.choices(questions)

def get_input():

    query = display.get()

    if query in fb:
        confirm = tkinter.messagebox.askquestion('Alert', 'Do you really want to open facebook during work hours?')
        if confirm =='yes':
            wb.open_new('https://www.facebook.com')

    elif query in youtube:
        confirm = tkinter.messagebox.askquestion('Alert', 'Do you really want to open youtube during work hours?')
        if confirm =='yes':
            wb.open_new('https://www.youtube.com')
    else:
        data = urllib.parse.urlencode({'q':query})

        url = 'https://www.google.com/search?'+data

    ##To find header, search what is my HTTP header
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}

        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)

        page = soup(resp, 'html.parser')

        wb.open_new('https://www.google.com')
        time.sleep(3)

        for links in page.find_all('h3',{'class':'r'})[1:11]:
            link = links.find('a').get('href')
            wb.open_new_tab(link)

def clear_all():
    display.delete(0, END)


window = Tk()
window.title('Google serach engine')
# window.geometry('200x100')

label = Label(window, text = rand_ques, fg='blue')
label.pack(side='top')

display = Entry(window)
display.pack(side='top', fill=X)

search_button = Button(window, text = 'Search', fg = 'red', command = get_input)
search_button.pack(side='left')

clear_button = Button(window, text = 'Clear', command = clear_all)
clear_button.pack(side ='left')

window.mainloop()
