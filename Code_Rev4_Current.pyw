#Revision 4
# -*- coding: utf-8 -*-
import urllib2, re, sys, webbrowser
from Tkinter import *

response = urllib2.urlopen('http://weather.yahoo.com/')
website = response.read()

regexReg = r'(?<=<span class="f"><span class="num">).*(?=</span><span class="deg">&deg;</span></span>)'
regexHi = r'(?<=<span class="hi f w-up-arrow">).*(?=&deg;</span>)'
regexLow = r'(?<=<span class="lo f w-down-arrow">).*(?=&deg;</span>)'

degree= u'\N{DEGREE SIGN}'
TodayTemp = re.search(regexReg, website).group()
TodayHi = re.search(regexHi, website).group()
TodayLow = re.search(regexLow, website).group()

RegTemp = 'Temperature Right Now: ' + TodayTemp + ' ' + degree + 'F'
TempHi = 'Today\'s Expected High: ' + TodayHi + ' ' + degree + 'F'
TemLow = 'Today\'s Expected Low : ' + TodayLow + ' ' + degree + 'F'

# GUI Funcs

def Quit():
    sys.exit('')

def LaunchAuthor():
    webbrowser.open_new('https://github.com/kingmak')

# GUI

root = Tk()
root.config(cursor = 'plus')
root.option_add('*Font', 'courier 12')
root.option_add('*Background', 'grey')
root.configure(bg = 'grey')

w, h = 355, 250
x, y = (root.winfo_screenwidth()/2) - (w/2), (root.winfo_screenheight()/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

Label1 = Label(root, fg = 'blue', text = RegTemp).place(x = 0, y = 0)
Label2 = Label(root, fg = 'blue', text = TempHi).place(x = 0, y = 25)
Label3 = Label(root, fg = 'blue', text = TemLow).place(x = 0, y = 50)
Label4 = Label(root, fg = 'blue', text = 'Source: weather.yahoo.com').place(x = 0, y = 100)
Label5 = Label(root, fg = 'blue', text = 'Author:').place(x = 0, y = 129)
Button1 = Button(root, relief = FLAT, height = 1, width = 18, text = 'KingMaK (click me)', command = LaunchAuthor).place(x = 95, y = 124)
Button2 = Button(root, fg = 'blue', height = 1, width = 27, text = 'Done', command = Quit).place(x = 10, y = 200)

root.resizable(0,0)
root.title('Weather Grab')
root.mainloop()
