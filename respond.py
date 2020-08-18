import os
import pyttsx3


pyttsx3.speak("WELCOME    .")
pyttsx3.speak("Nice to see you here.")
print("Nice to see you here")
pyttsx3.speak("Jarvis is at your service")
pyttsx3.speak("to be friends tell me your name")
name = input("What is your Name :: ").strip()

h = 1
pyttsx3.speak("DO you wish to open an application for any use")
p = input("Do you wish to open an application for any use (yes/no) :: ")

if  "n" in p or "exit" in p or "quit" in p:
    h = 0

if (h == 1) : 
    while True:
        pyttsx3.speak("What do you want to open ?")
        p = input("What do you want to open :: ").lower()
        l = " "        
        
        if ("run" in p or "open" in p or "execute" in p or "start" in p or "play" in p) and ("media" in p and "player" in p):
            h =[".mp4",".asf",".wma",".wmv",".wm",".mpg",".mpeg",".m1v",".mp2",".mp3",".mpa",".mpe",".m3u",".avi"]
            i = 0
            while i < 14:
                if h[i] in p:
                    i = h[i]
                    pyttsx3.speak("plz confirm the media file name")
                    l = input("confirm the media file name (by typing it again):: ")
                    break
                i = i + 1
            if i in h:
                pyttsx3.speak("Opening "+l)
                h = [os.system("wmplayer "+l), "wmplayer"]
            else:
                pyttsx3.speak("Opening Windows Media Player")
                h = [os.system("wmplayer"), "wmplayer"]
        elif ("run" in p or "open" in p or "execute" in p or "start" in p) and ("chrome" in p or "google" in p):
            h = ["search",".pdf"]
            i = 0
            while i < 2:
                if h[i] in p:
                    i = h[i]
                    pyttsx3.speak("plz confirm what do you want to search ")
                    l = input("confirm what do you want to search (by typing it again):: ").strip()
                    break
                i = i + 1
            if i in h:
                pyttsx3.speak("searching " + l)
                h = [os.system("start chrome " + l), "chrome"]
            else :
                pyttsx3.speak("Opening Chrome Browser")
                h = [os.system("start chrome"), "chrome"]
        elif ("run" in p or "open" in p or "execute" in p or "start" in p) and ("notepad" in p or "text" in p and "editor" in p):
            h =[".txt",".py",".jar",".java",".html",".css",".sass",".jnl",".CPP",".c"]
            i = 0
            while i < 10:
                if h[i] in p:
                    i = h[i]
                    pyttsx3.speak("plz confirm the file name")
                    l = input("confirm the file name (by typing it again):: ")
                    break
                i = i + 1
            if i in h:
                pyttsx3.speak("Opening " + l)
                h = [os.system("notepad " + l),"notepad"]
            else :
                pyttsx3.speak("Opening Notepad")
                h = [os.system("notepad"),"notepad"]
        elif ("run" in p or "open" in p or "execute" in p or "start" in p) and ("visual" in p and "code" in p):
            h =[".txt",".py",".jar",".java",".html",".css",".sass",".jnl",".CPP",".c"]
            i = 0
            while i < 10:
                if h[i] in p:
                    i = h[i]
                    pyttsx3.speak("plz confirm the file name")
                    l = input("confirm the file name (by typing it again):: ")
                    break
                i = i + 1
            if i in h:
                pyttsx3.speak("Opening " + l)
                h = [os.system("code "+l), "code"]
            else :
                pyttsx3.speak("Opening Visual Code")
                h = [os.system("code"), "code"]
        elif ("run" in p or "open" in p or "execute" in p or "start" in p) and ("visual" in p and "studio" in p):
            h =[".txt",".py",".jar",".java",".html",".css",".sass",".jnl",".CPP",".c"]
            i = 0
            while i < 10:
                if h[i] in p:
                    i = h[i]
                    pyttsx3.speak("plz confirm the file name")
                    l = input("confirm the file name (by typing it again):: ")
                    break
                i = i + 1
            if i in h:
                pyttsx3.speak("Opening " + l)
                h = [os.system("devenv "+l), "devenv"]
            else :
                pyttsx3.speak("Opening Visual Studio 2019")
                h = [os.system("devenv"), "devenv"]
        elif ("run" in p or "open" in p or "execute" in p or "start" in p) and ("atom" in p):
            h =[".txt",".py",".jar",".java",".html",".css",".sass",".jnl",".CPP",".c"]
            i = 0
            print("helo")
            while i < 10:
                if h[i] in p:
                    i = h[i]
                    pyttsx3.speak("plz confirm the file name")
                    l = input("confirm the file name (by typing it again):: ")
                    break
                i = i + 1
            if i in h:
                pyttsx3.speak("Opening " + l)
                h = [os.system("atom "+l), "atom"]
            else :
                pyttsx3.speak("Opening Atom")
                h = [os.system("atom"), "atom"]
        else :
            if "open" in p :
                h =[".txt",".py",".jar",".java",".html",".css",".sass",".jnl",".CPP",".c"]
                i = 0
                while i < 10:
                    if h[i] in p:
                        i = h[i]
                        pyttsx3.speak("plz confirm the file name")
                        l = input("confirm the file name (by typing it again):: ")
                        break
                    i = i + 1
                if i in h :
                    pyttsx3.speak("Opening " + l)
                    h = [os.system("notepad " + l), "notepad"]
                else :
                    h =[".mp4",".asf",".wma",".wmv",".wm",".mpg",".mpeg",".m1v",".mp2",".mp3",".mpa",".mpe",".m3u",".avi"]
                    i = 0
                    while i < 14:
                        if h[i] in p:
                            i = h[i]
                            pyttsx3.speak("plz confirm the media file name")
                            l = input("confirm the media file name (by typing it again):: ")
                            break
                        i = i + 1
                    if i in h:
                        pyttsx3.speak("Opening "+l)
                        h = [os.system("wmplayer "+l), "wmplayer"]
                    else :
                        h = ["search",".pdf"]
                        i = 0
                        while i < 2:
                            if h[i] in p:
                                i = h[i]
                                pyttsx3.speak("plz confirm what do you want to search")
                                l = input("confirm what do you want to search (by typing it again):: ").strip()
                                break
                            i = i + 1
                        if i in h:
                            pyttsx3.speak("searching " + l)
                            h = [os.system("start chrome " + l), "chrome"]
                        else :
                            pyttsx3.speak("APPLICATION NOT INSTALLED OR COMMUNICATION ERROR")
                            print("APPLICATION NOT INSTALLED OR COMMUNICATION ERROR")
            else :
                pyttsx3.speak("Sir , according to my diagnosis the Application is not installed.        Are you sure you have the specified software installed on the device")
                p = input("According to my diagnosis the Application is not installed. Are you sure you have the specified software installed on the device ? ::")
                if "n" in p or "exit" in p or "quit" in p:
                    pyttsx3.speak("I recommend you to first install the application")
                    print("I recommend you to first install the application :: ")
                    p = input("Will you install it now ? ")
                    if "n" in p or "exit" in p or "quit" in p:
                        print("As you wish")
                        pyttsx3.speak("As you wish")
                else:
                    print("I regret the inconvinience. Please Try Again")
                    pyttsx3.speak("I regret the inconvinience. Please Try Again")
                    continue
            

        if h[0] == 1:
            print(" Please update Enviornment Variables")
            pyttsx3.speak("Sir, then Please update Enviornment Variables")

        pyttsx3.speak("Sir, Will you like to open some another software.")
        p = input("Will you like to open some another software :: ")
        if "n" in p or "exit" in p or "quit" in p:
            pyttsx3.speak("BYE " + name)
            break
pyttsx3.speak("THANK YOU "+ name)
print("BYE " + name)