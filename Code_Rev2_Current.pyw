# -*- coding: utf-8 -*-
# Created By MAK
import urllib2, re, tkMessageBox, Tkinter
response = urllib2.urlopen('http://weather.yahoo.com/')
website = response.read()

def core():
     degree= u'\N{DEGREE SIGN}'
     TodayTemp = re.search(regex, website).group()
     msg = 'Today\'s Temperature:\n' + TodayTemp + ' ' + degree + 'F'
     window = Tkinter.Tk()
     window.withdraw()
     tkMessageBox.showinfo(title = 'Temperature', message = msg) 

regex = r'(?<=<span class="f"><span class="num">).*(?=</span><span class="deg">&deg;</span></span>)'
core()
