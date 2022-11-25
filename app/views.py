from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'Ashu','age':2}
    return render(request,'jinja_print.html',d)