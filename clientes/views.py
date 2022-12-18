from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

# Create your views here.
def redirecttoClientes(request):
    return redirect('clientes')

def listarClientes(request):  
    clientes = Cliente.objects.all()  
    return render(request,"index.html",{'clientes':clientes})  

def crearCliente(request):  
    if request.method == "POST":  
        form = ClienteForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('clientes')  
            except:  
                pass  
    else:  
        form = ClienteForm()
    return render(request,'crear.html',{'form':form})  

def actualizarCliente(request, id):  
    cliente = Cliente.objects.get(id=id)
    if request.method == "POST":  
        form = ClienteForm(request.POST, instance=cliente)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/clientes')  
            except Exception as e: 
                pass    
    return render(request,'actualizar.html',{'cliente':cliente})  

def verCliente(request, id):  
    cliente = Cliente.objects.get(id=id)
    return render(request,'detalles.html',{'cliente':cliente})  

def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    try:
        cliente.delete()
    except:
        pass
    return redirect('/clientes')