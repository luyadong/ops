#!coding:utf-8
from django.shortcuts import render_to_response, redirect, RequestContext, render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from device.models import Device
import datetime

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device

def manage(request):
    user = request.user
    if user.is_authenticated():
        if request.method == "POST" :
            df = DeviceForm(request.POST)
	    if df.is_valid():
		nei_ip		= df.cleaned_data['nei_ip']
		wai_ip		= df.cleaned_data['wai_ip']
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
		status		= df.cleaned_data['status']
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
	    years = [i for i in range(1990,2050)]
	    months = [i for i in range(1,13)]
	    days = [i for i in range(1,32)]
	    df=DeviceForm()
	    return render_to_response('manage_device.html',{'df':df, 'years':years, 'months':months, 'days':days},context_instance=RequestContext(request))
    else:
	return HttpResponseRedirect("/login/")

def list(request):
    user = request.user
    if user.is_authenticated():
	devices = Device.objects.order_by('nei_ip').all()
        return render_to_response('list_device.html', {'devices':devices}, context_instance=RequestContext(request))
    else:
	return HttpResponseRedirect("/login/")

def search(request):
    user = request.user
    if user.is_authenticated():
	if request.method == "POST":
	    search = request.POST.get('search', 'NONE')
	    devices = Device.objects.order_by('nei_ip').filter(nei_ip__icontains=search)
	    return render_to_response('list_device.html', {'devices':devices}, context_instance=RequestContext(request))
    else:
	return HttpResponseRedirect("/login/")

def every(request,nei_ip):
    user = request.user
    if user.is_authenticated():
        device = Device.objects.get(nei_ip=nei_ip.strip())
	return render_to_response('info_device.html', {'device':device}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/login/")
