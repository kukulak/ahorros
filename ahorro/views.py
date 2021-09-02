from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# from helpers.decorators import auth_user_should_not_access
from validate_email import validate_email
from django.contrib.auth.models import User
import time
from .models import Color, Plazo, Ahorro, Sistema, PrePlazo, Profile, CantidadFija, AhorrarEsLaMeta

from .example import sistema_Ahorro
from .example import restArray

from .example import Lista_total

from .forms import CantidadForm, LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, CreateNewSystem, CreatePlazoSystem, EmailShareForm, ArchiveSystem, FormCantidadFija, CantidadFormF, CantidadFormAM, FormCantidadLaMetaEsAhorrar, FormEditarAhorros


from django.views import View
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from django.contrib.auth.decorators import login_required

from django.core.exceptions import ValidationError
from django.core.mail import send_mail, EmailMessage



from django.contrib.humanize.templatetags.humanize import intcomma

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.conf import settings

# LOGIN DEL USUARIO P


def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('authentication/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject,
                 body=email_body,
                 from_email=settings.EMAIL_FROM_USER,
                 to=[user.email]
                 )

    email.send()


def login_user(request):
    next = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        context = {'data': request.POST}
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # user = authenticate(request, username = username, password = password)
        
        # if user and not user.profile.is_email_verified:
        #         print("NO VERIFICADO")
        #         messages.error(request, 'Email is not verified, please check your email inbox')
        #         return render(request, 'registration/login.html', context, status=401)

        form = LoginForm(request.POST)

  ############     
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])

            if user and not user.profile.is_email_verified:
                print("NO VERIFICADO")
                messages.error(request, 'Tu email no está verificado, revisa tambien la bandeja de no deseados de tu cuenta de email')
                return render(request, 'registration/login.html', context, status=401)
            # de YT
            if not user:
                messages.error(request, 'Las credenciales no son validas, inténtalo otra vez')
                return render(request, 'registration/login.html', context, status=401)

            login(request, user)   

            # messages.success(request, f'Bienvenido {user.username}')
            
            return redirect(reverse('ahorro:dashboard'))

########
            # if user is not None:              
            #     if user.is_active:
            #         login(request, user)                    
            #         if next:
            #             print("VERIFICADO")
            #             return HttpResponseRedirect(next)
            #         if user and not user.profile.is_email_verified:
            #             print("NO VERIFICADO")
            #             messages.error(request, 'Email is not verified, please check your email inbox')
            #             return render(request, 'registration/login.html', context, status=401)
            #         return HttpResponseRedirect('dashboard')
            #         #return HttpResponse('Authenticated '\
            #         #                    'successfully')
            #     else:
            #         return HttpResponse('Disabled account')

                    
            # else:
            #     return HttpResponse('Invalid login')

    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})






def index(request):
    return HttpResponse("Hello, world. You're at the ahorro index.")

def user(request):
    return render (request, 'ahorro/inIndex.html')


def system(request):
    preplazo = PrePlazo.objects.all
    return render (request,
                   'ahorro/systemChoose.html',
                   {"preplazo": preplazo}) 

# def user system 

'''
EL SISTEMA COMPLETO
'''

