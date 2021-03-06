#!coding:utf-8
from django.shortcuts import render_to_response, redirect, RequestContext, render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from device.models import Device
from project.models import Project
import datetime

class ProjectForm(forms.ModelForm):
    class Meta:
	model = Project

def manage(request):
    user = request.user
    if user.is_authenticated():
        if request.method == "POST" :
            pf = ProjectForm(request.POST)
	    if pf.is_valid():
		name	 = pf.cleaned_data['name']
		web	 = pf.cleaned_data['web']
		document = pf.cleaned_data['document']
                p = Project.objects.create(name=name, web=web, document=document)

		device   = pf.cleaned_data['device']
		for entry in pf.cleaned_data['device']:
		    p.device.add(entry)
		return HttpResponseRedirect("/project/list/")
	else:
	    devices=Device.objects.all()
	    pf=ProjectForm()
	    return render_to_response('manage_project.html',{'pf':pf,'devices':devices},context_instance=RequestContext(request))
    else:
	return HttpResponseRedirect("/login/")

def list(request):
    user = request.user
    if user.is_authenticated():
	projects = Project.objects.order_by('name').all()
        return render_to_response('list_project.html', {'projects':projects}, context_instance=RequestContext(request))
    else:
	return HttpResponseRedirect("/login/")

def search(request):
    user = request.user
    if user.is_authenticated():
	search = request.POST.get('search', 'noproject')
	projects = Project.objects.order_by('name').filter(name__icontains=search)
        return render_to_response('list_project.html', {'projects':projects}, context_instance=RequestContext(request))
    else:
	return HttpResponseRedirect("/login/")

def every(request, proname):
    user = request.user
    if user.is_authenticated():
	project = Project.objects.get(name=proname)
	devices = project.device.all()
	return render_to_response('info_project.html', {'project':project, 'devices':devices}, context_instance=RequestContext(request))
    else:
	return HttpResponseRedirect('/login/')
