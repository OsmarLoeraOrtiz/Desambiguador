from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def principal(request):
    if request.method == "POST":
        pass
    else:
        return render(request, 'index.html')
def registro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validaciones básicas
        if password != confirm_password:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'registro.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return render(request, 'registro.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está registrado.")
            return render(request, 'registro.html')

        # Crear el usuario
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Tu cuenta ha sido creada con éxito. ¡Ya puedes ingresar!")
        return redirect('ingreso')
    
    return render(request, 'registro.html')

def ingreso(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('proyectos')  # Redirige a la página de inicio
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
            return render(request, 'ingreso.html')
    
    return render(request, 'ingreso.html')
    
def configuracion(request):
    if request.method == 'POST':
        pass
    else:
        return render(request,'configuracion.html')

def salir(request):
    logout(request)
    return redirect('home')  
