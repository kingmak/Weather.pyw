#Revision 3
# -*- coding: utf-8 -*-
import urllib2, re, tkMessageBox, Tkinter
response = urllib2.urlopen('http://weather.yahoo.com/')
website = response.read()

def core():
     degree= u'\N{DEGREE SIGN}'
     TodayTemp = re.search(regex, website).group()
     TodayHi = re.search(regexHI, website).group()
     TodayLow = re.search(regexLOW, website).group()
     msg = ('Today\'s Temperature:\n' + TodayTemp + ' ' + degree + 'F' +
             '\n\nToday\'s Expected High:\n' + TodayHi + ' ' + degree + 'F' +
             '\n\nToday\'s Expected Low:\n' + TodayLow + ' ' + degree + 'F' +
             '\n\nSource:\nweather.yahoo.com\n\nAuthor: [RGN]WarKingMak')
     
     window = Tkinter.Tk()
     window.withdraw()
     tkMessageBox.showinfo(title = 'Temperature', message = msg)
     
regex = r'(?<=<span class="f"><span class="num">).*(?=</span><span class="deg">&deg;</span></span>)'
regexHI = r'(?<=<span class="hi f w-up-arrow">).*(?=&deg;</span>)'
regexLOW = r'(?<=<span class="lo f w-down-arrow">).*(?=&deg;</span>)'
core()
