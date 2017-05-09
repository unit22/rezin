from django.shortcuts import render
from .models import Category1, Category2, Category3


PROJECTNAME = "DaliExpress"


# Create your views here.
def index(request):
    categories1 = Category1.objects.all()
    categories2 = Category2.objects.all()
    categories3 = Category3.objects.all()
    #print(categoties1)
    return render(request, 'index.html',
                  {
        'page':'index',
        'categories1': categories1,
        'categories2': categories2,
        'categories3': categories3,
        'projectname':PROJECTNAME
                  }
                  )