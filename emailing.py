# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:48:53 2019

@author: OCEAN
"""
import smtplib

sender = 'catchsaurabh0209@gmail.com'
receivers = ['catchsaurabh0209@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

smtpObj = smtplib.SMTP('www.gmail.com',25)
smtpObj.sendmail(sender, receivers, message)         
print ("Successfully sent email")
