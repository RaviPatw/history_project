from django.shortcuts import render
from document.models import Document
# Create your views here.
def index(request):
    return render(request,'index.html')
def unit_page(request, unit_id):
    documents=Document.objects.filter(unit=unit_id)
    context={
        'documents':documents,
        'unit_id':unit_id
        
    }
    return render(request, 'unit.html',context)
def themes(request):
    return render(request,'themes.html')