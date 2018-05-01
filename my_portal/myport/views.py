from django.shortcuts import render, HttpResponse
#from PATH_TO_ROOT_FOLDER.urllib3 import request,response
from PATH_TO_ROOT_FOLDER import requests
from django.views.generic import TemplateView
from django import forms
from myport.FunctionDtl import ProgRoute

# Create your views here.
def home(request):
    return render(request, 'myport/index.html')
def LHome(request):
    return render(request, 'myport/LanguageHome.html')
def AWSHome(request):
    return render(request, 'myport/AWSHome.html')
def Stree(request):
    return render(request, 'myport/StudyTree.html')
def LPython3(request):
    return render(request, 'myport/Lpython3.html')
class LangProc(TemplateView):
    template_name = 'myport/Lpython3.html'
    printtxt = ProgRoute()
    def get(self,request):

        return render(request,self.template_name)

    def post(self,request):
         text1 = request.POST['EnterCode']
         self.printtxt.FuncBridge(text1)
         return render(request,self.template_name)