def userSystem(request, id):
    sistema = get_object_or_404(Sistema,
                               id=id,)

    # if request.method == 'POST':         # If method is POST,
    #     sistema.delete()                     # delete the cat.
    #     return redirect('/')             # Finally, redirect to the homepage.

    if (request.GET.get('DeleteButton')):
        Sistema.objects.filter(id = request.GET.get('DeleteButton')).delete()
        return redirect('/')

    if (request.GET.get('ArchiveButton')):
        Sistema.objects.filter(id = request.GET.get('ArchiveButton')).update(not_archived = False)
        messages.success(request, f'¡Archivaste {sistema.nombre}!')
        print("^^^ARCHIVED^^^")
        return redirect('/')  

    # FormEditarAhorros      

    

    if sistema.user.id == request.user.id:
                                  
        ahorro = sistema.ahorros.all()                           
        #retorna el total ahorrado
        my_ahorro = Lista_total(list(ahorro))
        
        listaFinal = restArray(sistema.description, list(ahorro))

        form = CantidadForm(request.POST)
        form_archived = ArchiveSystem(request.POST, instance=sistema)

        formEditarAhorro = FormEditarAhorros(request.POST)
        formEditarAhorro.email = sistema.email

        if request.method == 'POST':
            if formEditarAhorro.is_valid():
                sistema.nombre = formEditarAhorro.cleaned_data['ahorro_nombre']
                sistema.email = formEditarAhorro.cleaned_data['email']
                sistema.push = formEditarAhorro.cleaned_data['push']
                sistema.save()
                # messages.succes(request, 'ahorro editado con éxito')
                print('editado', sistema.nombre)
                # return redirect('/')    
        else:
            formEditarAhorro = FormEditarAhorros()    



        if request.method == 'POST':
            if form.is_valid():
            
                sistemaForm = form.save()
                if (my_ahorro +sistemaForm.cantidad) == sistema.meta:
                    messages.success(request, f'¡Felicidades lograste tu meta de ${intcomma(sistema.meta)}.00!')
                    print("^^^SAVED^^^", my_ahorro, sistema.meta)
                    
                else:  
                    messages.success(request, f'¡Ahorraste ${intcomma(sistemaForm.cantidad)}.00 para {sistemaForm.sistema}!')
                    print("^^^SAVED^^^", my_ahorro, sistema.meta)
                time.sleep(0.3)
                return redirect('/')
        else:
            form = CantidadForm()

        return render (request,
                    'ahorro/systemDetail.html',
                    {'sistema': sistema,
                    'ahorro': ahorro,
                    'my_ahorro': my_ahorro,
                    'listaFinal': listaFinal,
                    'form': form,
                    'form_archived': form_archived,
                    'formEditarAhorro': formEditarAhorro
                    })
    else:
        print('something') 
        return redirect('/')
# end def user system







def ahorros(request):
    plazo = Plazo.objects.all()
    
    return render(request,
                 'ahorro/ahorros.html',
                 {'plazo': plazo})           


def ahorroDetalle(request, id):
    plazo = get_object_or_404(Plazo,
                              id=id,)
    ahorro = Ahorro.objects.all()                         

    return render(request,
                 'ahorro/ahorroDetalle.html',
                 {'plazo': plazo,
                 'ahorro': ahorro}) 



# #diferent aproach but the same 
# class Dashboard(LoginRequiredMixin, View):

#     # template_name = 'ahorro/dashboard.html'
    
#     def get(self, request):
#         # user = CustomUser.objects.filter(username=request.user).all()
#         sistema = Sistema.objects.filter(nombre=request.user).all()

#         context = { #'user': user
#                     'sistema': sistema
#                     }

#         return render(request, 'ahorro/dashboard.html', context)


