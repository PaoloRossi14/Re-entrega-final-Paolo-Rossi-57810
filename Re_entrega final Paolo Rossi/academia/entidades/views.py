from django.shortcuts import render, redirect

from .models import *

from .forms import *

from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect

## https://github.com/NormanBeltran/Comision-57810/blob/clase22/Clase_21/academia/academia/urls.py#L22

# Create your views here.
def home(request):
    return render(request,"entidades/index.html")

@login_required
def comprar(request):
    if request.user.is_authenticated:
        contexto= {"comprar":Compras.objects.all()}
        return render(request,"entidades/comprar.html", contexto)
    else:
        return render(request,"entidades/login.html")    
    

class CompraUpdate(UpdateView):
    model = Compras
    template_name = 'entidades/compUpdate.html'
    fields= ('__all__')
    success_url = '/comprar/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['compra'] = self.object  # Asegura que el objeto compra esté en el contexto
        return context

class CompraDelete(DeleteView):
  model = Compras
  template_name = 'entidades/compDelete.html'
  fields= ('__all__')  
  success_url = '/comprar/'  # Redirige a la lista de compras

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['compra'] = self.object  # Asegura que el objeto 
        return context
 

@login_required
def visitantes(request):
    contexto= {"visitantes":Visitantes.objects.all()}
    return render(request,"entidades/visitantes.html", contexto)

@login_required
def profesores(request):        
    
    if request.user.is_authenticated:
    
        contexto = {"profesores":Profesores.objects.all()}
        return render(request,"entidades/profesores.html", contexto)    
    else:
        return render(request,"entidades/login.html")    
   

 # Compras 
@login_required
def comprarForm(request):
    if request.method =="POST":
        form = ComprasForm(request.POST)
        if form.is_valid():
            comprar_nombre =form.cleaned_data.get("nombre")
            comprar_stock=form.cleaned_data.get("stock")
            comprar_size=form.cleaned_data.get("size")
            comprar_precio=form.cleaned_data.get("precio")
            comprar = Compras(nombre=comprar_nombre, stock= comprar_stock, size=comprar_size, precio=comprar_precio)
            comprar.save()
            contexto = {"comprar": Compras.objects.all()}
            return render(request,"entidades/comprar.html", contexto)
        else:
            return render(request, "entidades/home.html",{"message":"Datos incorrectos"})    
    else:
        form = ComprasForm()
        return render(request, "entidades/comprarForm.html", {"form": form})




#Profesores

def profesor(nombre, edad,horarios, profesion):
    nuevo_prof = Profesores(nombre=nombre, edad=edad, horarios=horarios,profesion=profesion)
    nuevo_prof.save()

    return HttpResponse(f""" <p>Profesor: {nuevo_prof.nombre} creado!<p>""")

@login_required
def profesoresForm(request):
    if request.method == "POST":
        form = ProfesoresForm(request.POST)

        if form.is_valid():
            profesores_nombre = form.cleaned_data.get("nombre")
            profesores_edad= form.cleaned_data.get("edad")
            profesores_horarios= form.cleaned_data.get("horarios")
            profesores_profesion= form.cleaned_data.get("profesion")
            profesores = Profesores(nombre=profesores_nombre, edad=profesores_edad, horarios=profesores_horarios, profesion=profesores_profesion)
            profesores.save()
            contexto = {"profesores": Profesores.objects.all()}
            return render(request,"entidades/profesores.html", contexto)
            ## return render(request, 'entidades/home.html', {"message":"Profesor creado con éxito"})
        else:
            return render(request, "entidades/home.html",{"message":"Datos incorrectos"})    
    else:
        form = ProfesoresForm()
        return render(request, "entidades/profesoresForm.html", {"form": form})


@login_required
def profesoresUpdate(request,id_profesores):    
    profesores = Profesores.objects.get(id =id_profesores)

    if request.method == "POST":
        form = ProfesoresForm(request.POST)
        if form.is_valid():
            
            profesores.nombre =form.cleaned_data.get("nombre")
            profesores.edad= form.cleaned_data.get("edad")
            profesores.horarios= form.cleaned_data.get("horarios")
            profesores.profesion=form.cleaned_data.get("profecion")    
            profesores.save()
            contexto = {"profesores": Profesores.objects.all()}
            return render(request,"entidades/profesores.html", contexto)
        else:
            return render(request,"entidades/home.html", {"message": "Datos no válidos"})
    else:
        form = ProfesoresForm(initial={"nombre" : profesores.nombre, "edad" : profesores.edad, "horarios" : profesores.horarios, "profesion" : profesores.profesion})
        return render(request, "entidades/profesoresForm.html", {"form": form})

@login_required
def profesoresDelete(request, id_profesores):
    profesores = Profesores.objects.get(id=id_profesores)
    profesores.delete()
    contexto = {"profesores": Profesores.objects.all()}
    return render(request,"entidades/profesores.html", contexto)

class VisitantesList(LoginRequiredMixin, ListView):
    model = Visitantes


class VisitantesCreate(LoginRequiredMixin, CreateView):
    model = Visitantes
    fields =["nombre", "apellido", "email"]
    success_url = reverse_lazy("visitantes")


class VisitantesUpdate(LoginRequiredMixin, UpdateView):
    model = Visitantes
    fields =["nombre", "apellido", "email"]
    success_url = reverse_lazy("visitantes")

class VisitantesDelete(LoginRequiredMixin, DeleteView):
    model = Visitantes
    success_url = reverse_lazy("visitantes")


#login/logout/registration

