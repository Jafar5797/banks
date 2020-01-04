from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.admin.views.decorators import staff_member_required
#from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
# settings.AUTH_USER_MODEL
# #User = get_user_model()
from django.contrib.auth import get_user_model
User = get_user_model()

@login_required
def index(request):
    if request.user.is_first_time: 
        return redirect('/user/change-password/')
    if request.user.is_superuser:
    	val=request.user
    	return render(request,'index.html')
    else:
    	return render(request,'userindex.html')


def consultant_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_first_time=False
            user.is_consultant = True
            user.save()
            return HttpResponseRedirect('/')

    else:
        form = UserRegisterForm()
    return render(request,'registration/register.html',{'form':form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_first_time=False
            user.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    if request.user.is_first_time:
        return render(request, 'registration/changepwd.html',{ 'form': form })

    if request.user.is_superuser:
        return render(request, 'registration/change_password.html',{ 'form': form })
    else:
        return render(request, 'registration/user_change_password.html',{ 'form': form })

def user_settings(request):
	return render(request,'users/settings.html')

def user_delete(request,pk=None):
    instance =get_object_or_404(User,pk=pk)
    instance.delete()
    return HttpResponseRedirect('/consultant-list')


@login_required
def list_of_users(request):
	slist = User.objects.filter(is_consultant=True)
    
	#print(type(slist),slist.values())

	return render(request,'registration/slist.html',{'slist':slist })
@login_required
def list_of_consultants(request):
	clist = User.objects.filter(is_consultant = True)
	return render(request,'registration/clist.html',{'clist':clist })



def make_as_spoc(request):
    if request.is_ajax():
        if request.method == 'POST':
            val=request.POST['id']
            user = User.objects.get(pk=val)
            user.is_spoc = True
            user.save()
            message='Added as Spoc'
            return HttpResponse(message)

        else:
            HttpResponse('only post method allowed')

    else:
        message = "Not ajax"
        return HttpResponse(message)


def remove_as_spoc(request):
    if request.is_ajax():
        if request.method == 'POST':
            val=request.POST['id']
            user = User.objects.get(pk=val)
            user.is_spoc = False
            user.save()
            message = "Removed as Spoc"
            return HttpResponse(message)

        else:
            HttpResponse('only post method allowed')
    else:
        message = "Not ajax"
        return HttpResponse(message)









