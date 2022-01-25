# -*- coding: latin-1 -*-

import smtplib

gmail_user = 'xxxxxxx'
gmail_password = 'xxxxxxx'

sent_from = gmail_user
to = ['daneil2711@gmail.com']
subject = 'Pythao mandando email'
body = """Pai é brabo, 
CHUPA ESSA ROLA"""

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')
