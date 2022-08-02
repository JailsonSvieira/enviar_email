# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 05:00:47 2022

@author: Jailson
"""
import smtplib
import email.message

nome = "teste"

def enviar_email():  
    corpo_email = f"""
    <h1>Parágrafo1</h1>
    <p> {nome} </p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'jailsonsantos347@gmail.com'
    msg['To'] = 'jailsonsantos347@gmail.com'
    password = 'lqthfmsdqkjwzfae' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()