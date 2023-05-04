from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm
# Create your views here.




# Create your views here.
def PersonaList(request):  
    Personas = Persona.objects.all()  
    return render(request,"listaPersonas.html",{'personas':Personas})  

def CrearPersona(request):  
    if request.method == "POST":  
        form = PersonaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('listaPersonas')  
            except:  
                pass  
    else:  
        form = PersonaForm()  
    return render(request,'crearPersona.html',{'form':form})  

def ActualizarPersona(request, id):  
    persona = Persona.objects.get(id=id)
    form = PersonaForm(initial={'rut': Persona.rut, 'nombre': Persona.nombre, 'apellido': Persona.apellido})
    if request.method == "POST":  
        form = PersonaForm(request.POST, instance=Persona)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/listaPersonas')  
            except Exception as e: 
                pass    
    return render(request,'modifPersona.html',{'form':form})  

def EliminarPersona(request, id):
    persona = Persona.objects.get(id=id)
    try:
        Persona.delete()
    except:
        pass
    return redirect('listaPersonas')