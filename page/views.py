from django.shortcuts import render
from django.http import HttpResponse
from random import randint

def home(request):
    #print("merhaba: ",request)
    #return HttpResponse("Ana sayfaya hoş geldiniz 2022")
	context={"platform":f"Django patformu kullanıldı ve Randint ile dönen veri : {randint(1,100)}"}
	return render(request,'page/home_page.html',context)


