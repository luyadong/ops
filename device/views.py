#!coding:utf-8
from django.shortcuts import render_to_response, redirect, RequestContext, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import forms
from device.models import Device
import datetime, json

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device

#    def clean_nei_ip(self):
#	nei_ip = self.cleaned_data["nei_ip"]
#	if Device.objects.filter(nei_ip = nei_ip.strip()):
#	    raise forms.ValidationError("nei_ip repeat!!")

@login_required(login_url='/login/')
def manage(request):
    user = request.user
    if request.method == "POST" :
        df = DeviceForm(request.POST)
        if df.is_valid():
	    nei_ip	    = df.cleaned_data['nei_ip']
    	    wai_ip	    = df.cleaned_data['wai_ip']
    	    hostname        = df.cleaned_data['hostname']
    	    serial_number   = df.cleaned_data['serial_number']
    	    buy_date        = df.cleaned_data['buy_date']
    	    inventar_Nummer = df.cleaned_data['inventar_Nummer']
    	    manufacturer    = df.cleaned_data['manufacturer']
    	    type            = df.cleaned_data['type']
    	    monitor         = df.cleaned_data['monitor']
    	    location        = df.cleaned_data['location']
    	    principal       = df.cleaned_data['principal']
    	    administrator   = df.cleaned_data['administrator']
    	    purpose         = df.cleaned_data['purpose']
    	    status	    = df.cleaned_data['status']
    	    remarks         = df.cleaned_data['remarks']
    	    os              = df.cleaned_data['os']
    	    partion         = df.cleaned_data['partion']
    	    cpu             = df.cleaned_data['cpu']
    	    memory          = df.cleaned_data['memory']
    	    disk            = df.cleaned_data['disk']
    	    disk_controller = df.cleaned_data['disk_controller']
    	    protocol        = df.cleaned_data['protocol']
    	    port            = df.cleaned_data['port']
    	    username        = df.cleaned_data['username']
    	    password        = df.cleaned_data['password']
            Device.objects.create(nei_ip=nei_ip, wai_ip=wai_ip, hostname=hostname, serial_number=serial_number, buy_date=buy_date, inventar_Nummer=inventar_Nummer, manufacturer=manufacturer, type=type, monitor=monitor, location=location, principal=principal, administrator=administrator, purpose=purpose, status=status, remarks=remarks, os=os, partion=partion, cpu=cpu, memory=memory, disk=disk, disk_controller=disk_controller, protocol=protocol, port=port, username=username, password=password)
    	return HttpResponseRedirect("/device/list/")
    else:
	devid = request.GET.get('id','')
	if devid:
	    dev_edit = Device.objects.get(id=devid)
	    print dev_edit
	    return render_to_response('edit_device.html',{'dev_edit':dev_edit},context_instance=RequestContext(request))
	else:
	    df=DeviceForm()
	    return render_to_response('manage_device.html',{'df':df},context_instance=RequestContext(request))

@login_required(login_url='/login/')
def list(request):
    user = request.user
    search = request.GET.get('search', '')
    record = request.GET.get('record','10')
    if search:
	device_list = Device.objects.order_by('nei_ip').filter(nei_ip__icontains=search)
    else:
	device_list = Device.objects.order_by('nei_ip').all()
    paginator = Paginator(device_list, record)
    page_list = paginator.page_range
    page = request.GET.get('page')
    try:
        devices = paginator.page(page)
    except PageNotAnInteger:
        devices = paginator.page(1)
    except EmptyPage:
        devices = paginator.page(paginator.num_pages)
    
    return render_to_response('list_device.html', {"devices": devices, "page_list":page_list, "search":search, "record":record}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def every(request,id):
    user = request.user
    device = Device.objects.get(id=id)
    projects = device.project_set.all()
    return render_to_response('info_device.html', {'device':device, 'projects':projects}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def delete(request):
    user = request.user
    devid = request.GET.get('devid')
    Device.objects.get(id=devid).delete()
    return HttpResponse(json.dumps('ok'))


@login_required(login_url='/login/')
def update(request):
    user = request.user
    if request.method == "POST":
	id = request.POST.get('id')
        nei_ip = request.POST.get('nei_ip','')
        wai_ip = request.POST.get('wai_ip','')
        hostname = request.POST.get('hostname','')
        serial_number = request.POST.get('serial_number','')
        buy_date = request.POST.get('buy_date','')
        inventar_Nummer = request.POST.get('inventar_Nummer','')
        manufacturer = request.POST.get('manufacturer','')
        type = request.POST.get('type','')
        monitor = request.POST.get('monitor','')
        location = request.POST.get('location','')
        principal = request.POST.get('principal','')
        administrator = request.POST.get('administrator','')
        purpose = request.POST.get('purpose','')
        status = request.POST.get('status','')
        remarks = request.POST.get('remarks','')
        os = request.POST.get('os','')
        partion = request.POST.get('partion','')
        cpu = request.POST.get('cpu','')
        memory = request.POST.get('memory','')
        disk = request.POST.get('disk','')
        disk_controller = request.POST.get('disk_controller','')
        protocol = request.POST.get('protocol','')
        port = request.POST.get('port','')
        username = request.POST.get('username','')
        password = request.POST.get('password','')
	Device.objects.filter(id=id).update(nei_ip=nei_ip, wai_ip=wai_ip, hostname=hostname, serial_number=serial_number, buy_date=buy_date, inventar_Nummer=inventar_Nummer, manufacturer=manufacturer, type=type, monitor=monitor, location=location, principal=principal, administrator=administrator, purpose=purpose, status=status, remarks=remarks, os=os, partion=partion, cpu=cpu, memory=memory, disk=disk, disk_controller=disk_controller, protocol=protocol, port=port, username=username, password=password)
	return HttpResponseRedirect('/device/list/' + id)
    else:
	return HttpResponseRedirect('/static/error/404.html')
