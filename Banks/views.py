from django.shortcuts import render,get_object_or_404
from Banks.models import Bank
from Banks.forms import BankForm
from django.http import HttpResponse , HttpResponseRedirect
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()


def Bankslist(request):
	blist=Bank.objects.all()
	return render(request,'Bank/blist.html',{ 'blist':blist })


@login_required
def create_bank(request):
    form = BankForm(request.POST or None )
    if form.is_valid():
        form.cleaned_data['consultants']
        instance= form.save(commit=False)
        instance.save()

        consultantsQset=form.cleaned_data['consultants']
        for c in consultantsQset:       
            instance.consultants.add(c)
        instance.save()

        user = form.cleaned_data['spoc']
        user.is_spoc = True
        user.save()
        return HttpResponseRedirect('/banks-list')

    context={
        'form': form,
    }
    return  render (request,"Bank/add-bank.html" , context)



def bank_update(request,id=None):
    instance = get_object_or_404(Bank,id=id)
    oldspoc=instance.spoc
    form = BankForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        consultantsQset = form.cleaned_data['consultants']
        print(consultantsQset) 
        instance.consultants.clear()
        for c in consultantsQset:       
            instance.consultants.add(c)
        instance.save()
        l1=Bank.objects.filter(spoc=oldspoc)
        if len(l1) <= 0:
            oldspoc.is_spoc = False
            oldspoc.save()
        return HttpResponseRedirect('/banks-list')

    context ={
              'instance' : instance,
              'form':form ,
    }
    return  render (request,"Bank/add-bank.html" , context)


def bank_detail(request,id=None):
	instance = get_object_or_404(Bank,id=id)
	context ={
			'instance' : instance,

	}
	return  render (request,"Bank-details.html" , context)

def bank_delete(request,id=None):
	instance =get_object_or_404(Bank,id=id)
	instance.delete()
	return HttpResponseRedirect('/banks-list')



def make_active(request):
    if request.is_ajax():
        if request.method == 'POST':
            val=request.POST['id']
            bank=Bank.objects.get(pk=val)
            bank.is_active = True
            bank.save()
            message='Bank Activated'
            return HttpResponse(message)

        else:
            HttpResponse('only post method allowed')

    else:
        message = "Not ajax"
        return HttpResponse(message)


def make_inactive(request):
    if request.is_ajax():
        if request.method == 'POST':
            val=request.POST['id']
            bank=Bank.objects.get(pk=val)
            bank.is_active = False
            bank.save()
            message='Bank Inactivated'
            return HttpResponse(message)

        else:
            HttpResponse('only post method allowed')
    else:
        message = "Not ajax"
        return HttpResponse(message)


from django.shortcuts import render_to_response
from django.template import RequestContext


def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
