from django.core.management.base import BaseCommand, CommandError

import pymysql

import os
import sys
sys.path.append(
    os.path.join(os.path.dirname(__file__), 'ahorrosite')
)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ahorrosite.settings")


import django

django.setup()

from django.conf import settings


from ahorro.models import Color, Plazo, Ahorro, Sistema, PrePlazo, Profile
from django.contrib.auth.models import User

import datetime

from time import strftime
import smtplib, ssl

from django.core.mail import send_mail

current_month = strftime('%B')




def mailCreation(ahorros, sistema, user, email, frecuencia, nombreAhorro, fechaCreacion):
    """
    creacion del mail para envio
    """



    # port = 465  # For SSL
    # password = input("Type your password and press enter: ")

    # # Create a secure SSL context
    # context = ssl.create_default_context()

    # with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    #     server.login("valderrama.christian@gmail.com", password)
    #     # TODO: Send email here
   

    if len(ahorros) > 0:
        if sistema > 0:
            for e in sistema:
                '''
                enviar mail a user:
                hola <user> es momento de ahorrar
                para lograr tu meta <nombreaAhorro>
                '''
                pass
        else:
            print('get one sistem')        
    else:
        print("usuario sin ahorros")            
    pass



def sender():
    users = User.objects.all()
    user_ids = users.values_list('pk', flat=True)
    print(list(user_ids))
    print(user_ids)
    sistemas = Sistema.objects.all().filter(user = 'valderrama')
    febrero = 2
    todayMonth = datetime.datetime.now().month
    dt = datetime.datetime.today()
    for s in sistemas:
        print(s.user)
        print(s.user.email)
        print(s)
        print(s.frecuencia)
        print('=============')
        if dt.day % int(s.frecuencia) == 0:
            print('Hola', s.user, 'hoy te toca ahorrar para:', s )
            print('=============')
    
    print(User.objects.all())
    if febrero is todayMonth:
        if dt.day % 15 == 0:
            print('este es el caso cada quince dias')
        elif dt.day % 28 == 0:
            print('este es el caso cada mes')
        elif dt.day % 1 == 0:
            print('este es el caso diario')
        else:
            print('no pasara nada')    
        print('es febrero')
        print(dt.day)
    else:
        print('no es febrero')    
        print(datetime.datetime.now().month)



sender()