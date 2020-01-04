from django.shortcuts import render,get_object_or_404
from Classifications.models import Technology_domain,Document_type
from Classifications.forms import TForm,DForm,TestForm
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def Tlist(request):
	tlist=Technology_domain.objects.all()
	return render(request,'Classifications/tdlist.html',{ 'tlist':tlist})

def create_technology_domain(request):
	form = TForm(request.POST or None )
	if form.is_valid():    
		instance= form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/td-list/')
		#instance.get_absolute_url())

	context={
		'form': form,
		'obj' : 'Subject Area'
	}
	return  render (request,"Classifications/add.html" , context)


# def technology_domain_detail(request,id=None):
# 	instance = get_object_or_404(Technology_domain,id=id)
# 	context ={
# 			'instance' : instance,

# 	}
# 	return  render (request,"Bank-details.html" , context)

def technology_delete(request,id=None):
	instance =get_object_or_404(Technology_domain,id=id)
	instance.delete()
	return HttpResponseRedirect('/td-list/')

#doc

def Dlist(request):
	dlist=Document_type.objects.all()
	return render(request,'Classifications/dlist.html',{'dlist': dlist })

def create_document_type(request):
	form = DForm(request.POST or None )
	if form.is_valid():    
		instance= form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/dt-list/')

	context={
		'form': form,
		'obj' : 'Document type'
	}
	return  render (request,"Classifications/add.html" , context)


# def document_type_detail(request,id=None):
# 	instance = get_object_or_404(Document_type,id=id)
# 	context ={
# 			'instance' : instance,

# 	}
# 	return  render (request,"Bank-details.html" , context)

def document_delete(request,id=None):
	instance =get_object_or_404(Document_type,id=id)
	instance.delete()
	return HttpResponseRedirect('/dt-list/')






def test(request):
	form = TestForm(request.POST or None )
	if form.is_valid():
		for key,value in request.FILES.items():
			print(key,value)
			# if key == 'q_attachments':
			# 	queryfiles=request.FILES.getlist(key)
			
			# if key == 'res_attachments':
			# 	responsefiles = request.FILES.getlist(key)

		return HttpResponseRedirect('/')
	context={
		'form': form,
	}
	return render(request,'testing.html',context)