import os
import pyttsx3
import datetime
import pytz
import getpass

name = ""
password = 0

# checking whether the file username.txt already exists
if not(os.path.isfile(".username.txt")):
    # Taking the start
    pyttsx3.speak("JARVIS is Online")
    print("Jarvis is online.")
    pyttsx3.speak("Lets Start the conversation.")
    pyttsx3.speak("So      ,    what is your name.") # asking for the username first time the program runs
    name = input("What is your full Name :: ").strip() # storing the input into variable name ad removing the leading and trailing blank spaces
    td = open("usernamedetail.txt","w+") # creating and opening a file in jarvis folder
    td.write(name) # storing the full name of the user in the file

    pyttsx3.speak("SET A USER NAME")
    name = input("USERNAME :: ")
    td.write(name)# storing the user name

    pyttsx3.speak("would you like to set a password")
    while True :
        print("Would you like to set a password (yes/no) :: ", end = "")
        n = input().lower()
        if "y" in n or "of course" in n or "sure" in n :
            i = 0
            while True :
                password = getpass.getpass(prompt="ENTER THE NEW PASSWORD :: ")
                password2 = getpass.getpass(prompt="ENTER THE NEW PASSWORD AGAIN :: ")
                if password == password2 :
                    break
                elif i == 4 :
                    pyttsx3.speak("Set it Later")
                    print("Set it Later")
                    i = 8
                    break
                else :
                    pyttsx3.speak("Password mismatch")
                    print("Password mismatch")
                i = i + 1
            if (i != 8) :
                td.write(password)
            break
        elif "n" in n :
            break
        else :
            pyttsx3.speak("unrecognised typo")
            print("unrecognised typo")
else :
    pyttsx3.speak("JARVIS is back online")
    td = open("username.txt","r") # opening the file username to read
    name = td.readline() # reading the file line by line
    name = td.readline() # reading the file line by line
    pass2= td.readline() # reading the file line by line
    password = getpass.getpass(prompt="PASSWORD :: ") # asking the user to confirm username
    i = 0
    while True :
        if pass2 == password:
            pyttsx3.speak("Nice to see you back " + name)
            break
        else :
            print("   WRONG PASSWORD!    ")
            print("Only %i attempts left!", 4-i)
            pyttsx3.speak("Wrong Password")
            pyttsx3.speak(4-i)
            pyttsx3.speak("Attempts Left")
            if(5 % i == 0) :
                pyttsx3.speak("To many attempts")
                print("Wait .......")
                if o == 1:
                    sleep(60 * 5)
                elif o == 2:
                    sleep(60 * 15)
                elif o == 3:
                    sleep(60 * 30)
                elif o == 4:
                    sleep(60 * 60)
                elif o == 5:
                    sleep(60 * 60 * 6)
                elif o == 6:
                    sleep(60 * 60 * 12)
                elif o == 7:
                    sleep(60 * 60 * 24)
                elif o == 8:
                    sleep(60 * 60 * 24 *2)
                elif o == 9:
                    sleep(60 * 60 * 24 *5)
                elif o == 10:
                    pyttsx3.speak("YOU Intruder GET OUT")
                    print("you intruder get out")
                    exit(0)
        i = i + 1

# getting the date and time in a object t of datetime
t = datetime.datetime.now()

# greeting the user
if t.hour < 12 :
    pyttsx3.speak("GOOD MORNING")
elif t.hour == 12 and t.min == 0 :
    pyttsx3.speak("GOOD NOON")
elif t.hour > 11 and t.hour < 4 :
    pyttsx3.speak("GOOD AFTERNOON")
else :
    pyttsx3.speak("GOOD EVENING")  

# calculating the day like monday,tuesday......
td = datetime.date(int(t.year), int(t.month), int(t.day))
pyttsx3.speak("Today is "+ td.strftime("%A"))

while True :
    pyttsx3.speak("DO you wish to open an application for any use")
    p = input("Do you wish to open an application for any use (yes/no) :: ")
    if "n" in p:
        h = 0
        break
    if "y" in n or "of course" in n or "sure" in n :
        h = 1
        break
    else :
        pyttsx3.speak("unrecognised typo")
        print("unrecognised typo")

