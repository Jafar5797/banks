from django.shortcuts import render,get_object_or_404
from suggestions.models import Suggestion
from suggestions.forms import SForm
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def suggestionslist(request):
	slist=Suggestion.objects.all()
	return render(request,'suggestions/slist.html',{ 'slist':slist })


@login_required
def create_suggestion(request):
    form = SForm(request.POST or None )
    if form.is_valid():
        instance= form.save(commit=False)
        instance.name=request.user.name
        instance.save()
        return HttpResponseRedirect('/')

    context={
        'form': form,
    }
    return  render (request,"suggestions/add.html" , context)