@login_required
def dashboard(request):
    my_systems = Sistema.objects.all().filter(user=request.user.id, not_archived=True)
    my_systemsF = CantidadFija.objects.all().filter(user=request.user.id, not_archived=True) 
    my_systemsAM = AhorrarEsLaMeta.objects.all().filter(user=request.user.id, not_archived=True) 
    t = 0
    st = 0
    am = 0
    meta_list = []


    # Numero de visitas a esta view, como está contado en la variable de sesión.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
   
    print("-------")
    print(my_systemsAM)
    print("-------")
    get_total = 0
    get_totalF = 0
    for ahorro in my_systems:
        get_total = Ahorro.objects.all().filter(sistema = my_systems[t])
        get_meta = my_systems[t]
        print("resultado")
        print(get_total)
        print('after total')
        by_meta = Lista_total(list(get_total))
        ahorro.total_ahorrado = by_meta
        t = t + 1
        card_class = "simple"
        if by_meta == get_meta.meta:
            print("META CUMPLIDA LOGRO")
            card_class = "logro"
            ahorro.exito = card_class 
        else:
            print("SIMPLE NONE")
            card_class = "simple"
            ahorro.exito = card_class
            

    for ahorroF in my_systemsF:
        get_totalF = Ahorro.objects.all().filter(sistemaF = my_systemsF[st])
        get_meta = my_systemsF[st]
        by_meta = Lista_total(list(get_totalF))
        ahorroF.total_ahorrado = by_meta
        st = st + 1
        card_class = "simple"
        if by_meta >= get_meta.meta:
            print("META CUMPLIDA LOGRO")
            card_class = "logro"
            ahorroF.exito = card_class 
        else:
            print("SIMPLE NONE")
            card_class = "simple"
            ahorroF.exito = card_class   


    for ahorroAM in my_systemsAM:
        get_totalAM = Ahorro.objects.all().filter(sistemaAM = my_systemsAM[am])
        get_meta = my_systemsAM[am]
        by_meta = Lista_total(list(get_totalAM))
        ahorroAM.total_ahorrado = by_meta
        am = am + 1
        card_class = "simple"
        # if by_meta >= get_meta.meta:
        #     print("META CUMPLIDA LOGRO")
        #     card_class = "logro"
        #     ahorroAM.exito = card_class 
        # else:
        #     print("SIMPLE NONE")
        #     card_class = "simple"
        #     ahorroAM.exito = card_class      

    print("-------")
    print(my_systems)
    print("-------")

    user = request.user
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailShareForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            page_url = 'http://www.ahorraahora.app'
            subject = '{} te recomienda "{}"'.format(user.username, page_url)
            message = '{} te recomiendo ahorrar con esta herramienta:"ahorraahora.com" ({}) '.format(cd['name'], page_url)
            send_mail(subject, message, 'recordatorio@ahorraahora.com', [cd['email']])
            sent = True
    else:
        form = EmailShareForm()
 


    return render(request,
                  'ahorro/dashboard.html',
                  {'section': 'dashboard',
                  'my_systems': my_systems,
                  'my_systemsF': my_systemsF,
                  'my_systemsAM': my_systemsAM,
                  'form': form,
                  'sent': sent,
                  'get_total': get_total,
                  'get_totalF': get_totalF,
                  'num_visits':num_visits})
     
@login_required
def archived(request):
    archived = Sistema.objects.all().filter(user=request.user.id, not_archived=False)
    archivedF = CantidadFija.objects.all().filter(user=request.user.id, not_archived=False) 
    archivedAM = AhorrarEsLaMeta.objects.all().filter(user=request.user.id, not_archived=False) 
    t = 0
    st = 0
    am = 0

    for ahorro in archived:
        get_total = Ahorro.objects.all().filter(sistema = archived[t])
        get_meta = archived[t]
        by_meta = Lista_total(list(get_total))
        ahorro.total_ahorrado = by_meta
        t = t + 1
        card_class = "simple"
        if by_meta == get_meta.meta:
            print("META CUMPLIDA LOGRO")
            card_class = "logro"
            ahorro.exito = card_class 
        else:
            print("SIMPLE NONE")
            card_class = "simple"
            ahorro.exito = card_class


    for ahorroF in archivedF:
        get_totalF = Ahorro.objects.all().filter(sistemaF = archivedF[st])
        get_meta = archivedF[st]
        by_meta = Lista_total(list(get_totalF))
        ahorroF.total_ahorrado = by_meta
        st = st + 1
        card_class = "simple"
        if by_meta >= get_meta.meta:
            print("META CUMPLIDA LOGRO")
            card_class = "logro"
            ahorroF.exito = card_class 
        else:
            print("SIMPLE NONE")
            card_class = "simple"
            ahorroF.exito = card_class   


    for ahorroAM in archivedAM:
        get_totalAM = Ahorro.objects.all().filter(sistemaAM = archivedAM[am])
        get_meta = archivedAM[am]
        by_meta = Lista_total(list(get_totalAM))
        ahorroAM.total_ahorrado = by_meta
        am = am + 1
        card_class = "simple"
        # if by_meta >= get_meta.meta:
        #     print("META CUMPLIDA LOGRO")
        #     card_class = "logro"
        #     ahorroAM.exito = card_class 
        # else:
        #     print("SIMPLE NONE")
        #     card_class = "simple"
        #     ahorroAM.exito = card_class   



    return render(request,
                   'ahorro/archived.html',
                   {'archived': archived,
                   'archivedF': archivedF,
                   'archivedAM': archivedAM,})

