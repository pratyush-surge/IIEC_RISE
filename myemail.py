import os
import pyttsx3
import smtplib
import ssl
import getpass

port = 465 
from_email = input("ENTER EMAIL ADDRESS : ")
password = getpass.getpass(prompt="ENTER PASSWORD : ")
to_email = input("TO : ")
Subject = input("SUBJECT : ")
Body = input("----------------------------------------------------\nBody : ")

message = """\
Subject: """+Subject+"""\
"""+Body+"""."""

# Create a secure SSL context
context = ssl.create_default_context()

# Using with smtplib.SMTP_SSL() as server: makes sure that the connection is automatically closed at the end of the indented code block.
# If port is zero, or not specified, .SMTP_SSL() will use the standard port for SMTP over SSL (port 465).

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(from_email, password)     # using SMTP_SSL()
    server.sendmail(from_email, to_email, message) 
