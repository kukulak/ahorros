from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.models import User
import time
from .models import Color, Plazo, Ahorro, Sistema, PrePlazo, Profile

from .example import sistema_Ahorro

from .example import Lista_total

from .forms import CantidadForm, LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, CreateNewSystem, CreatePlazoSystem, EmailShareForm, ArchiveSystem


from django.views import View
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

# packt

from django.contrib.auth.decorators import login_required

from django.core.exceptions import ValidationError
from django.core.mail import send_mail


# LOGIN DEL USUARIO P

def user_login(request):
    next = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if next:
                        return HttpResponseRedirect(next)
                    return HttpResponseRedirect('dashboard')
                    #return HttpResponse('Authenticated '\
                    #                    'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
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

    if sistema.user.id == request.user.id:
                                  
        ahorro = sistema.ahorros.all()                           
        #retorna el total ahorrado
        my_ahorro = Lista_total(list(ahorro))

        form = CantidadForm(request.POST)
        form_archived = ArchiveSystem(request.POST, instance=sistema)

        # if request.method == 'POST':
        #     if form.is_valid():
            
        #         archive = form_archived.save()
                
        #         messages.success(request, f'¡Archivaste {sistema.nombre}!')
        #         print("^^^ARCHIVED^^^")
        #         time.sleep(0.3)
        #         return redirect('/')
        # else:
        #     form_archived = ArchiveSystem()

        if request.method == 'POST':
            if form.is_valid():
            
                sistema = form.save()
                
                messages.success(request, f'¡Ahorraste ${sistema.cantidad}.00 para {sistema.sistema}!')
                print("^^^SAVED^^^")
                time.sleep(0.3)
                return redirect('/')
        else:
            form = CantidadForm()

        return render (request,
                    'ahorro/systemDetail.html',
                    {'sistema': sistema,
                    'ahorro': ahorro,
                    "my_ahorro": my_ahorro,
                    'form': form,
                    'form_archived': form_archived})
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
    t = 0
    st = 0
    meta_list = []
   
    print("-------")
    print(my_systems)
    print("-------")
    get_total = 0
    for ahorro in my_systems:
        get_total = Ahorro.objects.all().filter(sistema = my_systems[t])
        get_meta = my_systems[t]
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
            page_url = 'http://127.0.0.1:8000/'
            subject = '{} te recomienda "{}"'.format(user.username, page_url)
            message = '{} te recomiendo ahorrar con esta herramienta:"miLadoQueAhorra.com" ({}) '.format(cd['name'], page_url)
            send_mail(subject, message, 'admin@myblog.com', [cd['email']])
            sent = True
    else:
        form = EmailShareForm()
 


    return render(request,
                  'ahorro/dashboard.html',
                  {'section': 'dashboard',
                  'my_systems': my_systems,
                  'form': form,
                  'sent': sent,
                  'get_total': get_total})
     
@login_required
def archived(request):
    archived = Sistema.objects.all().filter(user=request.user.id, not_archived=False)
    t = 0
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

    return render(request,
                   'ahorro/archived.html',
                   {'archived': archived,})


# PACKT 
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'ahorro/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'ahorro/register.html',
                  {'user_form': user_form})            



@login_required
def edit(request):
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
            messages.success(request, 'Profile updated successfully')
        else: messages.error(request, 'Error updating your profile') 
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile)
    return render(request,
                  'ahorro/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})                  


def createSys(request):
    '''
    CON PLAZO INCLUIDO
    '''
    user = request.user
    if request.method == 'POST':
        sys_form = CreateNewSystem(request.POST)
        if sys_form.is_valid():
            
            new_sistema = sys_form.save(commit=False)
          
            new_sistema.user = request.user
            new_sistema.save()
            
                        
            messages.success(request, 'Ahorro creado con exito')

            return redirect('/')
          
        else:
            messages.error(request, 'Error al crear Ahorro')   
            return render(request, 'ahorro/createSystem.html', {'form': sys_form,} )
    else:
   
        form = CreateNewSystem(instance=request.user, initial={'user': request.user})
            
        return render(request,
                    'ahorro/createSystem.html',
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
            page_url = 'http://127.0.0.1:8000/'
            subject = '{} ({}) te recomienda "{}"'.format(cd['name'], cd['email'], '127.0.0')
            message = cd['name'], 'Te recomiendo ahorrar con esta herramienta:'.format(page_url, cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
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
        return redirect('/')

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