# @auth_user_should_not_access


# old register
# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             # Create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # Set the chosen password
#             new_user.set_password(
#                 user_form.cleaned_data['password'])
#             # Save the User object
#             new_user.save()

#             # Create the user profile

#             Profile.objects.create(user=new_user)

#             send_activation_email(new_user, request )
#             messages.success(request, f'Enviamos un email a  {new_user.email} para activar tu cuenta')

            

#             return render(request,
#                         #   'ahorro/register_done.html',
#                           'registration/login.html',
#                           {'new_user': new_user})
#     else:
#         user_form = UserRegistrationForm()
#     return render(request,
#                   'ahorro/register.html',
#                   {'user_form': user_form})            
# endOLDREGISTER







# @auth_user_should_not_access
def register(request):
    if request.method == "POST":
        context = {'has_error': False, 'data': request.POST}
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        terminos = request.POST.get('terminos')
        aviso = request.POST.get('aviso')

        if terminos == False:
            messages.add_message(request, messages.ERROR,
                                 'Debes estar deacuerdo con los Terminos y Condiciones ')
            context['has_error'] = True

        if aviso == False:
            messages.add_message(request, messages.ERROR,
                                 'Debes estar deacuerdo con los Aviso de Privacidad ')
            context['has_error'] = True


        if len(password) < 6:
            messages.add_message(request, messages.ERROR,
                                 'El password debe tener al menos 6 caracteres')
            context['has_error'] = True

        if password != password2:
            messages.add_message(request, messages.ERROR,
                                 'Los passwords no coinciden')
            context['has_error'] = True

        if not validate_email(email):
            messages.add_message(request, messages.ERROR,
                                 'Pon un email válido')
            context['has_error'] = True

        if not username:
            messages.add_message(request, messages.ERROR,
                                 'Nombre es requerido')
            context['has_error'] = True

        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR,
                                 'Nombre en uso, escoge otro')
            context['has_error'] = True

            return render(request, 'ahorro/register.html', context, status=409)

        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,
                                 'Email en uso, usa otro email')
            context['has_error'] = True

            return render(request, 'ahorro/register.html', context, status=409)

        if context['has_error']:
            return render(request, 'ahorro/register.html', context)

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()

        Profile.objects.create(user=user)

        if not context['has_error']:

            send_activation_email(user, request)

            messages.add_message(request, messages.SUCCESS,
                                 'Te enviamos un email para verificar tu cuenta')
            return redirect('ahorro:login')

    return render(request, 'ahorro/register.html')









@login_required
def edit(request):
    user_date = request.user.profile.date_of_birth                            

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil actualizado con éxito')

            return redirect('/')

        else: messages.error(request, 'Error al actualizar perfil') 
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile)
    return render(request,
                  'ahorro/edit.html',
                  {'user_form': user_form,
                  'user_date': user_date,
                   'profile_form': profile_form})                  






##########
##############FORMULARIO
########### guardar el array desde el origen
##########