while True:
    # terminatinig the program if user had shown no intrest
    if (h != 1) :
        exit(0)

    pyttsx3.speak("What do you want to open ?")
    p = input("What do you want to open :: ").lower()
    l = " "        
    
    #opening windows media player
    if ("media" in p and "player" in p):
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
    #opening chrome
    elif ("chrome" in p or "google" in p):
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
            h = [os.system("chrome"), "chrome"]
    #opening virtual box
    elif ("virtualbox" in p):
        pytttsx3.speak("opening ORACLE VIRTUAL BOX")
        h = [os.system("VirtualBox"), "VirtualBox"]
    #opening discord
    elif ("discord" in p):
        pytttsx3.speak("opening discord")
        h = [os.system("discord"), "discord"]
    #opening cmd
    elif "cmd" in p or ("command" in p and ("prompt" in p or "line" in p)):
        pytttsx3.speak("opening windows command prompt")
        h = [os.system("cmd"), "cmd"]
    #opening control panel
    elif ("control" in p and "panel" in p) or ("windows" in p and "administrative" in p and "tool" in p):
        pytttsx3.speak("opening Control Panel")
        h = [os.system("Control Panel"), "Control Panel"]
    #opening Recycle Bin
    elif ("Recycle" in p and "Bin" in p):
        pytttsx3.speak("opening Recycle Bin")
        h = [os.system("Recycle Bin"), "Recycle Bin"]
    #opening ONeDRIVE
    elif ("one" in p and "drive"in p):
        pytttsx3.speak("opening onedrive")
        h = [os.system("OneDrive"), "OneDrive"]
    #opening Libraries
    elif "libraries" in p or ("file" in p and "explorer" in p) :
        pytttsx3.speak("opening file explorer")
        h = [os.system("Libraries"), "Libraries"]
    #opening this Pc
    elif ("this" in p or "my" in p) and ("pc" in p or "computer" in p):
        pytttsx3.speak("opening THIS Pc")
        h = [os.system("This PC"), "This PC"]
    #opening system networks
    elif "network" in p :
        pytttsx3.speak("opening Networks")
        h = [os.system("Network"), "Network"]
    #opening RUN
    elif "run" in p:
        pytttsx3.speak("opening run")
        h = [os.system("run"), "run"]
    #opening unity hub
    elif "unity" in p :
        pytttsx3.speak("opening UNITY HUB")
        h = [os.system("Unity Hub"), "Unity Hub"]
    #opening unity hub
    elif "edge" in p :
        pytttsx3.speak("opening Microsoft Edge")
        h = [os.system("msedge"), "msedge"]
    #opening ADobe Acrobat reader
    elif "AcroRd#2" in p :
        pytttsx3.speak("opening Adobe Acrobat")
        h = [os.system("AcroRd32"), "AcroRd32"]
    #opening Maxx Audio Pro
    elif "waves" in p and ("max" in p or "audio" in p):
        pytttsx3.speak("opening Waves Maxx Audio Pro")
        h = [os.system("MaxxAudioPro"), "MaxxAudioPro"]
    #opening notepad
    elif ("notepad" in p or "text" in p) and "editor" in p:
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
    #opening Visual code
    elif ("visual" in p and "code" in p):
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
    # opening Visual studios 2019
    elif ("visual" in p and "studio" in p):
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
    # opening atom
    elif ("atom" in p):
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
    # to open a file
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
            p = input("According to my diagnosis the Application is not installed.\n Are you sure you have the specified software installed on the device ? ::")
            if "n" in p or "exit" in p or "quit" in p:
                pyttsx3.speak("I recommend you to first install the application")
                print("I recommend you to first install the application :: ")
                p = input("Will you install it now ? ")
                if "n" in p or "exit" in p or "quit" in p:
                    print("OK")
                    pyttsx3.speak("Ok")
            else:
                print("I regret the inconvinience. Please Try Again by typing in whole name")
                pyttsx3.speak("I regret the inconvinience. Please Try Again")
                continue
    # if an application was not opened then h[0] was supposed to be one so telling the user to update enviornment variables
    if h[0] == 1:
        print(" Please update Enviornment Variables")
        pyttsx3.speak("Sir, then Please update Enviornment Variables")
    #asking the user whether he will open something more
    pyttsx3.speak("Sir, Will you like to open some another software.")
    while i < 5:
        i = i + 1
        p = input("Will you like to open some another software (yes/no):: ")
        if "n" in p or "exit" in p or "quit" in p:
            h = 1
            break
        elif not("y" in n or "of course" in n or "sure" in n) :
            pyttsx3.speak("unrecognised typo")
            print("unrecognised typo")
     h = 1
#termination
pyttsx3.speak("Bye "+ name)
print("BYE " + name)
exit(0)