def loginRequest(request):
    if request.method == "POST":
        usuario= request.POST["username"]
        clave= request.POST["password"]                        

        user = authenticate(username=usuario, password=clave)
     
        if user is not None:
            login(request,user)
        
            try:
                avatar= Avatar.object.get(user=request.user.id).imagen.url #error
            except: 
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

        
            return render(request, "entidades/index.html", {"message": f"Bienvenido {user.username}"})
            ## return render(request, "entidades/index.html")
        else:
        
            return redirect(reverse_lazy('login'))
    else:
        form = AuthenticationForm()
        return render(request, "entidades/login.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():                             

            usuario = form.save()
            return render(request, "entidades/index.html", {"message": f"Usuario {usuario.username} creado con éxito!"})
        else:
            return render(request, "entidades/index.html", {"message": "Datos inválidos"})            
        
    else:
        form = RegistroForm()
        return render(request, "entidades/registro.html", {"form": form})


# Edicion

@login_required
def editProfile(request):
    usuario = request.user
    if request.merhod == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "entidades/editPerfil.html", {"from", miForm})



class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "entidades/cambiar_clave.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.merhod == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen= miForm.cleaned_data["imagen"]
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0 :
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            avatar= Avatar(user=usuario, imagen=imagen)
            avatar.save()
            imagen= Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm(instance=avatar)
    return render(request, "entidades/agregarAvatar.html", {"from", miForm})    

 ### Búsqueda de Profesores

def busqueda_profesion(req):
   return render(req, "entidades/busqueda_profesion.html", {})


def buscar(req):

  profesion = req.GET.get("profesion")  
  if profesion:
    
    profesores = Profesores.objects.filter(profesion__icontains=profesion)

    return render(req, "entidades/resultadoBusqueda.html", {"profesores": profesores, "profesion": profesion})
  else:      
      return render(req, "entidades/index.html", {"message": "No enviás el nombre del profesor"})

class ProfUpdate(UpdateView):    
    model = Profesores    
    template_name = 'entidades/profUpdate.html'
    fields= ('__all__')
    success_url = '/profesores/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profesor'] = self.object  # Asegura que el objeto profesor esté en el contexto
        return context
   
class ProfDelete(DeleteView):

  model = Profesores
  template_name = 'entidades/profDelete.html'
  fields= ('__all__')  
  success_url = '/profesores/'  # Redirige a la vista que lista los profesores  

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profesor'] = self.object  # Asegura que el objeto 
        return context
 
## Alumnos
@login_required
def alumnos(request):        
    
    if request.user.is_authenticated:
    
        contexto = {"alumnos":Alumno.objects.all()}
        return render(request,"entidades/alumnos.html", contexto)    
    else:
        return render(request,"entidades/login.html")    

@login_required
def alumno_form(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)

        if form.is_valid():
            a_nombre = form.cleaned_data.get("nombre")
            a_edad= form.cleaned_data.get("edad")
            a_email= form.cleaned_data.get("email")
            a_direccion= form.cleaned_data.get("direccion")
            alumno = Alumno(nombre=a_nombre, edad=a_edad, email=a_email, direccion=a_direccion)
            alumno.save()
            contexto = {"alumnos": Alumno.objects.all()}
            return render(request,"entidades/alumnos.html", contexto)
            ## return render(request, 'entidades/home.html', {"message":"Profesor creado con éxito"})
        else:
            return render(request, "entidades/home.html",{"message":"Datos incorrectos"})    
    else:
        form = AlumnoForm()
        return render(request, "entidades/alumnoForm.html", {"form": form})

class AlumnoUpdate(UpdateView):    
    model = Alumno
    template_name = 'entidades/alumnoUpdate.html'
    fields= ('__all__')
    success_url = '/alumnos/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alumno'] = self.object  # Asegura que el objeto profesor esté en el contexto
        return context


class AlumnoDelete(DeleteView):

  model = Alumno
  template_name = 'entidades/alumnoDelete.html'
  fields= ('__all__')  
  success_url = '/alumnos/'  # Redirige a la vista que lista los profesores  

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alumno'] = self.object  # Asegura que el objeto 
        return context



## Proveedores
@login_required
def proveedores(request):        
    
    if request.user.is_authenticated:
    
        contexto = {"proveedores":Proveedor.objects.all()}
        return render(request,"entidades/proveedores.html", contexto)    
    else:
        return render(request,"entidades/login.html")    

@login_required
def proveedor_form(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)

        if form.is_valid():
            p_nombre = form.cleaned_data.get("nombre")
            p_producto= form.cleaned_data.get("producto")
            p_email= form.cleaned_data.get("email")
            
            proveedor = Proveedor(nombre=p_nombre,producto=p_producto , email=p_email)
            proveedor.save()
            contexto = {"proveedores": Proveedor.objects.all()}
            return render(request,"entidades/proveedores.html", contexto)            
        else:
            return render(request, "entidades/home.html",{"message":"Datos incorrectos"})    
    else:
        form = ProveedorForm()
        return render(request, "entidades/proveedorForm.html", {"form": form})

class ProvUpdate(UpdateView):    
    model = Proveedor
    template_name = 'entidades/provUpdate.html'
    fields= ('__all__')
    success_url = '/proveedores/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proveedor'] = self.object  # Asegura que el objeto profesor esté en el contexto
        return context


class ProvDelete(DeleteView):

  model = Proveedor
  template_name = 'entidades/provDelete.html'
  fields= ('__all__')  
  success_url = '/proveedores/'  # Redirige a la vista que lista los profesores  

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proveedor'] = self.object  # Asegura que el objeto 
        return context