def createSys(request):
    '''
    CON PLAZO INCLUIDO con cantidades variables
    '''
    user = request.user
    if request.method == 'POST':
        sys_form = CreateNewSystem(request.POST)
        if sys_form.is_valid():
            
            new_sistema = sys_form.save(commit=False)
          
            new_sistema.user = request.user
            # rellenar la descripcion con el array de las cantidades asi no se tiene que computar esto cada vez que accedemos
            new_sistema.description = sistema_Ahorro(int(new_sistema.frecuencia), int(new_sistema.tiempo), int(new_sistema.meta))
            new_sistema.save()
            
                        
            messages.success(request, f'Ahorro {new_sistema.nombre.capitalize()} creado con éxito, <br/> <div class="smallmessage">tu mínimo a ahorrar es de {min(new_sistema.description)} y el máximo {max(new_sistema.description)}.</div>')

            return redirect('/')
          
        else:
            messages.error(request, 'Error al crear Ahorro')   
            return render(request, 'ahorro/createSystem.html', {'form': sys_form,} )
    else:
   
        form = CreateNewSystem(instance=request.user, initial={'user': request.user})
            
        return render(request,
                    'ahorro/createSystem.html',
                    {'form': form,})
  



def createSysFijo(request):
    '''
    CON PLAZO INCLUIDO Cantidad Fija
    '''
    user = request.user
    if request.method == 'POST':
        sys_form = FormCantidadFija(request.POST)
        if sys_form.is_valid():
            
            new_sistema = sys_form.save(commit=False)
          
            new_sistema.user = request.user
            new_sistema.save()
            
                        
            messages.success(request, 'Ahorro creado con éxito')

            return redirect('/')
          
        else:
            messages.error(request, 'Error al crear Ahorro')   
            return render(request, 'ahorro/createSystemFijo.html', {'form': sys_form,} )
    else:
   
        form = FormCantidadFija(instance=request.user, initial={'user': request.user})
            
        return render(request,
                    'ahorro/createSystemFijo.html',
                    {'form': form,})
  


def createSysLaMetaEsAhorrar(request):
    '''
    SIN PLAZO SIN META SOLO EL MOTIVO Y SI EL USUARIO QUIERE LA PERIODISIDAD
    '''
    user = request.user
    if request.method == 'POST':
        sys_form = FormCantidadLaMetaEsAhorrar(request.POST)
        if sys_form.is_valid():
            
            new_sistema = sys_form.save(commit=False)
          
            new_sistema.user = request.user
            new_sistema.save()
            
                        
            messages.success(request, 'Ahorro creado con éxito')

            return redirect('/')
          
        else:
            messages.error(request, 'Error al crear Ahorro')   
            return render(request, 'ahorro/createSystemLaMetaEsAhorrar.html', {'form': sys_form,} )
    else:
   
        form = FormCantidadLaMetaEsAhorrar(instance=request.user, initial={'user': request.user})
            
        return render(request,
                    'ahorro/createSystemLaMetaEsAhorrar.html',
                    {'form': form,})





def post_share(request, post_id):
    # Retrieve post by id
    user = request.user
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailShareForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            page_url = 'ahorraahora.com'
            subject = '{} ({}) te recomienda "{}"'.format(cd['name'], cd['email'], page_url)
            message = cd['name'], 'Te recomiendo ahorrar con esta herramienta:'.format(page_url, cd['comments'])
            send_mail(subject, message, 'recordatorio@ahorraahora.com', [cd['to']])
            sent = True
    else:
        form = EmailShareForm()
    return render(request, 'blog/post/share.html', {'user': user,
                                                    'form': form,
                                                    'sent': sent})

