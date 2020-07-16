# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# def hello(request):
#     my_dic = {'insert_me':"HELLO WORD"}
#     return render(request,'appone/rk.html',context=my_dic)
#
#
# # views.py
# from django.shortcuts import render, redirect
#
# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponse, HttpResponseNotFound
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound


def pdf_view(request):
    fs = FileSystemStorage()
    filename = 'RK_Resume.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"' #user will be prompted with the browser’s open/save file
            response[
                'Content-Disposition'] = 'inline; filename="RK_Resume.pdf"'  # user will be prompted display the PDF in the browser
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')