from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from ahorro.views import ahorros, dashboard, register, edit, createSys, dashFierros, archived, userArchived, userArchivedF, userArchivedAM, userSystemFijo, createSysLaMetaEsAhorrar, userSystemAhorrarMeta
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'ahorro'
urlpatterns = [
   
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
  
    path("", views.dashboard, name="dashboard"),
    path("archived/", views.archived, name="archived"),
    path("estadistics/", views.dashFierros, name="estadistics"),
    path("informacion/", views.dashFierros, name="informacion"),
    path("contacto/", views.dashFierros, name="contacto"),
    
    path("crearSistema/", views.createSys, name="create"),
    path("crearSistemaFijo/", views.createSysFijo, name="createFijo"),
    path("crearSistemaLaMetaEsAhorrar/", views.createSysLaMetaEsAhorrar, name="createLaMetaEsAhorrar"),
    # path("crearPlazo/", views.createPla, name="createp"),
    path("register/", views.register, name="register"),
    
    path('', views.index, name='index'),
  
    path('ahorros', views.ahorros, name='ahorros'),
    path('<int:id>', views.ahorroDetalle, name='ahorroDetalle'),
    path('user', views.user, name='loguser'),
   
    path('system', views.system, name='system'),
    path('fijoSystem/<int:id>', views.userSystemFijo, name='fijoSystem'),
    path('MetaAhorrarSystem/<int:id>', views.userSystemAhorrarMeta, name='MetaAhorrarSystem'),
    path('userSystem/<int:id>', views.userSystem, name='userSystem'),
    path('userArchived/<int:id>', views.userArchived, name='userArchived'),
    path('userArchivedF/<int:id>', views.userArchivedF, name='userArchivedF'),
    path('userArchivedAM/<int:id>', views.userArchivedAM, name='userArchivedAM'),
  

    # change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('ahorro:password_change_done')), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('ahorro:password_reset_done')),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('ahorro:password_reset_complete')),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('edit/', views.edit, name='edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)