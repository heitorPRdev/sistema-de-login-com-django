from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        passaword = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Já existe um usuario com esse username')
        user = User.objects.create_user(username=username,password=passaword)
        user.save()
        return  redirect('login')
    
def loginP(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        passaword = request.POST.get('password')
        user = authenticate(username=username)
        if user:
            login(request,user)
            return HttpResponse('Já existe um usuario com esse username')
        
        return redirect('sucesso')

def sucesso(request):
    if request.user.is_authenticated:
        return render(request,'sucesso.html')
    return render(request,'sucesso.html', {'erro':'você precisa estar logado'})
def home(request):
    return render(request,'home.html')