@login_required
def dashFierros(request):
    users = User.objects.all()
    plazo = Plazo.objects.all()                                  
    my_systems = Sistema.objects.all()
    my_systemsF = CantidadFija.objects.all()
    my_systemsAM = AhorrarEsLaMeta.objects.all()
    ahorro = Ahorro.objects.all()
    total_users = len(User.objects.all())
    t = 0
    full_total = 0
    full_total = Ahorro.objects.all()
    by_meta = Lista_total(list(full_total))
    # for ahorro in my_systems:
    #     ahorro.total_ahorrado = by_meta
    #     t = t + 1 

    return render(request,
                 'ahorro/dashboardFierros.html',
                 {'plazo': plazo,
                  'my_systems': my_systems,
                  'my_systemsF': my_systemsF,
                  'my_systemsAM': my_systemsAM,
                  'ahorro': ahorro,
                  'by_meta': by_meta,
                  'total_users': total_users,
                  'users': users}) 


'''
EL ARCHIVEDDETAIL COMPLETO
'''

def userArchived(request, id):
    sistema = get_object_or_404(Sistema,
                               id=id,)
    

    if (request.GET.get('DeleteButton')):
        Sistema.objects.filter(id = request.GET.get('DeleteButton')).delete()
        return redirect('/archived')
        # return redirect('/')




    if sistema.user.id == request.user.id:
                                  
        ahorro = sistema.ahorros.all()                           
        #retorna el total ahorrado
        my_ahorro = Lista_total(list(ahorro))

        form = CantidadForm(request.POST)
        if request.method == 'POST':
            form_archived = ArchiveSystem(request.POST, instance=sistema)
            if form_archived.is_valid:
            
                # sistema = form.save()
                # sistema = form
                form_archived.save()
                messages.success(request, f'¡Desarchivaste {sistema.nombre}!')
                print("^^^unArchived^^^")
                time.sleep(0.3)
                return redirect('/')
        else:
            print("the form was not valid")
            form = CantidadForm()
            form_archived = ArchiveSystem()

        return render (request,
                    'ahorro/archivedDetail.html',
                    {'sistema': sistema,
                    'ahorro': ahorro,
                    "my_ahorro": my_ahorro,
                    'form': form,
                    'form_archived': form_archived})
    else:
        print('something') 
        return redirect('/')

# end archived DETAIL






'''
EL ARCHIVEDDETAIL FIJO COMPLETO
'''

def userArchivedF(request, id):
    
    sistema = get_object_or_404(CantidadFija,
                               id=id,)
                 
    if (request.GET.get('DeleteButton')):
        CantidadFija.objects.filter(id = request.GET.get('DeleteButton')).delete()
        print("IAM LOST SO WHERE I AM")
        return redirect('/archived')

    if sistema.user.id == request.user.id:
                                  
        ahorro = sistema.ahorrosF.all()                           
        #retorna el total ahorrado
        my_ahorro = Lista_total(list(ahorro))

        form = CantidadForm(request.POST)
        if request.method == 'POST':
            form_archived = ArchiveSystem(request.POST, instance=sistema)
            if form_archived.is_valid:
            
                # sistema = form.save()
                # sistema = form
                form_archived.save()
                messages.success(request, f'¡Desarchivaste {sistema.nombre}!')
                print("^^^unArchived^^^")
                time.sleep(0.3)
                return redirect('/')
        else:
            print("El formulario no es valido en USERARCHIVEDF")
            form = CantidadForm()
            form_archived = ArchiveSystem()

        return render (request,
                    'ahorro/archivedDetail.html',
                    {'sistema': sistema,
                    'ahorro': ahorro,
                    "my_ahorro": my_ahorro,
                    'form': form,
                    'form_archived': form_archived})
    else:
        print('something') 
        return redirect('/')

# end archived FIJO DETAIL



'''
EL ARCHIVEDDETAIL AM AHORRAR ES LA META COMPLETO
'''

