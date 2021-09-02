from django.core.management.base import BaseCommand, CommandError
from webpush import send_user_notification

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

from django.core.mail import send_mass_mail, EmailMultiAlternatives, send_mail



from django.template.loader import get_template
from django.template import Context

# plaintext = get_template('home/templates/mail_template.txt')
# htmly     = get_template('mail_template.html')



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
    mass_messages = []
    users = User.objects.all()
    ahorro = Ahorro.objects.all()
    user_ids = users.values_list('pk', flat=True)
    print(list(user_ids))
    print(user_ids)
    print('888888888')
    # sistemas = Sistema.objects.all().filter(user = 'valderrama')
    sistemas = Sistema.objects.all()

    febrero = 2
    todayMonth = datetime.datetime.now().month
    dt = datetime.datetime.today()


    # print(len(ahorro), "ahorro")
    for s in sistemas:
        if s.not_archived:
            # print('no archivados', s.user, 'esta ahorrando para', s)
            if dt.day % int(s.frecuencia) == 0 or todayMonth % int(s.frecuencia) == 0:
                if s.email:
                    d = Context({ 'username': s.user, 'nombreahorro': s })
                    subject = 'Es momento de ahorrar'
                    html_content = f'''Hola {s.user} hoy te toca ahorrar para {s}.
                    
                    ahorraAhora.app te ayuda a ahorrar.

                    Si ya no quieres recibir estos comunicados, entra a tu ahorro y desactiva los recordatorios por email.'''
                    # html_content = htmly.render(d)
                    # text_content = plaintext.render(d)
                    from_email = 'yaeshora@ahorraahora.app'
                    to = f'{s.user.email}'
                    message = (subject, html_content, from_email, [to])
                    # message = EmailMultiAlternatives(subject, html_content, from_email, [to])
                    # message.attach_alternative(html_content, "text/html")
                    mass_messages.append(message)

                    # send_mail(message)

                    print(s, 'aviso por mail')
                    # print('cuales mails y como', mass_messages)
                    print('Hola', s.user, 'hoy te toca ahorrar para:', s )

                # send_mass_mail((mass_messages), fail_silently=False)

                if s.push:
                    # push notification testing
                    payload = {"head": "¡Es momento de ahorrar!",
                            "body": f"Hola {s.user} Ahorra para {s}",
                            "icon": "https://i.imgur.com/dRDxiCQ.png",
                            "url": "https://ahorraahora.app"}
                    send_user_notification(user=s.user, payload=payload, ttl=1000)

                    print(s, 'aviso por push')
                    print('Hola', s.user, 'hoy te toca ahorrar para:', s )



        number = 0
        for a in ahorro:
            if a.sistema == s and s.not_archived == True:
                number += 1
                # print("len", a.sistema, number)
        if s.frecuencia != number and s.not_archived == True:
            # print('number', number)
            # print(s.user)
            # print(s.user.email)
            # print(s)
            # print(s.id)
            # print(s.frecuencia)
            print('=============')
            if dt.day % int(s.frecuencia) == 0:
                 # push notification testing
                # payload = {"head": "¡Es momento de ahorrar!",
                #         "body": f"Ahorra para {s}",
                #         "icon": "https://i.imgur.com/dRDxiCQ.png",
                #         "url": "https://www.example.com"}
                # send_user_notification(user=s.user, payload=payload, ttl=1000)

                # print('Hola', s.user, 'hoy te toca ahorrar para:', s )
                print('=============')
    
    print(User.objects.all())
    

    
    if febrero is todayMonth:
        if dt.day % 28 == 0:
            print('este es el caso cada mes')
        else:
            print('no pasara nada')    
        print('es febrero')
        print(dt.day)
    else:
        print('no es febrero')    
        print(datetime.datetime.now().month)

    send_mass_mail((mass_messages), fail_silently=False)
    print('cuales mails y como', mass_messages)

sender()

