#!coding:utf-8
from django.shortcuts import render_to_response, redirect, RequestContext, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import forms
from device.models import Device
from project.models import Project
import datetime, json

class ProjectForm(forms.ModelForm):
    class Meta:
	model = Project

@login_required(login_url='/login/')
def manage(request):
    if request.method == "POST" :
        pf = ProjectForm(request.POST)
        if pf.is_valid():
    	    name = pf.cleaned_data['name']
	    status = pf.cleaned_data['status']
    	    web	= pf.cleaned_data['web']
	    document = pf.cleaned_data['document']
            p = Project.objects.create(name=name, status=status, web=web, document=document)
    	    device = pf.cleaned_data['device']
    	    for entry in pf.cleaned_data['device']:
    	         p.device.add(entry)
    	    return HttpResponseRedirect("/project/list/")
    else:
	devices=Device.objects.all()
	proid = request.GET.get('id','')
	if proid:
	    pro_edit = Project.objects.get(id=proid)
	    dev_edit = pro_edit.device.all()
	    return render_to_response('edit_project.html', {'devices':devices, 'pro_edit':pro_edit, 'dev_edit':dev_edit}, context_instance=RequestContext(request))
	else:
	    pf=ProjectForm()
	    return render_to_response('manage_project.html',{'pf':pf,'devices':devices},context_instance=RequestContext(request))

@login_required(login_url='/login/')
def list(request):
    user = request.user
    search = request.GET.get('search', '')
    record = request.GET.get('record', 10)
    if search:
        project_list = Project.objects.order_by('name').filter(name__contains=search)
    else:
        project_list = Project.objects.order_by('name').all()
    paginator = Paginator(project_list, record)
    page_list = paginator.page_range
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    return render_to_response('list_project.html', {"projects": projects, "page_list":page_list, "search":search, "record":record}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def search(request):
    search = request.POST.get('search', 'noproject')
    projects = Project.objects.order_by('name').filter(name__icontains=search)
    return render_to_response('list_project.html', {'projects':projects}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def every(request, id):
    project = Project.objects.get(id=id)
    devices = project.device.all()
    return render_to_response('info_project.html', {'project':project, 'devices':devices}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def delete(request):
    proid = request.GET.get('proid')
    Project.objects.get(id=proid).delete()
    return HttpResponse(json.dumps("ok"))

@login_required(login_url='/login/')
def update(request):
    if request.method == "POST":
	id = request.POST.get('id','')
	name = request.POST.get('name','')
	status = request.POST.get('status','')
	web = request.POST.get('web','')
	document = request.POST.get('document','')
	devices = request.POST['devices']
	Project.objects.filter(id=id).update(name=name, status=status, web=web, document=document)
	p = Project.objects.get(id=id)
	p.device.clear()
	print request.POST
	print request.POST.get('devices')
        for entry in devices:
            p.device.add(entry)
        return HttpResponseRedirect('/project/list/' + id)
    else:
	return HttpResponseRedirect('/static/error/404.html') 
