
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import home, comprar, comprarForm, CompraUpdate, CompraDelete, profesores, profesoresForm, profesoresUpdate, profesoresDelete, VisitantesList, VisitantesCreate, VisitantesUpdate, loginRequest, register, editProfile, CambiarClave, agregarAvatar,ProfUpdate,ProfDelete, busqueda_profesion, buscar,alumnos,alumno_form,AlumnoUpdate,AlumnoDelete,proveedores,proveedor_form,ProvUpdate,ProvDelete
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    #Compras
    path('comprar/', comprar, name="comprar"),
    path('comprarForm/', comprarForm, name="comprarForm"),
    path('comprarUpdate/<int:pk>', CompraUpdate.as_view(), name="comprarUpdate"),
    path('comprarDelete/<int:pk>', CompraDelete.as_view(), name="comprarDelete"),

    #Profesores
    path('profesores/', profesores, name="profesores"),
    path('profesoresForm/', profesoresForm, name="profesoresForm"),
    path('profesorUpdate/<int:pk>', ProfUpdate.as_view(), name="profesorUpdate"),        
    path('profesorDelete/<int:pk>', ProfDelete.as_view(), name="profesorDelete"),
    path('busquedaProf/', busqueda_profesion, name='BusquedaProfesion'),
    path('buscar/', buscar, name='BuscarProfesion'),  
    
    #Alumnos
    path('alumnos/', alumnos, name="alumnos"),
    path('alumnoForm/', alumno_form, name="alumnoForm"),
    path('alumnoUpdate/<int:pk>', AlumnoUpdate.as_view(), name="alumnoUpdate"),
    path('alumnoDelete/<int:pk>', AlumnoDelete.as_view(), name="alumnoDelete"),

    #Proveedores
    path('proveedores/', proveedores, name="proveedores"),
    path('proveedorForm/', proveedor_form, name="proveedorForm"),
    path('proveedorUpdate/<int:pk>', ProvUpdate.as_view(), name="proveedorUpdate"),
    path('proveedorDelete/<int:pk>', ProvDelete.as_view(), name="proveedorDelete"),

    #Visitantes
    path('projects/', VisitantesList.as_view(), name="visitantes"),
    path('visitantesCreate/', VisitantesCreate.as_view(), name="visitantesCreate"),
    path('visitantesUpdate/<int:pk>/', VisitantesUpdate.as_view(), name="visitantesUpdate"),


    #login/logout/registration
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name="logout"),    
    path('registro/', register, name="registro"),

    #Edicion
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),  
]

