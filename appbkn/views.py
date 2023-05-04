from django.shortcuts import render, redirect
from .models import persona
from .forms import PersonaForm
# Create your views here.




# Create your views here.
def PersonaList(request):  
    Personas = persona.objects.all()  
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
    return render(request,'persona-create.html',{'form':form})  

def ActualizarPersona(request, id):  
    persona = persona.objects.get(id=id)
    form = PersonaForm(initial={'rut': persona.rut, 'nombre': persona.nombre, 'apellido': persona.apellido})
    if request.method == "POST":  
        form = PersonaForm(request.POST, instance=persona)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/listaPersonas')  
            except Exception as e: 
                pass    
    return render(request,'persona-update.html',{'form':form})  

def EliminarPersona(request, id):
    persona = persona.objects.get(id=id)
    try:
        persona.delete()
    except:
        pass
    return redirect('listaPersonas')