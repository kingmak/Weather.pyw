#Revision 1
# -*- coding: utf-8 -*-
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

try:
     regex = r'(?<=<div class="day-temp-current temp-f ">).*(?=&deg;<span class="unit">F</span><a href="#toggle" class="ntime">&deg;C</a>)'
     core()

except Exception:
     regex = r'(?<=<div class="day-temp-current temp-f ">).*(?=&deg;<span class="unit">F</span><a href="#toggle" class="dtime">&deg;C</a>)'
     core() 