def userArchivedAM(request, id):
   
    sistema = get_object_or_404(AhorrarEsLaMeta,
                               id=id,)
                    
    if (request.GET.get('DeleteButton')):
        AhorrarEsLaMeta.objects.filter(id = request.GET.get('DeleteButton')).delete()
        print('IAMHEREDOYOUSEEME')
        return redirect('/archived')


    if sistema.user.id == request.user.id:
                                  
        ahorro = sistema.ahorrosAM.all()                           
        #retorna el total ahorrado
        my_ahorro = Lista_total(list(ahorro))

        form = CantidadForm(request.POST)
        if request.method == 'POST':
            form_archived = ArchiveSystem(request.POST, instance=sistema)
            if form_archived.is_valid:
            
                # sistema = form.save()
                # sistema = form
                form_archived.save()
                messages.success(request, f'¡Desarchivaste {sistema.nombre}!')
                print("^^^unArchived^^^")
                time.sleep(0.3)
                return redirect('/')
        else:
            print("El formulario no es valido en USERARCHIVEDAM")
            form = CantidadForm()
            form_archived = ArchiveSystem()

        return render (request,
                    'ahorro/archivedDetail.html',
                    {'sistema': sistema,
                    'ahorro': ahorro,
                    "my_ahorro": my_ahorro,
                    'form': form,
                    'form_archived': form_archived})
    else:
        print('something') 
        return redirect('/')

# end archived AM DETAIL





@login_required
def chooseSystems(request):
    users = User.objects.all()
    plazo = Plazo.objects.all()                                  
    my_systems = Sistema.objects.all()
    ahorro = Ahorro.objects.all()
    total_users = len(User.objects.all())
    t = 0
    full_total = 0
    full_total = Ahorro.objects.all()
    by_meta = Lista_total(list(full_total))
    # for ahorro in my_systems:
    #     ahorro.total_ahorrado = by_meta
    #     t = t + 1 

    return render(request,
                 'ahorro/systemChoose.html',
                 {'plazo': plazo,
                  'my_systems': my_systems,
                  'ahorro': ahorro,
                  'by_meta': by_meta,
                  'total_users': total_users,
                  'users': users}) 




'''
EL SISTEMA FIJO COMPLETO
'''

def userSystemFijo(request, id):
    sistema = get_object_or_404(CantidadFija,
                               id=id,)

    if (request.GET.get('DeleteButton')):
        CantidadFija.objects.filter(id = request.GET.get('DeleteButton')).delete()
        return redirect('/')

    if (request.GET.get('ArchiveButton')):
        CantidadFija.objects.filter(id = request.GET.get('ArchiveButton')).update(not_archived = False)
        messages.success(request, f'¡Archivaste {sistema.nombre}!')
        print("^^^ARCHIVED^^^")
        return redirect('/')    

    if sistema.user.id == request.user.id:
                                  
        ahorro = sistema.ahorrosF.all()                           
        #retorna el total ahorrado
        my_ahorro = Lista_total(list(ahorro))

        form = CantidadFormF(request.POST)
        form_archived = ArchiveSystem(request.POST, instance=sistema)

        formEditarAhorro = FormEditarAhorros(request.POST)
        formEditarAhorro.email = sistema.email

        if request.method == 'POST':
            if formEditarAhorro.is_valid():
                sistema.nombre = formEditarAhorro.cleaned_data['ahorro_nombre']
                sistema.email = formEditarAhorro.cleaned_data['email']
                sistema.push = formEditarAhorro.cleaned_data['push']
                sistema.save()
                # messages.succes(request, 'ahorro editado con éxito')
                print('editado', sistema.nombre)
                # return redirect('/')    
        else:
            formEditarAhorro = FormEditarAhorros()    



        if request.method == 'POST':
            if form.is_valid():
            
                sistemaForm = form.save()

                if (my_ahorro +sistemaForm.cantidad) == sistema.meta:
                    messages.success(request, f'¡Felicidades lograste tu meta de ${intcomma(sistema.meta)}.00!')
                    print("^^^SAVED^^^", my_ahorro, sistema.meta)

                else:
                    elSistema = str(sistemaForm.sistemaF)
                    messages.success(request, f'¡Ahorraste ${intcomma(sistemaForm.cantidad)}.00 para {elSistema.upper()}!')
                    print("^^^SAVED^^^")
                time.sleep(0.3)
                return redirect('/')
        else:
            form = CantidadFormF()

        return render (request,
                    'ahorro/systemDetailFijo.html',
                    {'sistema': sistema,
                    'ahorro': ahorro,
                    "my_ahorro": my_ahorro,
                    'form': form,
                    'form_archived': form_archived,
                    'formEditarAhorro': formEditarAhorro
                    })
    else:
        return redirect('/')
