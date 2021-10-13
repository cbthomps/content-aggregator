#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created on: Thu Jul 15 14:52:45 2021
@author: Chris Thompson
@course: INF 6050
@university: Wayne State University
@assignment: 

@pythonVersion: 3.8
@requiredModules:
    
@description: This is a script to...
"""
#####################################
#IMPORT MODULES
#####################################
import requests
from bs4 import BeautifulSoup
import webbrowser
import tkinter as tk
from datetime import datetime

#####################################
#GLOBAL VARIABLES AND FUNCTIONS
#####################################
#A list of items to be removed from website titles in order to access the webpage
removal = ["– ", "’", '"', '“', "(", ")", "/", ":", "- ", "”", "...", "!", "?", ",",
           "„", "…", "[", "]", "°"]
#These lists contain characters with accents or other markings to be replaced into
#their English letter equivalent in order to access the webpage
letterA = ["ą", "ã", "Ã", "ä", "Ä", "å", "Å", "Á", "á", "À", "à", "Â", "â", "ǎ", "Ǎ",
           "ä", "Ä", "ă", "Ă", "ā", "Ā", "ⱥ", "Ⱥ", "ą", "Ą", "ǡ", "Ǡ", "ǻ", "Ǻ", "ǟ",
           "Ǟ", "ǻ", "Ǻ", "ǟ", "Ǟ", "ȁ", "Ȁ", "ȃ", "Ȃ", "ḁ", "Ḁ"]
letterAE = ["æ", "Æ", "ǽ", "Ǽ", "ǣ", "Ǣ"]
letterB = ["ḃ", "Ḃ", "ƀ", "Ƀ", "ḅ", "Ḅ", "ḇ", "Ḇ"]
letterC = ["ç", "Ç", "Ĉ", "ĉ", "č", "Č", "ć", "Ć", "ċ", "Ċ", "ȼ", "Ȼ", "ḉ", "Ḉ"]
letterD = ["ḋ", "Ḋ", "ď", "Ď", "ḑ", "Ḑ", "đ", "Đ", "ḍ", "Ḍ", "ḓ", "Ḓ", "ḏ", "Ḏ"]
letterE = ["è", "É", "é", "È", "ê", "Ê", "ë", "Ë", "ė", "Ė", "ě", "Ě", "ĕ", "Ĕ",
           "ē", "Ē", "ę", "Ę", "ȩ", "Ȩ", "ɇ", "Ɇ", "ḗ", "Ḗ", "ḕ", "Ḕ", "ḝ", "Ḝ",
           "ȅ", "Ȅ", "ȇ", "Ȇ", "ḙ", "Ḙ", "ḛ", "Ḛ"]
letterF = ["ḟ", "Ḟ"]
letterG = ["Ĝ", "ĝ", "ǵ", "Ǵ", "ġ", "Ġ", "ǧ", "Ǧ", "ğ", "Ğ", "ḡ", "Ḡ", "ģ", "Ģ",
           "ǥ", "Ǥ"]
letterH = ["Ĥ", "ĥ", "ḣ", "Ḣ", "ḧ", "Ḧ", "ȟ", "Ȟ", "ḩ", "Ḩ", "ħ", "Ħ", "ḥ", "Ḥ",
           "ḫ", "Ḫ", "ⱨ", "Ⱨ"]
letterI = ["í", "Í", "ì", "Ì", "î", "Î", "ï", "Ï", "ǐ", "Ǐ", "ĭ", "Ĭ", "ī", "Ī",
           "ĩ", "Ĩ", "į", "Į", "ḯ", "Ḯ", "ȉ", "Ȉ", "ȋ", "Ȋ", "ḭ", "Ḭ"]
letterJ = ["Ĵ", "ĵ", "ɉ", "Ɉ"]
letterK = ["ḱ", "Ḱ", "ǩ", "Ǩ", "ķ", "Ķ", "ḳ", "Ḳ", "ḵ", "Ḵ", "ⱪ", "Ⱪ"]
letterL = ["ƚ", "Ƚ", "ĺ", "Ĺ", "ŀ", "Ŀ", "ľ", "Ľ", "ļ", "Ļ", "ł", "Ł", "ḷ", "Ḷ",
           "ḽ", "Ḽ", "ḻ", "Ḻ", "ḹ", "Ḹ"]
letterM = ["ḿ", "Ḿ", "ṁ", "Ṁ", "ṃ", "Ṃ"]
letterN = ["ń", "Ń", "ñ", "Ñ", "ǹ", "Ǹ", "ṅ", "Ṅ", "ň", "Ň", "ņ", "Ņ", "ƞ", "Ƞ",
           "ṇ", "Ṇ", "ṋ", "Ṋ", "ṉ", "Ṉ"]
letterO = ["ø", "Ø", "ô", "Ô", "ó", "Ó", "ò", "Ò", "ö", "Ö", "õ", "Õ", "ȯ", "Ȯ",
           "ǒ", "Ǒ", "ŏ", "Ŏ", "ō", "Ō", "õ", "Õ", "ǫ", "Ǫ", "ő", "Ő", "ṓ", "Ṓ",
           "ṑ", "Ṑ", "ṍ", "Ṍ", "ȱ", "Ȱ", "ȫ", "Ȫ", "ṏ", "Ṏ", "ǿ", "Ǿ", "ȭ", "Ȭ",
           "ǭ", "Ǭ", "ȍ", "Ȍ", "ȏ", "Ȏ"]
letterOE = ["œ", "Œ"]
letterOU = ["ȣ", "Ȣ"]
letterP = ["ṕ", "Ṕ", "ṗ", "Ṗ"]
letterQ = ["ɋ", "Ɋ"]
letterR = ["ŕ", "Ŕ", "ṙ", "Ṙ", "ř", "Ř", "ŗ", "Ŗ", "ɍ", "Ɍ", "ȑ", "Ȑ", "ȓ", "Ȓ",
           "ṛ", "Ṛ", "ṟ", "Ṟ", "ṝ", "Ṝ"]
letterS = ["ß", "ẞ", "ş", "Ŝ", "ŝ", "ś", "Ś", "ṡ", "Ṡ", "š", "Š", "ş", "Ş", "ṥ",
           "Ṥ", "ṧ", "Ṧ", "ṣ", "Ṣ", "ș", "Ș", "ṩ", "Ṩ"]
letterT = ["ṫ", "Ṫ", "ť", "Ť", "ţ", "Ţ", "ṭ", "Ṭ", "ț", "Ț", "ṱ", "Ṱ", "ṯ", "Ṯ",
           "ⱦ", "Ⱦ", "þ", "Þ", "ŧ", "Ŧ"]
letterU = ["ü", "Ü", "ú", "Ú", "ù", "Ù", "û", "Û", "ū", "Ū" "Ǔ", "ǔ", "ŭ", "Ŭ",
           "ũ", "Ũ", "ů", "Ů", "ų", "Ų", "ű", "Ű", "ʉ", "Ʉ", "ǘ", "Ǘ", "ǜ", "Ǜ",
           "ṹ", "Ṹ", "ǚ", "Ǚ", "ṻ", "Ṻ", "ǖ", "Ǖ", "ȕ", "Ȕ", "ȗ", "Ȗ", "ṳ", "Ṳ",
           "ṷ", "Ṷ", "ṵ", "Ṵ"]
letterV = ["ṽ", "Ṽ", "ṿ", "Ṿ"]
letterW = ["ẃ", "Ẃ", "ẁ", "Ẁ", "ẇ", "Ẇ", "ŵ", "Ŵ", "ẅ", "Ẅ", "ẉ", "Ẉ", "ⱳ", "Ⱳ"]
letterX = ["ẋ", "Ẋ", "ẍ", "Ẍ"]
letterY = ["ÿ", "Ÿ", "ý", "Ý", "ỳ", "Ỳ", "ẏ", "Ẏ", "ŷ", "Ŷ", "ȳ", "Ȳ", "ỹ", "Ỹ",
           "ɏ", "Ɏ", "ỷ", "Ỷ", "ỵ", "Ỵ"]
letterZ = ["ž", "Ž", "ź", "Ź", "ż", "Ż", "ẑ", "Ẑ", "ȥ", "Ȥ", "ẓ", "Ẓ", "ẕ", "Ẕ",
           "ⱬ", "Ⱬ"]
#This function is used to replace characters that need removing in a page title
#It also replaces letters that have accents and other markings with non-accented letters
def remove_characters(string):
    for char in letterA:
        string = string.replace(char, "a")
    for char in letterE:
        string = string.replace(char, "ae")
    for char in letterB:
        string = string.replace(char, "b")
    for char in letterC:
        string = string.replace(char, "c")
    for char in letterD:
        string = string.replace(char, "d")
    for char in letterE:
        string = string.replace(char, "e")
    for char in letterF:
        string = string.replace(char, "f")
    for char in letterG:
        string = string.replace(char, "g")
    for char in letterH:
        string = string.replace(char, "h")
    for char in letterI:
        string = string.replace(char, "i")
    for char in letterJ:
        string = string.replace(char, "j")
    for char in letterK:
        string = string.replace(char, "k")
    for char in letterL:
        string = string.replace(char, "l")
    for char in letterM:
        string = string.replace(char, "m")
    for char in letterN:
        string = string.replace(char, "n")
    for char in letterO:
        string = string.replace(char, "o")
    for char in letterOE:
        string = string.replace(char, "oe")
    for char in letterOU:
        string = string.replace(char, "ou")
    for char in letterP:
        string = string.replace(char, "p")
    for char in letterQ:
        string = string.replace(char, "q")
    for char in letterR:
        string = string.replace(char, "r")
    for char in letterS:
        string = string.replace(char, "s")
    for char in letterT:
        string = string.replace(char, "t")
    for char in letterU:
        string = string.replace(char, "u")
    for char in letterV:
        string = string.replace(char, "v")
    for char in letterW:
        string = string.replace(char, "w")
    for char in letterX:
        string = string.replace(char, "x")
    for char in letterY:
        string = string.replace(char, "y")
    for char in letterZ:
        string = string.replace(char, "z")
    for char in removal:
        string = string.replace(char,"")
        string = string.replace("¶", "to")
        string = string.replace("&", "and")    
        string = string.replace(" ", "-").lower()
    return string

#####################################
#CLASSES
#####################################
#The main menu for the program
class MainMenu(tk.Tk):
    #Sets up the frame and label and buttons for the main menu
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, bg ='LightCyan2', width = 1500, height = 800)
        self.foo = None
        self.label1 = tk.Label(self.frame, text = 'Angry Metal Guy' , font='arial 20 bold', bg = 'PaleTurquoise1')
        self.label1.place(x=50, y=50)
        #First web article
        self.amg1 = tk.StringVar()
        self.entry1 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.amg1, bg ='antiquewhite2',width = 30,)
        self.entry1.place(x=50, y = 100)
        self.button1 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readAMG1)
        self.button1.place(x=50, y=125)
        self.amgPage1 = requests.get("https://www.angrymetalguy.com")
        self.amgSoup1 = BeautifulSoup(self.amgPage1.content, 'html.parser')
        #Find and set the title of the article
        self.amgPageTitle1 = self.amgSoup1.select('h2')[0].text
        self.amg1.set(self.amgPageTitle1)
        #Second web article
        self.amg2 = tk.StringVar()
        self.entry2 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.amg2, bg ='antiquewhite2',width = 30,)
        self.entry2.place(x=50, y = 160)
        self.button2 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readAMG2)
        self.button2.place(x=50, y=185)
        self.amgPage2 = requests.get("https://www.angrymetalguy.com")
        self.amgSoup2 = BeautifulSoup(self.amgPage2.content, 'html.parser')
        #Find and set the title of the article
        self.amgPageTitle2 = self.amgSoup2.select('h2')[1].text
        self.amg2.set(self.amgPageTitle2)
        #Third web article
        self.amg3 = tk.StringVar()
        self.entry3 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.amg3, bg ='antiquewhite2',width = 30,)
        self.entry3.place(x=50, y = 220)
        self.button3 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readAMG3)
        self.button3.place(x=50, y=245)
        self.amgPage3 = requests.get("https://www.angrymetalguy.com")
        self.amgSoup3 = BeautifulSoup(self.amgPage3.content, 'html.parser')
        #Find and set the title of the article
        self.amgPageTitle3 = self.amgSoup3.select('h2')[2].text
        self.amg3.set(self.amgPageTitle3)
        #Fourth web article
        self.amg4 = tk.StringVar()
        self.entry4 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.amg4, bg ='antiquewhite2',width = 30,)
        self.entry4.place(x=50, y = 275)
        self.button4 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readAMG4)
        self.button4.place(x=50, y=295)
        self.amgPage4 = requests.get("https://www.angrymetalguy.com")
        self.amgSoup4 = BeautifulSoup(self.amgPage4.content, 'html.parser')
        #Find and set the title of the article
        self.amgPageTitle4 = self.amgSoup4.select('h2')[3].text
        self.amg4.set(self.amgPageTitle4)
        #Fifth web article
        self.amg5 = tk.StringVar()
        self.entry5 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.amg5, bg ='antiquewhite2',width = 30,)
        self.entry5.place(x=50, y = 330)
        self.button5 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readAMG5)
        self.button5.place(x=50, y=355)
        self.amgPage5 = requests.get("https://www.angrymetalguy.com")
        self.amgSoup5 = BeautifulSoup(self.amgPage5.content, 'html.parser')
        #Find and set the title of the article
        self.amgPageTitle5 = self.amgSoup5.select('h2')[4].text
        self.amg5.set(self.amgPageTitle5)
        #Second website 
        self.label2 = tk.Label(self.frame, text = 'No Clean Singing' , font='arial 20 bold', bg = 'PaleTurquoise1')
        self.label2.place(x=350, y=50)
        #First web article
        self.injection1 = tk.StringVar()
        self.entry4 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.injection1, bg ='antiquewhite2',width = 40,)
        self.entry4.place(x=350, y = 100)
        self.button4 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readInjection1)
        self.button4.place(x=350, y=125)
        self.injectionPage1 = requests.get("https://www.nocleansinging.com/category/reviews/album-reviews/")
        self.injectionSoup1 = BeautifulSoup(self.injectionPage1.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.injectionPageTitle1 = self.injectionSoup1.select('h2')[0].text
        self.injection1.set(self.injectionPageTitle1)
        self.injectionYear1 = self.injectionSoup1.select('span.year')[0].text
        self.injectionMonth1 = self.injectionSoup1.select('span.month')[0].text
        self.injectionDay1 = self.injectionSoup1.select('span.day')[0].text
        if self.injectionMonth1 == "Jan":
            self.injectionMonth1 = "01"
        elif self.injectionMonth1 == "Feb":
            self.injectionMonth1 = "02"
        elif self.injectionMonth1 == "Mar":
            self.injectionMonth1 = "03"
        elif self.injectionMonth1 == "Apr":
            self.injectionMonth1 = "04"
        elif self.injectionMonth1 == "May":
            self.injectionMonth1 = "05"
        elif self.injectionMonth1 == "Jun":
            self.injectionMonth1 = "06"
        elif self.injectionMonth1 == "Jul":
            self.injectionMonth1 = "07"
        elif self.injectionMonth1 == "Aug":
            self.injectionMonth1 = "08"
        elif self.injectionMonth1 == "Sep":
            self.injectionMonth1 = "09"
        elif self.injectionMonth1 == "Oct":
            self.injectionMonth1 = "10"
        elif self.injectionMonth1 == "Nov":
            self.injectionMonth1 = "11"
        elif self.injectionMonth1 == "Dec":
            self.injectionMonth1 = "12"
        #Second page of website
        self.injection2 = tk.StringVar()
        self.entry5 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.injection2, bg ='antiquewhite2',width = 40,)
        self.entry5.place(x=350, y = 160)
        self.button5 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readInjection2)
        self.button5.place(x=350, y=185)
        self.injectionPage2 = requests.get("https://www.nocleansinging.com/category/reviews/album-reviews/")
        self.injectionSoup2 = BeautifulSoup(self.injectionPage2.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.injectionPageTitle2 = self.injectionSoup2.select('h2')[1].text
        self.injection2.set(self.injectionPageTitle2)
        self.injectionYear2 = self.injectionSoup2.select('span.year')[1].text
        self.injectionMonth2 = self.injectionSoup2.select('span.month')[1].text
        self.injectionDay2 = self.injectionSoup2.select('span.day')[1].text
        if self.injectionMonth2 == "Jan":
            self.injectionMonth2 = "01"
        elif self.injectionMonth2 == "Feb":
            self.injectionMonth2 = "02"
        elif self.injectionMonth2 == "Mar":
            self.injectionMonth2 = "03"
        elif self.injectionMonth2 == "Apr":
            self.injectionMonth2 = "04"
        elif self.injectionMonth2 == "May":
            self.injectionMonth2 = "05"
        elif self.injectionMonth2 == "Jun":
            self.injectionMonth2 = "06"
        elif self.injectionMonth2 == "Jul":
            self.injectionMonth2 = "07"
        elif self.injectionMonth2 == "Aug":
            self.injectionMonth2 = "08"
        elif self.injectionMonth2 == "Sep":
            self.injectionMonth2 = "09"
        elif self.injectionMonth2 == "Oct":
            self.injectionMonth2 = "10"
        elif self.injectionMonth2 == "Nov":
            self.injectionMonth2 = "11"
        elif self.injectionMonth2 == "Dec":
            self.injectionMonth2 = "12"
        #Third page of website
        self.injection3 = tk.StringVar()
        self.entry6 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.injection3, bg ='antiquewhite2',width = 40,)
        self.entry6.place(x=350, y = 220)
        self.button6 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readInjection3)
        self.button6.place(x=350, y=245)
        self.injectionPage3 = requests.get("https://www.nocleansinging.com/category/reviews/album-reviews/")
        self.injectionSoup3 = BeautifulSoup(self.injectionPage3.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.injectionPageTitle3 = self.injectionSoup3.select('h2')[2].text
        self.injection3.set(self.injectionPageTitle3)
        self.injectionYear3 = self.injectionSoup3.select('span.year')[2].text
        self.injectionMonth3 = self.injectionSoup3.select('span.month')[2].text
        self.injectionDay3 = self.injectionSoup3.select('span.day')[2].text
        if self.injectionMonth3 == "Jan":
            self.injectionMonth3 = "01"
        elif self.injectionMonth3 == "Feb":
            self.injectionMonth3 = "02"
        elif self.injectionMonth3 == "Mar":
            self.injectionMonth3 = "03"
        elif self.injectionMonth3 == "Apr":
            self.injectionMonth3 = "04"
        elif self.injectionMonth3 == "May":
            self.injectionMonth3 = "05"
        elif self.injectionMonth3 == "Jun":
            self.injectionMonth3 = "06"
        elif self.injectionMonth3 == "Jul":
            self.injectionMonth3 = "07"
        elif self.injectionMonth3 == "Aug":
            self.injectionMonth3 = "08"
        elif self.injectionMonth3 == "Sep":
            self.injectionMonth3 = "09"
        elif self.injectionMonth3 == "Oct":
            self.injectionMonth3 = "10"
        elif self.injectionMonth3 == "Nov":
            self.injectionMonth3 = "11"
        elif self.injectionMonth3 == "Dec":
            self.injectionMonth3 = "12"
        #Fourth page of website
        self.injection4 = tk.StringVar()
        self.entry6 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.injection4, bg ='antiquewhite2',width = 40,)
        self.entry6.place(x=350, y = 275)
        self.button6 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readInjection4)
        self.button6.place(x=350, y=295)
        self.injectionPage4 = requests.get("https://www.nocleansinging.com/category/reviews/album-reviews/")
        self.injectionSoup4 = BeautifulSoup(self.injectionPage4.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.injectionPageTitle4 = self.injectionSoup4.select('h2')[3].text
        self.injection4.set(self.injectionPageTitle4)
        self.injectionYear4 = self.injectionSoup4.select('span.year')[3].text
        self.injectionMonth4 = self.injectionSoup4.select('span.month')[3].text
        self.injectionDay4 = self.injectionSoup4.select('span.day')[3].text
        if self.injectionMonth4 == "Jan":
            self.injectionMonth4 = "01"
        elif self.injectionMonth4 == "Feb":
            self.injectionMonth4 = "02"
        elif self.injectionMonth4 == "Mar":
            self.injectionMonth4 = "03"
        elif self.injectionMonth4 == "Apr":
            self.injectionMonth4 = "04"
        elif self.injectionMonth4 == "May":
            self.injectionMonth4 = "05"
        elif self.injectionMonth4 == "Jun":
            self.injectionMonth4 = "06"
        elif self.injectionMonth4 == "Jul":
            self.injectionMonth4 = "07"
        elif self.injectionMonth4 == "Aug":
            self.injectionMonth4 = "08"
        elif self.injectionMonth4 == "Sep":
            self.injectionMonth4 = "09"
        elif self.injectionMonth4 == "Oct":
            self.injectionMonth4 = "10"
        elif self.injectionMonth4 == "Nov":
            self.injectionMonth4 = "11"
        elif self.injectionMonth4 == "Dec":
            self.injectionMonth4 = "12"
        #Fifth page of website
        self.injection5 = tk.StringVar()
        self.entry6 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.injection5, bg ='antiquewhite2',width = 40,)
        self.entry6.place(x=350, y = 330)
        self.button6 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readInjection5)
        self.button6.place(x=350, y=355)
        self.injectionPage5 = requests.get("https://www.nocleansinging.com/category/reviews/album-reviews/")
        self.injectionSoup5 = BeautifulSoup(self.injectionPage5.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.injectionPageTitle5 = self.injectionSoup5.select('h2')[4].text
        self.injection5.set(self.injectionPageTitle5)
        self.injectionYear5 = self.injectionSoup5.select('span.year')[4].text
        self.injectionMonth5 = self.injectionSoup5.select('span.month')[4].text
        self.injectionDay5 = self.injectionSoup5.select('span.day')[4].text
        if self.injectionMonth5 == "Jan":
            self.injectionMonth5 = "01"
        elif self.injectionMonth5 == "Feb":
            self.injectionMonth5 = "02"
        elif self.injectionMonth5 == "Mar":
            self.injectionMonth5 = "03"
        elif self.injectionMonth5 == "Apr":
            self.injectionMonth5 = "04"
        elif self.injectionMonth5 == "May":
            self.injectionMonth5 = "05"
        elif self.injectionMonth5 == "Jun":
            self.injectionMonth5 = "06"
        elif self.injectionMonth5 == "Jul":
            self.injectionMonth5 = "07"
        elif self.injectionMonth5 == "Aug":
            self.injectionMonth5 = "08"
        elif self.injectionMonth5 == "Sep":
            self.injectionMonth5 = "09"
        elif self.injectionMonth5 == "Oct":
            self.injectionMonth5 = "10"
        elif self.injectionMonth5 == "Nov":
            self.injectionMonth5 = "11"
        elif self.injectionMonth5 == "Dec":
            self.injectionMonth5 = "12"
        #Third website
        self.label3 = tk.Label(self.frame, text = 'Ave Noctum' , font='arial 20 bold', bg = 'PaleTurquoise1')
        self.label3.place(x=650, y=50)
        #First page of website
        self.heavy1 = tk.StringVar()
        self.entry7 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.heavy1, bg ='antiquewhite2',width = 30,)
        self.entry7.place(x=650, y = 100)
        self.button7 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readHeavy1)
        self.button7.place(x=650, y=125)
        self.heavyPage1 = requests.get("https://avenoctum.com/category/album/", headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"})
        self.heavySoup1 = BeautifulSoup(self.heavyPage1.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.heavyPageTitle1 = self.heavySoup1.select('h2')[0].text
        self.heavy1.set(self.heavyPageTitle1)
        self.heavyDate1 = self.heavySoup1.select('a.post-date')[0].text
        self.heavyDate1 = self.heavyDate1.replace("/", " ")
        self.heavyDate1 = self.heavyDate1.split()
        self.heavyYear1 = self.heavyDate1[2]
        self.heavyMonth1 = self.heavyDate1[1]
        self.heavyDay1 = self.heavyDate1[0]
        #Second page of website
        self.heavy2 = tk.StringVar()
        self.entry8 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.heavy2, bg ='antiquewhite2',width = 30,)
        self.entry8.place(x=650, y = 160)
        self.button8 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readHeavy2)
        self.button8.place(x=650, y=185)
        self.heavyPage2 = requests.get("https://avenoctum.com/category/album/", headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"})
        self.heavySoup2 = BeautifulSoup(self.heavyPage2.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.heavyPageTitle2 = self.heavySoup2.select('h2')[1].text
        self.heavy2.set(self.heavyPageTitle2)
        self.heavyDate2 = self.heavySoup2.select('a.post-date')[1].text
        self.heavyDate2 = self.heavyDate2.replace("/", " ")
        self.heavyDate2 = self.heavyDate2.split()
        self.heavyYear2 = self.heavyDate2[2]
        self.heavyMonth2 = self.heavyDate2[1]
        self.heavyDay2 = self.heavyDate2[0]
        #Third page of website
        self.heavy3 = tk.StringVar()
        self.entry9 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.heavy3, bg ='antiquewhite2',width = 30,)
        self.entry9.place(x=650, y = 220)
        self.button9 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readHeavy3)
        self.button9.place(x=650, y=245)
        self.heavyPage3 = requests.get("https://avenoctum.com/category/album/", headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"})
        self.heavySoup3 = BeautifulSoup(self.heavyPage3.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.heavyPageTitle3 = self.heavySoup3.select('h2')[2].text
        self.heavy3.set(self.heavyPageTitle3)
        self.heavyDate3 = self.heavySoup3.select('a.post-date')[2].text
        self.heavyDate3 = self.heavyDate3.replace("/", " ")
        self.heavyDate3 = self.heavyDate3.split()
        self.heavyYear3 = self.heavyDate3[2]
        self.heavyMonth3 = self.heavyDate3[1]
        self.heavyDay3 = self.heavyDate3[0]
        #Fourth page of website    
        self.heavy4 = tk.StringVar()
        self.entry9 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.heavy4, bg ='antiquewhite2',width = 30,)
        self.entry9.place(x=650, y = 275)
        self.button9 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readHeavy4)
        self.button9.place(x=650, y=295)
        self.heavyPage4 = requests.get("https://avenoctum.com/category/album/", headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"})
        self.heavySoup4 = BeautifulSoup(self.heavyPage4.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.heavyPageTitle4 = self.heavySoup4.select('h2')[3].text
        self.heavy4.set(self.heavyPageTitle4)
        self.heavyDate4 = self.heavySoup4.select('a.post-date')[3].text
        self.heavyDate4 = self.heavyDate4.replace("/", " ")
        self.heavyDate4 = self.heavyDate4.split()
        self.heavyYear4 = self.heavyDate4[2]
        self.heavyMonth4 = self.heavyDate4[1]
        self.heavyDay4 = self.heavyDate4[0]
        #Fifth page of website    
        self.heavy5 = tk.StringVar()
        self.entry9 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.heavy5, bg ='antiquewhite2',width = 30,)
        self.entry9.place(x=650, y = 330)
        self.button9 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readHeavy5)
        self.button9.place(x=650, y=355)
        self.heavyPage5 = requests.get("https://avenoctum.com/category/album/", headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"})
        self.heavySoup5 = BeautifulSoup(self.heavyPage5.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.heavyPageTitle5 = self.heavySoup5.select('h2')[4].text
        self.heavy5.set(self.heavyPageTitle5)
        self.heavyDate5 = self.heavySoup5.select('a.post-date')[4].text
        self.heavyDate5 = self.heavyDate5.replace("/", " ")
        self.heavyDate5 = self.heavyDate5.split()
        self.heavyYear5 = self.heavyDate5[2]
        self.heavyMonth5 = self.heavyDate5[1]
        self.heavyDay5 = self.heavyDate5[0]
        #Fourth website    
        self.label3 = tk.Label(self.frame, text = 'Head-Banger Reviews' , font='arial 20 bold', bg = 'PaleTurquoise1')
        self.label3.place(x=950, y=50)
        #First page of website
        self.head1 = tk.StringVar()
        self.entry10 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.head1, bg ='antiquewhite2',width = 30,)
        self.entry10.place(x=950, y = 100)
        self.button10 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readHead1)
        self.button10.place(x=950, y=125)
        self.headPage1 = requests.get("https://headbangerreviews.wordpress.com/")
        self.headSoup1 = BeautifulSoup(self.headPage1.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.headPageTitle1 = self.headSoup1.select('h1')[1].text
        self.head1.set(self.headPageTitle1)
        self.headDate1 = self.headSoup1.select('time')[0].text
        self.headDate1 = self.headDate1.replace(", ", " ")
        self.headDate1 = self.headDate1.split()
        self.headYear1 = self.headDate1[2]
        self.headDay1 = self.headDate1[1]
        if self.headDate1[0] == "January":
            self.headMonth1 = "01"
        elif self.headDate1[0] == "February":
            self.headMonth1 = "02"
        elif self.headDate1[0] == "March":
            self.headMonth1 = "03"
        elif self.headDate1[0] == "April":
            self.headMonth1 = "04"
        elif self.headDate1[0] == "May":
            self.headMonth1 = "05"
        elif self.headDate1[0] == "June":
            self.headMonth1 = "06"
        elif self.headDate1[0] == "July":
            self.headMonth1 = "07"
        elif self.headDate1[0] == "August":
            self.headMonth1 = "08"
        elif self.headDate1[0] == "September":
            self.headMonth1 = "09"
        elif self.headDate1[0] == "October":
            self.headMonth1 = "10"
        elif self.headDate1[0] == "November":
            self.headMonth1 = "11"
        elif self.headDate1[0] == "December":
            self.headMonth1 = "12"
        #Second page of website
        self.head2 = tk.StringVar()
        self.entry11 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.head2, bg ='antiquewhite2',width = 30,)
        self.entry11.place(x=950, y = 160)
        self.button11 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readHead2)
        self.button11.place(x=950, y=185)
        self.headPage2 = requests.get("https://headbangerreviews.wordpress.com/")
        self.headSoup2 = BeautifulSoup(self.headPage2.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.headPageTitle2 = self.headSoup2.select('h1')[2].text
        self.head2.set(self.headPageTitle2)
        self.headDate2 = self.headSoup2.select('time')[2].text
        self.headDate2 = self.headDate2.replace(", ", " ")
        self.headDate2 = self.headDate2.split()
        self.headYear2 = self.headDate2[2]
        self.headDay2 = self.headDate2[1]
        if self.headDate2[0] == "January":
            self.headMonth2 = "01"
        elif self.headDate2[0] == "February":
            self.headMonth2 = "02"
        elif self.headDate2[0] == "March":
            self.headMonth2 = "03"
        elif self.headDate2[0] == "April":
            self.headMonth2 = "04"
        elif self.headDate2[0] == "May":
            self.headMonth2 = "05"
        elif self.headDate2[0] == "June":
            self.headMonth2 = "06"
        elif self.headDate2[0] == "July":
            self.headMonth2 = "07"
        elif self.headDate2[0] == "August":
            self.headMonth2 = "08"
        elif self.headDate2[0] == "September":
            self.headMonth2 = "09"
        elif self.headDate2[0] == "October":
            self.headMonth2 = "10"
        elif self.headDate2[0] == "November":
            self.headMonth2 = "11"
        elif self.headDate2[0] == "December":
            self.headMonth2 = "12"
        #Third page of website
        self.head3 = tk.StringVar()
        self.entry12 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.head3, bg ='antiquewhite2',width = 30,)
        self.entry12.place(x=950, y = 220)
        self.button12 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readHead3)
        self.button12.place(x=950, y=245)
        self.headPage3 = requests.get("https://headbangerreviews.wordpress.com/")
        self.headSoup3 = BeautifulSoup(self.headPage3.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.headPageTitle3 = self.headSoup3.select('h1')[3].text
        self.head3.set(self.headPageTitle3)
        self.headDate3 = self.headSoup3.select('time')[4].text
        self.headDate3 = self.headDate3.replace(", ", " ")
        self.headDate3 = self.headDate3.split()
        self.headYear3 = self.headDate3[2]
        self.headDay3 = self.headDate3[1]
        if self.headDate3[0] == "January":
            self.headMonth3 = "01"
        elif self.headDate3[0] == "February":
            self.headMonth3 = "02"
        elif self.headDate3[0] == "March":
            self.headMonth3 = "03"
        elif self.headDate3[0] == "April":
            self.headMonth3 = "04"
        elif self.headDate3[0] == "May":
            self.headMonth3 = "05"
        elif self.headDate3[0] == "June":
            self.headMonth3 = "06"
        elif self.headDate3[0] == "July":
            self.headMonth3 = "07"
        elif self.headDate3[0] == "August":
            self.headMonth3 = "08"
        elif self.headDate3[0] == "September":
            self.headMonth3 = "09"
        elif self.headDate3[0] == "October":
            self.headMonth3 = "10"
        elif self.headDate3[0] == "November":
            self.headMonth3 = "11"
        elif self.headDate3[0] == "December":
            self.headMonth3 = "12"
        #Fourth page of website    
        self.head4 = tk.StringVar()
        self.entry12 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.head4, bg ='antiquewhite2',width = 30,)
        self.entry12.place(x=950, y = 275)
        self.button12 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readHead4)
        self.button12.place(x=950, y=295)
        self.headPage4 = requests.get("https://headbangerreviews.wordpress.com/")
        self.headSoup4 = BeautifulSoup(self.headPage4.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.headPageTitle4 = self.headSoup4.select('h1')[4].text
        self.head4.set(self.headPageTitle4)
        self.headDate4 = self.headSoup4.select('time')[6].text
        self.headDate4 = self.headDate4.replace(", ", " ")
        self.headDate4 = self.headDate4.split()
        self.headYear4 = self.headDate4[2]
        self.headDay4 = self.headDate4[1]
        if self.headDate4[0] == "January":
            self.headMonth4 = "01"
        elif self.headDate4[0] == "February":
            self.headMonth4 = "02"
        elif self.headDate4[0] == "March":
            self.headMonth4 = "03"
        elif self.headDate4[0] == "April":
            self.headMonth4 = "04"
        elif self.headDate4[0] == "May":
            self.headMonth4 = "05"
        elif self.headDate4[0] == "June":
            self.headMonth4 = "06"
        elif self.headDate4[0] == "July":
            self.headMonth4 = "07"
        elif self.headDate4[0] == "August":
            self.headMonth4 = "08"
        elif self.headDate4[0] == "September":
            self.headMonth4 = "09"
        elif self.headDate4[0] == "October":
            self.headMonth4 = "10"
        elif self.headDate4[0] == "November":
            self.headMonth4 = "11"
        elif self.headDate4[0] == "December":
            self.headMonth4 = "12"
        #Fifth page of website    
        self.head5 = tk.StringVar()
        self.entry12 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.head5, bg ='antiquewhite2',width = 30,)
        self.entry12.place(x=950, y = 330)
        self.button12 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readHead5)
        self.button12.place(x=950, y=355)
        self.headPage5 = requests.get("https://headbangerreviews.wordpress.com/")
        self.headSoup5 = BeautifulSoup(self.headPage5.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.headPageTitle5 = self.headSoup5.select('h1')[5].text
        self.head5.set(self.headPageTitle5)
        self.headDate5 = self.headSoup5.select('time')[8].text
        self.headDate5 = self.headDate5.replace(", ", " ")
        self.headDate5 = self.headDate5.split()
        self.headYear5 = self.headDate5[2]
        self.headDay5 = self.headDate5[1]
        if self.headDate5[0] == "January":
            self.headMonth5 = "01"
        elif self.headDate5[0] == "February":
            self.headMonth5 = "02"
        elif self.headDate5[0] == "March":
            self.headMonth5 = "03"
        elif self.headDate5[0] == "April":
            self.headMonth5 = "04"
        elif self.headDate5[0] == "May":
            self.headMonth5 = "05"
        elif self.headDate5[0] == "June":
            self.headMonth5 = "06"
        elif self.headDate5[0] == "July":
            self.headMonth5 = "07"
        elif self.headDate5[0] == "August":
            self.headMonth5 = "08"
        elif self.headDate5[0] == "September":
            self.headMonth5 = "09"
        elif self.headDate5[0] == "October":
            self.headMonth5 = "10"
        elif self.headDate5[0] == "November":
            self.headMonth5 = "11"
        elif self.headDate5[0] == "December":
            self.headMonth5 = "12"
        #Fifth website
        self.label1 = tk.Label(self.frame, text = 'Metal Noise' , font='arial 20 bold', bg = 'PaleTurquoise1')
        self.label1.place(x=50, y=450)
        #Get month and year to access Metal Noise blog
        self.currentMonth = datetime.now().month
        if len(str(self.currentMonth)) == 1:
            self.currentMonth = "0" + str(self.currentMonth)
        self.currentYear = datetime.now().year
        #First page of website
        self.brave1 = tk.StringVar()
        self.entry13 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.brave1, bg ='antiquewhite2',width = 30,)
        self.entry13.place(x=50, y = 500)
        self.button13 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readBrave1)
        self.button13.place(x=50, y=525)
        self.bravePage1 = requests.get(f"https://metalnoise.net/{self.currentYear}/{self.currentMonth}")
        self.braveSoup1 = BeautifulSoup(self.bravePage1.content, 'html.parser')
        #Find and set the title of the article
        self.bravePageTitle1 = self.braveSoup1.select('h2')[1].text
        self.brave1.set(self.bravePageTitle1)
        #Second page of website
        self.brave2 = tk.StringVar()
        self.entry14 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.brave2, bg ='antiquewhite2',width = 30,)
        self.entry14.place(x=50, y = 560)
        self.button14 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readBrave2)
        self.button14.place(x=50, y=585)
        self.bravePage2 = requests.get(f"https://metalnoise.net/{self.currentYear}/{self.currentMonth}")
        self.braveSoup2 = BeautifulSoup(self.bravePage2.content, 'html.parser')
        #Find and set the title of the article
        self.bravePageTitle2 = self.braveSoup2.select('h2')[2].text
        self.brave2.set(self.bravePageTitle2)
        #Third page of website
        self.brave3 = tk.StringVar()
        self.entry15 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.brave3, bg ='antiquewhite2',width = 30,)
        self.entry15.place(x=50, y = 620)
        self.button15 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readBrave3)
        self.button15.place(x=50, y=645)
        self.bravePage3 = requests.get(f"https://metalnoise.net/{self.currentYear}/{self.currentMonth}")
        self.braveSoup3 = BeautifulSoup(self.bravePage3.content, 'html.parser')
        #Find and set the title of the article
        self.bravePageTitle3 = self.braveSoup3.select('h2')[3].text
        self.brave3.set(self.bravePageTitle3)
        #Fourth page of website
        self.brave4 = tk.StringVar()
        self.entry15 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.brave4, bg ='antiquewhite2',width = 30,)
        self.entry15.place(x=50, y = 680)
        self.button15 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readBrave4)
        self.button15.place(x=50, y=705)
        self.bravePage4 = requests.get(f"https://metalnoise.net/{self.currentYear}/{self.currentMonth}")
        self.braveSoup4 = BeautifulSoup(self.bravePage4.content, 'html.parser')
        #Find and set the title of the article
        self.bravePageTitle4 = self.braveSoup4.select('h2')[4].text
        self.brave4.set(self.bravePageTitle4)
        #Sixth website
        self.label2 = tk.Label(self.frame, text = 'The Killchain' , font='arial 20 bold', bg = 'PaleTurquoise1')
        self.label2.place(x=350, y=450)
        #First page of website
        self.kill1 = tk.StringVar()
        self.entry16 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.kill1, bg ='antiquewhite2',width = 40,)
        self.entry16.place(x=350, y = 500)
        self.button16 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readKill1)
        self.button16.place(x=350, y=525)
        self.killPage1 = requests.get("https://thoseonceloyal.wordpress.com/")
        self.killSoup1 = BeautifulSoup(self.killPage1.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.killPageTitle1 = self.killSoup1.select('h2')[5].text
        self.kill1.set(self.killPageTitle1)
        self.killDate1 = self.killSoup1.select('small')[0].text
        self.killDate1 = self.killDate1.replace(", ", " ")
        self.killDate1 = self.killDate1.split()
        self.killYear1 = self.killDate1[3]
        self.killDay1 = self.killDate1[2]
        if self.killDate1[1] == "January":
            self.killMonth1 = "01"
        elif self.killDate1[1] == "February":
            self.killMonth1 = "02"
        elif self.killDate1[1] == "March":
            self.killMonth1 = "03"
        elif self.killDate1[1] == "April":
            self.killMonth1 = "04"
        elif self.killDate1[1] == "May":
            self.killMonth1 = "05"
        elif self.killDate1[1] == "June":
            self.killMonth1 = "06"
        elif self.killDate1[1] == "July":
            self.killMonth1 = "07"
        elif self.killDate1[1] == "August":
            self.killMonth1 = "08"
        elif self.killDate1[1] == "September":
            self.killMonth1 = "09"
        elif self.killDate1[1] == "October":
            self.killMonth1 = "10"
        elif self.killDate1[1] == "November":
            self.killMonth1 = "11"
        elif self.killDate1[1] == "December":
            self.killMonth1 = "12"
        #Second page of website
        self.kill2 = tk.StringVar()
        self.entry17 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.kill2, bg ='antiquewhite2',width = 40,)
        self.entry17.place(x=350, y = 560)
        self.button17 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readKill2)
        self.button17.place(x=350, y=585)
        self.killPage2 = requests.get("https://thoseonceloyal.wordpress.com/")
        self.killSoup2 = BeautifulSoup(self.killPage2.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.killPageTitle2 = self.killSoup2.select('h2')[6].text
        self.kill2.set(self.killPageTitle2)
        self.killDate2 = self.killSoup2.select('small')[1].text
        self.killDate2 = self.killDate2.replace(", ", " ")
        self.killDate2 = self.killDate2.split()
        self.killYear2 = self.killDate2[3]
        self.killDay2 = self.killDate1[2]
        if self.killDate2[1] == "January":
            self.killMonth2 = "01"
        elif self.killDate2[1] == "February":
            self.killMonth2 = "02"
        elif self.killDate2[1] == "March":
            self.killMonth2 = "03"
        elif self.killDate2[1] == "April":
            self.killMonth2 = "04"
        elif self.killDate2[1] == "May":
            self.killMonth2 = "05"
        elif self.killDate2[1] == "June":
            self.killMonth2 = "06"
        elif self.killDate2[1] == "July":
            self.killMonth2 = "07"
        elif self.killDate2[1] == "August":
            self.killMonth2 = "08"
        elif self.killDate2[1] == "September":
            self.killMonth2 = "09"
        elif self.killDate2[1] == "October":
            self.killMonth2 = "10"
        elif self.killDate2[1] == "November":
            self.killMonth2 = "11"
        elif self.killDate2[1] == "December":
            self.killMonth2 = "12"
        #Third page of website
        self.kill3 = tk.StringVar()
        self.entry18 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.kill3, bg ='antiquewhite2',width = 40,)
        self.entry18.place(x=350, y = 620)
        self.button18 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readKill3)
        self.button18.place(x=350, y=645)
        self.killPage3 = requests.get("https://thoseonceloyal.wordpress.com/")
        self.killSoup3 = BeautifulSoup(self.killPage3.content, 'html.parser')
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.killPageTitle3 = self.killSoup3.select('h2')[7].text
        self.kill3.set(self.killPageTitle3)
        self.killDate3 = self.killSoup3.select('small')[2].text
        self.killDate3 = self.killDate3.replace(", ", " ")
        self.killDate3 = self.killDate3.split()
        self.killYear3 = self.killDate3[3]
        self.killDay3 = self.killDate3[2]
        if self.killDate3[1] == "January":
            self.killMonth3 = "01"
        elif self.killDate3[1] == "February":
            self.killMonth3 = "02"
        elif self.killDate3[1] == "March":
            self.killMonth3 = "03"
        elif self.killDate3[1] == "April":
            self.killMonth3 = "04"
        elif self.killDate3[1] == "May":
            self.killMonth3 = "05"
        elif self.killDate3[1] == "June":
            self.killMonth3 = "06"
        elif self.killDate3[1] == "July":
            self.killMonth3 = "07"
        elif self.killDate3[1] == "August":
            self.killMonth3 = "08"
        elif self.killDate3[1] == "September":
            self.killMonth3 = "09"
        elif self.killDate3[1] == "October":
            self.killMonth3 = "10"
        elif self.killDate3[1] == "November":
            self.killMonth3 = "11"
        elif self.killDate3[1] == "December":
            self.killMonth3 = "12"
        #Fourth page of website
        self.kill4 = tk.StringVar()
        self.entry18 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.kill4, bg ='antiquewhite2',width = 40,)
        self.entry18.place(x=350, y = 680)
        self.button18 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readKill4)
        self.button18.place(x=350, y=705)
        self.killPage4 = requests.get("https://thoseonceloyal.wordpress.com/")
        self.killSoup4 = BeautifulSoup(self.killPage4.content, 'html.parser')    
        #Find and set the title of the article
        #Date is necessary to access webpage
        self.killPageTitle4 = self.killSoup4.select('h2')[8].text
        self.kill4.set(self.killPageTitle4)
        self.killDate4 = self.killSoup4.select('small')[3].text
        self.killDate4 = self.killDate4.replace(", ", " ")
        self.killDate4 = self.killDate4.split()
        self.killYear4 = self.killDate4[3]
        self.killDay4 = self.killDate4[2]
        if self.killDate4[1] == "January":
            self.killMonth4 = "01"
        elif self.killDate4[1] == "February":
            self.killMonth4 = "02"
        elif self.killDate4[1] == "March":
            self.killMonth4 = "03"
        elif self.killDate4[1] == "April":
            self.killMonth4 = "04"
        elif self.killDate4[1] == "May":
            self.killMonth4 = "05"
        elif self.killDate4[1] == "June":
            self.killMonth4 = "06"
        elif self.killDate4[1] == "July":
            self.killMonth4 = "07"
        elif self.killDate4[1] == "August":
            self.killMonth4 = "08"
        elif self.killDate4[1] == "September":
            self.killMonth4 = "09"
        elif self.killDate4[1] == "October":
            self.killMonth4 = "10"
        elif self.killDate4[1] == "November":
            self.killMonth4 = "11"
        elif self.killDate4[1] == "December":
            self.killMonth4 = "12"
        #Seventh website
        self.label3 = tk.Label(self.frame, text = 'Metal Addicts' , font='arial 20 bold', bg = 'PaleTurquoise1')
        self.label3.place(x=650, y=450)
        #First page of website
        self.addict1 = tk.StringVar()
        self.entry19 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.addict1, bg ='antiquewhite2',width = 30,)
        self.entry19.place(x=650, y = 500)
        self.button19 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readAddict1)
        self.button19.place(x=650, y=525)
        self.addictPage1 = requests.get("https://metaladdicts.com/reviews/")
        self.addictSoup1 = BeautifulSoup(self.addictPage1.content, 'html.parser')
        #Find and set the title of the article
        self.addictPageTitle1 = self.addictSoup1.select('h3')[0].text
        self.addict1.set(self.addictPageTitle1)
        #Second page of website
        self.addict2 = tk.StringVar()
        self.entry20 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.addict2, bg ='antiquewhite2',width = 30,)
        self.entry20.place(x=650, y = 560)
        self.button20 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readAddict2)
        self.button20.place(x=650, y=585)
        self.addictPage2 = requests.get("https://metaladdicts.com/reviews/")
        self.addictSoup2 = BeautifulSoup(self.addictPage2.content, 'html.parser')
        #Find and set the title of the article
        self.addictPageTitle2 = self.addictSoup2.select('h3')[1].text
        self.addict2.set(self.addictPageTitle2)
        #Thirdt page of website
        self.addict3 = tk.StringVar()
        self.entry21 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.addict3, bg ='antiquewhite2',width = 30,)
        self.entry21.place(x=650, y = 620)
        self.button21 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readAddict3)
        self.button21.place(x=650, y=645)
        self.addictPage3 = requests.get("https://metaladdicts.com/reviews/")
        self.addictSoup3 = BeautifulSoup(self.addictPage3.content, 'html.parser')
        #Find and set the title of the article
        self.addictPageTitle3 = self.addictSoup3.select('h3')[2].text
        self.addict3.set(self.addictPageTitle3)
        #Fourth page of website
        self.addict4 = tk.StringVar()
        self.entry21 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.addict4, bg ='antiquewhite2',width = 30,)
        self.entry21.place(x=650, y = 680)
        self.button21 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readAddict4)
        self.button21.place(x=650, y=705)
        self.addictPage4 = requests.get("https://metaladdicts.com/reviews/")
        self.addictSoup4 = BeautifulSoup(self.addictPage4.content, 'html.parser')
        #Find and set the title of the article
        self.addictPageTitle4 = self.addictSoup4.select('h3')[3].text
        self.addict4.set(self.addictPageTitle4)
        #Eighth website
        self.label3 = tk.Label(self.frame, text = 'Metal Epidemic' , font='arial 20 bold', bg = 'PaleTurquoise1')
        self.label3.place(x=950, y=450)
        #First page of website
        self.epidemic1 = tk.StringVar()
        self.entry22 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.epidemic1, bg ='antiquewhite2',width = 30,)
        self.entry22.place(x=950, y = 500)
        self.button22 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readEpidemic1)
        self.button22.place(x=950, y=525)
        self.epidemicPage1 = requests.get("https://www.metalepidemic.com/reviews/", headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"})
        self.epidemicSoup1 = BeautifulSoup(self.epidemicPage1.content, 'html.parser')
        #Find and set the title of the article
        self.epidemicPageTitle1 = self.epidemicSoup1.select('h2')[0].text
        self.epidemic1.set(self.epidemicPageTitle1)
        #Second page of website
        self.epidemic2 = tk.StringVar()
        self.entry23 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.epidemic2, bg ='antiquewhite2',width = 30,)
        self.entry23.place(x=950, y = 560)
        self.button23 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readEpidemic2)
        self.button23.place(x=950, y=585)
        self.epidemicPage2 = requests.get("https://www.metalepidemic.com/reviews/", headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"})
        self.epidemicSoup2 = BeautifulSoup(self.epidemicPage2.content, 'html.parser')
        #Find and set the title of the article
        self.epidemicPageTitle2 = self.epidemicSoup2.select('h2')[1].text
        self.epidemic2.set(self.epidemicPageTitle2)
        #Third page of website
        self.epidemic3 = tk.StringVar()
        self.entry24 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.epidemic3, bg ='antiquewhite2',width = 30,)
        self.entry24.place(x=950, y = 620)
        self.button24 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readEpidemic3)
        self.button24.place(x=950, y=645)
        self.epidemicPage3 = requests.get("https://www.metalepidemic.com/reviews/", headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"})
        self.epidemicSoup3 = BeautifulSoup(self.epidemicPage3.content, 'html.parser')
        #Find and set the title of the article
        self.epidemicPageTitle3 = self.epidemicSoup3.select('h2')[2].text
        self.epidemic3.set(self.epidemicPageTitle3)
        #Fourth page of website
        self.epidemic4 = tk.StringVar()
        self.entry24 = tk.Entry(self.frame, font = 'arial 10 bold', textvariable = self.epidemic4, bg ='antiquewhite2',width = 30,)
        self.entry24.place(x=950, y = 680)
        self.button24 = tk.Button(self.frame, font = 'arial 13 bold', text = 'Read Article'  ,padx =5,bg ='LightCyan3' ,command = self.readEpidemic4)
        self.button24.place(x=950, y=705)
        self.epidemicPage4 = requests.get("https://www.metalepidemic.com/reviews/", headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"})
        self.epidemicSoup4 = BeautifulSoup(self.epidemicPage4.content, 'html.parser')
        #Find and set the title of the article
        self.epidemicPageTitle4 = self.epidemicSoup4.select('h2')[3].text
        self.epidemic4.set(self.epidemicPageTitle4)
        #Set the frame for the graphical interface
        self.frame.pack()
    #A series of functions to allow users to go to each displayed webpage from each
    #website
    def readAMG1(self):
        for s in self.amgPageTitle1:
            s = remove_characters(self.amgPageTitle1)
            self.amgPageTitle1 = s
        self.url = 'https://www.angrymetalguy.com/%s' %self.amgPageTitle1
        webbrowser.open(self.url)
        
    def readAMG2(self):
        for s in self.amgPageTitle2:
            s = remove_characters(self.amgPageTitle2)
            self.amgPageTitle2 = s
        self.url = 'https://www.angrymetalguy.com/%s' %self.amgPageTitle2
        webbrowser.open(self.url)

    def readAMG3(self):
        for s in self.amgPageTitle3:
            s = remove_characters(self.amgPageTitle3)
            self.amgPageTitle3 = s
        self.url = 'https://www.angrymetalguy.com/%s' %self.amgPageTitle3
        webbrowser.open(self.url)
        
    def readAMG4(self):
        for s in self.amgPageTitle4:
            s = remove_characters(self.amgPageTitle4)
            self.amgPageTitle4 = s
        self.url = 'https://www.angrymetalguy.com/%s' %self.amgPageTitle4
        webbrowser.open(self.url)
        
    def readAMG5(self):
        for s in self.amgPageTitle5:
            s = remove_characters(self.amgPageTitle5)
            self.amgPageTitle5 = s
        self.url = 'https://www.angrymetalguy.com/%s' %self.amgPageTitle5
        webbrowser.open(self.url)
        
    def readInjection1(self):
        self.injectionPageTitle1 = self.injectionPageTitle1.replace(": ", "")
        for s in self.injectionPageTitle1:
            s = remove_characters(self.injectionPageTitle1)
            self.injectionPageTitle1 = s
        self.url = f'https://www.nocleansinging.com/{self.injectionYear1}/{self.injectionMonth1}/{self.injectionDay1}/{self.injectionPageTitle1}'
        webbrowser.open(self.url)
        
    def readInjection2(self):
        self.injectionPageTitle2 = self.injectionPageTitle2.replace(": ", "")
        for s in self.injectionPageTitle2:
            s = remove_characters(self.injectionPageTitle2)
            self.injectionPageTitle2 = s
        self.url = f'https://www.nocleansinging.com/{self.injectionYear2}/{self.injectionMonth2}/{self.injectionDay2}/{self.injectionPageTitle2}'
        webbrowser.open(self.url)

    def readInjection3(self):
        self.injectionPageTitle3 = self.injectionPageTitle3.replace(": ", "")
        for s in self.injectionPageTitle3:
            s = remove_characters(self.injectionPageTitle3)
            self.injectionPageTitle3 = s
        self.url = f'https://www.nocleansinging.com/{self.injectionYear3}/{self.injectionMonth3}/{self.injectionDay3}/{self.injectionPageTitle3}'
        webbrowser.open(self.url)
        
    def readInjection4(self):
        self.injectionPageTitle4 = self.injectionPageTitle4.replace(": ", "")
        for s in self.injectionPageTitle4:
            s = remove_characters(self.injectionPageTitle4)
            self.injectionPageTitle4 = s
        self.url = f'https://www.nocleansinging.com/{self.injectionYear4}/{self.injectionMonth4}/{self.injectionDay4}/{self.injectionPageTitle4}'
        webbrowser.open(self.url)

    def readInjection5(self):
        self.injectionPageTitle5 = self.injectionPageTitle5.replace(": ", "")
        for s in self.injectionPageTitle5:
            s = remove_characters(self.injectionPageTitle5)
            self.injectionPageTitle5 = s
        self.url = f'https://www.nocleansinging.com/{self.injectionYear5}/{self.injectionMonth5}/{self.injectionDay5}/{self.injectionPageTitle5}'
        webbrowser.open(self.url)
        
    def readHeavy1(self):
        self.heavyPageTitle1 = self.heavyPageTitle1.replace("/", " ")
        for s in self.heavyPageTitle1:
            s = remove_characters(self.heavyPageTitle1)
            self.heavyPageTitle1 = s
        self.url = f'https://avenoctum.com/{self.heavyYear1}/{self.heavyMonth1}/{self.heavyDay1}/{self.heavyPageTitle1}'
        webbrowser.open(self.url)
        
    def readHeavy2(self):
        self.heavyPageTitle2 = self.heavyPageTitle2.replace("/", " ")
        for s in self.heavyPageTitle2:
            s = remove_characters(self.heavyPageTitle2)
            self.heavyPageTitle2 = s
        self.url = f'https://avenoctum.com/{self.heavyYear2}/{self.heavyMonth2}/{self.heavyDay2}/{self.heavyPageTitle2}'
        webbrowser.open(self.url)

    def readHeavy3(self):
        self.heavyPageTitle3 = self.heavyPageTitle3.replace("/", " ")
        for s in self.heavyPageTitle3:
            s = remove_characters(self.heavyPageTitle3)
            self.heavyPageTitle3 = s
        self.url = f'https://avenoctum.com/{self.heavyYear3}/{self.heavyMonth3}/{self.heavyDay3}/{self.heavyPageTitle3}'
        webbrowser.open(self.url)
        
    def readHeavy4(self):
        self.heavyPageTitle4 = self.heavyPageTitle4.replace("/", " ")
        for s in self.heavyPageTitle4:
            s = remove_characters(self.heavyPageTitle4)
            self.heavyPageTitle4 = s
        self.url = f'https://avenoctum.com/{self.heavyYear4}/{self.heavyMonth4}/{self.heavyDay4}/{self.heavyPageTitle4}'
        webbrowser.open(self.url)

    def readHeavy5(self):
        self.heavyPageTitle5 = self.heavyPageTitle5.replace("/", " ")
        for s in self.heavyPageTitle5:
            s = remove_characters(self.heavyPageTitle5)
            self.heavyPageTitle5 = s
        self.url = f'https://avenoctum.com/{self.heavyYear5}/{self.heavyMonth5}/{self.heavyDay5}/{self.heavyPageTitle5}'
        webbrowser.open(self.url)
        
    def readHead1(self):
        for s in self.headPageTitle1:
            s = remove_characters(self.headPageTitle1)
            self.headPageTitle1 = s
        self.url = f'https://headbangerreviews.wordpress.com/{self.headYear1}/{self.headMonth1}/{self.headDay1}/{self.headPageTitle1}'
        webbrowser.open(self.url)
        
    def readHead2(self):
        for s in self.headPageTitle2:
            s = remove_characters(self.headPageTitle2)
            self.headPageTitle2 = s
        self.url = f'https://headbangerreviews.wordpress.com/{self.headYear2}/{self.headMonth2}/{self.headDay2}/{self.headPageTitle2}'
        webbrowser.open(self.url)

    def readHead3(self):
        for s in self.headPageTitle3:
            s = remove_characters(self.headPageTitle3)
            self.headPageTitle3 = s
        self.url = f'https://headbangerreviews.wordpress.com/{self.headYear3}/{self.headMonth3}/{self.headDay3}/{self.headPageTitle3}'
        webbrowser.open(self.url)
        
    def readHead4(self):
        for s in self.headPageTitle4:
            s = remove_characters(self.headPageTitle4)
            self.headPageTitle4 = s
        self.url = f'https://headbangerreviews.wordpress.com/{self.headYear4}/{self.headMonth4}/{self.headDay4}/{self.headPageTitle4}'
        webbrowser.open(self.url)

    def readHead5(self):
        for s in self.headPageTitle5:
            s = remove_characters(self.headPageTitle5)
            self.headPageTitle5 = s
        self.url = f'https://headbangerreviews.wordpress.com/{self.headYear5}/{self.headMonth5}/{self.headDay5}/{self.headPageTitle5}'
        webbrowser.open(self.url)
        
    def readBrave1(self):
        for s in self.bravePageTitle1:
            s = remove_characters(self.bravePageTitle1)
            self.bravePageTitle1 = s
        self.url = f"https://metalnoise.net/{self.currentYear}/{self.currentMonth}/{self.bravePageTitle1}"
        webbrowser.open(self.url)
        
    def readBrave2(self):
        for s in self.bravePageTitle2:
            s = remove_characters(self.bravePageTitle2)
            self.bravePageTitle2 = s
        self.url = f"https://metalnoise.net/{self.currentYear}/{self.currentMonth}/{self.bravePageTitle2}"
        webbrowser.open(self.url)

    def readBrave3(self):
        for s in self.bravePageTitle3:
            s = remove_characters(self.bravePageTitle3)
            self.bravePageTitle3 = s
        self.url = f"https://metalnoise.net/{self.currentYear}/{self.currentMonth}/{self.bravePageTitle3}"
        webbrowser.open(self.url)
        
    def readBrave4(self):
        for s in self.bravePageTitle4:
            s = remove_characters(self.bravePageTitle4)
            self.bravePageTitle4 = s
        self.url = f"https://metalnoise.net/{self.currentYear}/{self.currentMonth}/{self.bravePageTitle4}"
        webbrowser.open(self.url)
        
    def readKill1(self):
        self.killPageTitle1 = " ".join(self.killPageTitle1.split())
        for s in self.killPageTitle1:
            s = remove_characters(self.killPageTitle1)
            self.killPageTitle1 = s
        self.url = f'https://thoseonceloyal.wordpress.com/{self.killYear1}/{self.killMonth1}/{self.killDay1}/{self.killPageTitle1}'
        webbrowser.open(self.url)
        
    def readKill2(self):
        self.killPageTitle2 = " ".join(self.killPageTitle2.split())
        for s in self.killPageTitle2:
            s = remove_characters(self.killPageTitle2)
            self.killPageTitle2 = s
        self.url = f'https://thoseonceloyal.wordpress.com/{self.killYear2}/{self.killMonth2}/{self.killDay2}/{self.killPageTitle2}'
        webbrowser.open(self.url)

    def readKill3(self):
        self.killPageTitle3 = " ".join(self.killPageTitle3.split())
        for s in self.killPageTitle3:
            s = remove_characters(self.killPageTitle3)
            self.killPageTitle3 = s
        self.url = f'https://thoseonceloyal.wordpress.com/{self.killYear3}/{self.killMonth3}/{self.killDay3}/{self.killPageTitle3}'
        webbrowser.open(self.url)
        
    def readKill4(self):
        self.killPageTitle4 = " ".join(self.killPageTitle4.split())
        for s in self.killPageTitle4:
            s = remove_characters(self.killPageTitle4)
            self.killPageTitle4 = s
        self.url = f'https://thoseonceloyal.wordpress.com/{self.killYear4}/{self.killMonth4}/{self.killDay4}/{self.killPageTitle4}'
        webbrowser.open(self.url)
        
    def readAddict1(self):
        for s in self.addictPageTitle1:
            s = remove_characters(self.addictPageTitle1)
            self.addictPageTitle1 = s
        self.url = 'https://metaladdicts.com/%s' %self.addictPageTitle1
        webbrowser.open(self.url)
        
    def readAddict2(self):
        for s in self.addictPageTitle2:
            s = remove_characters(self.addictPageTitle2)
            self.addictPageTitle2 = s
        self.url = 'https://metaladdicts.com/%s' %self.addictPageTitle2
        webbrowser.open(self.url)

    def readAddict3(self):
        for s in self.addictPageTitle3:
            s = remove_characters(self.addictPageTitle3)
            self.addictPageTitle3 = s
        self.url = 'https://metaladdicts.com/%s' %self.addictPageTitle3
        webbrowser.open(self.url)
        
    def readAddict4(self):
        for s in self.addictPageTitle4:
            s = remove_characters(self.addictPageTitle4)
            self.addictPageTitle4 = s
        self.url = 'https://metaladdicts.com/%s' %self.addictPageTitle4
        webbrowser.open(self.url)
        
    def readEpidemic1(self):
        for s in self.epidemicPageTitle1:
            s = remove_characters(self.epidemicPageTitle1)
            self.epidemicPageTitle1 = s
        self.url = 'https://www.metalepidemic.com/%s' %self.epidemicPageTitle1
        webbrowser.open(self.url)
        
    def readEpidemic2(self):
        for s in self.epidemicPageTitle2:
            s = remove_characters(self.epidemicPageTitle2)
            self.epidemicPageTitle2 = s
        self.url = 'https://www.metalepidemic.com/%s' %self.epidemicPageTitle2
        webbrowser.open(self.url)

    def readEpidemic3(self):
        for s in self.epidemicPageTitle3:
            s = remove_characters(self.epidemicPageTitle3)
            self.epidemicPageTitle3 = s
        self.url = 'https://www.metalepidemic.com/%s' %self.epidemicPageTitle3
        webbrowser.open(self.url)
        
    def readEpidemic4(self):
        for s in self.epidemicPageTitle4:
            s = remove_characters(self.epidemicPageTitle4)
            self.epidemicPageTitle4 = s
        self.url = 'https://www.metalepidemic.com/%s' %self.epidemicPageTitle4
        webbrowser.open(self.url)

#####################################
#USER-DEFINED FUNCTIONS
#####################################
#Function to set the graphical interface
def main():
    root = tk.Tk()
    root.geometry('1500x800')
    root.resizable(0,0)
    root.title("Heavy Metal Websites")
    root.config(bg ='LightCyan2')
    app = MainMenu(root)

#####################################
#RUN SCRIPT
#####################################
if __name__ == "__main__":
    main()