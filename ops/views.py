#!coding:utf-8
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django import forms

class LF(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码',widget=forms.PasswordInput)

def index(request):
    user = request.user
    if user.is_authenticated():
        return render_to_response('index.html', context_instance=RequestContext(request))
    else:
	return HttpResponseRedirect('/login/')

def user_login(request):
    if request.method == "POST":
	lf=LF(request.POST)
	if lf.is_valid():
	    username = lf.cleaned_data['username']
	    password = lf.cleaned_data['password']
	    user = authenticate(username=username, password=password)
	    if user is not None:
		login(request, user)
		return HttpResponseRedirect('/')
    else:
	lf=LF()
    return render_to_response('login.html', {'lf':lf})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