# end def user system







'''
EL SISTEMA LA META ES AHORRAR COMPLETO
    AHORRAR ES LA META
'''

def userSystemAhorrarMeta(request, id):
    sistema = get_object_or_404(AhorrarEsLaMeta,
                               id=id,)

    if (request.GET.get('DeleteButton')):
        AhorrarEsLaMeta.objects.filter(id = request.GET.get('DeleteButton')).delete()
        return redirect('/')

    if (request.GET.get('ArchiveButton')):
        AhorrarEsLaMeta.objects.filter(id = request.GET.get('ArchiveButton')).update(not_archived = False)
        messages.success(request, f'¡Archivaste {sistema.nombre}!')
        print("^^^ARCHIVED^^^")
        return redirect('/')    

    if sistema.user.id == request.user.id:
                                  
        ahorro = sistema.ahorrosAM.all()                           
        #retorna el total ahorrado
        my_ahorro = Lista_total(list(ahorro))

        form = CantidadFormAM(request.POST)
        form_archived = ArchiveSystem(request.POST, instance=sistema)

        formEditarAhorro = FormEditarAhorros(request.POST)
        formEditarAhorro.email = sistema.email

        if request.method == 'POST':
            if formEditarAhorro.is_valid():
                sistema.nombre = formEditarAhorro.cleaned_data['ahorro_nombre']
                sistema.email = formEditarAhorro.cleaned_data['email']
                sistema.push = formEditarAhorro.cleaned_data['push']
                sistema.save()
                # messages.succes(request, 'ahorro editado con éxito')
                print('editado', sistema.nombre)
                # return redirect('/')    
        else:
            formEditarAhorro = FormEditarAhorros()    


        if request.method == 'POST':
            if form.is_valid():
            
                sistema = form.save()
                elSistema = str(sistema.sistemaAM)
                messages.success(request, f'¡Ahorraste ${intcomma(sistema.cantidad)}.00 para {elSistema.upper()}!')

                # if user_form.is_valid() and profile_form.is_valid():
                #     user_form.save()
                #     profile_form.save()
                #     messages.success(request, 'Perfil actualizado con éxito')
                # else: messages.error(request, 'Error al actualizar perfil') 

                print("^^^SAVED MEGA^^^")
                time.sleep(0.3)
                return redirect('/')
            else:
                print(CantidadFormAM().non_field_errors()) 
                form = CantidadFormAM()
                messages.error(request, 'Eso es demaciado intentalo de nuevo') 

        else:
            form = CantidadFormAM()

        return render (request,
                    'ahorro/systemLaMetaEsAhorrar.html',
                    {'sistema': sistema,
                    'ahorro': ahorro,
                    "my_ahorro": my_ahorro,
                    'form': form,
                    'form_archived': form_archived,
                    'formEditarAhorro': formEditarAhorro
                    })
    else:
        return redirect('/')
# end def user system


def activate_user(request, uidb64, token):

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.profile.is_email_verified = True
        user.profile.save()
        # user.save()
        # Profile.objects.save(user=user)

        messages.success(request, 'Cuenta verificada')

        # return redirect('registration/login.html')
        return redirect(reverse('ahorro:login'))

        

    return render(request,
                 'authentication/activate-failed.html', {'user': user})    


def terminos(request):
    return render(request, 'avisos/terminos-condiciones.html')


def privacidad(request):
    return render(request, 'avisos/privacidad-y-cookies.html')    