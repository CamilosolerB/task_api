from django.shortcuts import render, redirect
from .models import user_model, task_model
from django.contrib import messages
from django.http import JsonResponse

def login_page(request):
    return render(request, 'index.html')

def sing_up_page(request):
    return render(request, 'singUp.html')

def home_page(request):
    if request.method == 'POST':
        post = request.POST
        user = user_model.objects.get(username=post.get('email'), password=post.get('password'))
        if user is not None:
            request.session['id_user'] = user.id
            messages.success(request, '¡Inicio de sesión exitoso!')
            return redirect('home')
        else:
            messages.error(request, 'Correo electrónico o contraseña incorrectos.')
            return redirect('/')
    return render(request, 'home.html')

def create_user(request):
    if request.method == 'POST':
        post = request.POST
        email = post.get('email')
        password = post.get('password')
        if user_model.objects.filter(username=email).exists():
            messages.error(request, 'El correo electrónico ya está en uso.')
            return redirect('signup')
        user = user_model.objects.create(username=email, password=password)
        request.session['id_user'] = user.id
        return redirect('home')
    else:
        return redirect('signup')
    
def create_note(request):
    if request.method == 'POST':
        post = request.POST
        title = post.get('title')
        description = post.get('description')
        date = post.get('date')
        user_id = request.session.get('id_user')
        user = user_model.objects.get(id=user_id)
        note = task_model.objects.create(title=title, description=description, date=date, user = user)
        return redirect('home')
    else:
        return redirect('home')
    
def sing_out(request):
    request.session['id_user'] = ''
    return redirect('/')

def home_view(request):
    user_id = request.session.get('id_user')
    notes = task_model.objects.filter(user=user_id).values()
    return render(request, 'home.html', {'session': user_id, 'notes': notes})

def delete_task(request, task_id):
    try:
        nota = task_model.objects.get(taks_id=task_id)
        nota.delete()
        return JsonResponse({'mensaje': 'Nota eliminada correctamente.'})
    except task_model.DoesNotExist:
        return JsonResponse({'error': 'La nota no existe.'}, status=404)
    
def update_view(request, task_id):
    nota = task_model.objects.get(taks_id=task_id)
    return render(request, 'update.html', {'note': nota})

def update_task(request):
    if request.method == 'POST':
        id = request.POST.get('task_id')
        nota = task_model.objects.get(taks_id = id) 
        nota.title = request.POST.get('title')
        nota.description = request.POST.get('description')
        nota.date = request.POST.get('date')
        nota.save()
        return redirect('home')
    else:
        return redirect('home')
