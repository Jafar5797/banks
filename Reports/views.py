from django.shortcuts import render,get_object_or_404
from Reports.models import Report,Q_Report,QueryFiles,ResponseFiles
from Reports.forms import CreateReportForm,QFull_ReportForm,SearchForm,TopicForm,ConsultantForm,QA_Formset,AttachmentsFormset,AttachmentsForm,SubDocForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User = get_user_model()
import datetime


@login_required
def FilterDetails(request):
    if request.is_ajax():
        if request.method == 'POST':
            val=request.POST['id']

            return HttpResponse(message)

        else:
            HttpResponse('only post method allowed')
    else:
        message = "Not ajax"
        return HttpResponse(message)
@login_required
def QFull_Summary_Generate(request):
	if request.method=='POST':
		form=QFull_ReportForm(request.POST or None,user=request.user)
		if form.is_valid():
			report=Q_Report()
			spoc=User.objects.get(name=request.user)
			consultantsQset=form.cleaned_data['consultants']
			From=form.cleaned_data['From']
			To=form.cleaned_data['To']
			bankname=form.cleaned_data['bankname']
			print(bankname)
			requests_recieved=form.cleaned_data['requests_recieved']
			summary_of_response=form.cleaned_data['summary_of_response']
			summary_of_workdone=form.cleaned_data['summary_of_workdone']
			learnings=form.cleaned_data['learnings']
			print('summary_of_response : ',summary_of_response)
			report.spoc=spoc
			report.bankname=bankname.name
			report.fromdate=From
			report.todate=To
			report.requests_recieved=requests_recieved
			report.summary_of_response=summary_of_response
			report.summary_of_workdone=summary_of_workdone
			report.learnings=learnings
			report.save()
			for c in consultantsQset:
				print(type(c))
				report.consultants.add(c)
			report.consultants.add(spoc)
			report.save()
			return HttpResponseRedirect(report.get_absolute_url())
		
	else:
		form=QFull_ReportForm(user=request.user)
	return render(request,"Report/summary_index.html",{"form":form})


@login_required
def Q_ReportDetails(request,id):
	qlist=Q_Report.objects.get(id=id)
	return render(request,'Report/qrdetails.html',{ 'qlist':qlist })



@login_required
def create_report(request):
	if request.method=='POST':

		form=CreateReportForm(request.POST or None,request.FILES,user=request.user)
		# for key,item in request.FILES.items():
		# 	print(key,item)
		if form.is_valid():
			report=Report()
			spoc=User.objects.get(name=request.user)
			consultantsQset=form.cleaned_data['consultants']
			date=form.cleaned_data['date']
			bankname=form.cleaned_data['bankname']
			topic=form.cleaned_data['topic']
			query=form.cleaned_data['query']
			response=form.cleaned_data['response']
			technology_domain=form.cleaned_data['technology_domain']
			document_type=form.cleaned_data['document_type']
			q_attachments=form.cleaned_data['q_attachments']
			res_attachments=form.cleaned_data['res_attachments']

			report.spoc=spoc
			report.date=date
			report.bankname=bankname.name
			report.topic=topic
			report.query=query
			report.response=response
			report.technology_domain = technology_domain.name
			report.document_type=document_type.name
			report.save()

			responsefiles=queryfiles=[]

			for key,value in request.FILES.items():
				if key == 'q_attachments':
					queryfiles=request.FILES.getlist(key)
				
				if key == 'res_attachments':
					responsefiles = request.FILES.getlist(key)


			for qf in queryfiles:
				QueryFiles.objects.create(report=report,file=qf)
			report.save()

			for rf in responsefiles:
				ResponseFiles.objects.create(report=report,file=rf)
			report.save()
			report.consultants.add(spoc)
			for c in consultantsQset:
				print(type(c))
				report.consultants.add(c)
			report.save()
			return HttpResponseRedirect('/')

	else:
		print(request.user,request.user.email,)
		form=CreateReportForm(user=request.user)
	return render(request,"Report/create-report.html",{"form":form})

@login_required
def SearchFormView(request):
	if request.method=='POST':
		form=SearchForm(request.POST or None)
		if form.is_valid():
			bankname=form.cleaned_data.get('bankname')
			From=form.cleaned_data.get('From')
			To=form.cleaned_data.get('To')
			print(bankname,To,From)
			Fromdate=str(From).split("-")
			Todate=str(To).split("-")
			first_date = datetime.date(int(Fromdate[0]),int(Fromdate[1]),int(Fromdate[2]))
			last_date = datetime.date(int(Todate[0]),int(Todate[1]),int(Todate[2]))
			results = Report.objects.filter(date__range=(first_date, last_date),bankname=bankname)
			print(results)
			if request.user.is_consultant:
				return render(request,'Report/results.html',{'results':results })
			else:
				return render(request,'Report/resultsAdmin.html',{'results':results })
	else:
		form=SearchForm()

	if request.user.is_consultant:
		return render(request,"Report/search.html",{"form":form})
	else:
		return render(request,'Report/Adminsearch.html'	,{"form":form}	)
	




@login_required
def myActivitiesView(request):
	me=request.user
	print(me)
	vlist=Report.objects.filter(consultants__in=[me,])
	qlist=Q_Report.objects.filter(consultants__in=[me,])
	print(vlist)
	return render(request, 'Report/activity.html',{ 'vlist': vlist,'qlist':qlist })


@login_required
def FilterTopicDetails(request):
	val='Topic'
	if request.method=='POST':
		form=TopicForm(request.POST or None)
		if form.is_valid():
			topic=form.cleaned_data.get('topic')
			print(topic)
			results = Report.objects.filter(topic__icontains=topic)
			print(results)
			if request.user.is_consultant:
				return render(request,'Report/topicresults.html',{'results':results,'obj': val })
			else:
				return render(request,'Report/topicAdmin.html',{'results':results,'obj': val })
	else:
		form=TopicForm()

	if request.user.is_consultant:
		return render(request,"Report/topicsearch.html",{"form":form,'obj': val })
	else:
		return render(request,'Report/admintopicsearch.html',{"form":form,'obj': val}	)

@login_required
def FilterByConsultant(request):
	if request.method=='POST':
		form=ConsultantForm(request.POST or None)
		if form.is_valid():
			val=form.cleaned_data['consultant']
			vlist=Report.objects.filter(consultants__in=[val,])
			qlist=Q_Report.objects.filter(consultants__in=[val,])
			return render(request, 'Report/AdminActivity.html',{ 'vlist': vlist,'qlist':qlist })

	else:
		form=ConsultantForm()
	return render(request,'Report/AdminConSearch.html',{ 'form':form })
	


@login_required
def Activities(request):
	vlist=Report.objects.all()
	qlist=Q_Report.objects.all()
	return render(request, 'Report/AdminActivity.html',{ 'vlist': vlist,'qlist':qlist })



@login_required
def FilterBySubjectDocType(request):
	val='Subject Area & Document Type'
	if request.method=='POST':
		form=SubDocForm(request.POST or None)
		if form.is_valid():
			technology_domain=form.cleaned_data.get('technology_domain').name
			document_type=form.cleaned_data.get('document_type').name
			results = Report.objects.filter(technology_domain__icontains=technology_domain
				,document_type__icontains=document_type)
			print(results)
			if request.user.is_consultant:
				return render(request,'Report/topicresults.html',{'results':results,'obj': val})
			else:
				return render(request,'Report/topicAdmin.html',{'results':results,'obj': val })
	else:
		form=SubDocForm()
	if request.user.is_consultant:
		return render(request,"Report/topicsearch.html",{"form":form,'obj': val })
	else:
		return render(request,'Report/admintopicsearch.html',{"form":form,'obj': val }	)







@login_required
def FilterTopicByMe(request):
	val='Topic'
	if request.method=='POST':
		form=TopicForm(request.POST or None)
		if form.is_valid():
			me=request.user
			topic=form.cleaned_data['topic']
			results = Report.objects.filter(topic__icontains=topic,consultants__in=[me,])
			print(results)
			return render(request,'Report/topicresults.html',{'results':results,'obj': val })
	else:
		form=TopicForm()
	return render(request,"Report/topicsearch.html",{"form":form,'obj': val })



@login_required
def FilterBySubjectDocTypeByMe(request):
	val='Subject Area & Document Type'
	if request.method=='POST':
		form=SubDocForm(request.POST or None)
		if form.is_valid():
			me=request.user
			technology_domain=form.cleaned_data.get('technology_domain').name
			document_type=form.cleaned_data.get('document_type').name
			results = Report.objects.filter(technology_domain__icontains=technology_domain
				,document_type__icontains=document_type,consultants__in=[me,])
			return render(request,'Report/topicresults.html',{'results':results,'obj': val})
	else:
		form=SubDocForm()
	return render(request,"Report/topicsearch.html",{"form":form,'obj': val })



@login_required
def SearchFormViewByMe(request):
	if request.method=='POST':
		form=SearchForm(request.POST or None)
		if form.is_valid():
			me=request.user
			bankname=form.cleaned_data.get('bankname')
			From=form.cleaned_data.get('From')
			To=form.cleaned_data.get('To')
			Fromdate=str(From).split("-")
			Todate=str(To).split("-")
			first_date = datetime.date(int(Fromdate[0]),int(Fromdate[1]),int(Fromdate[2]))
			last_date = datetime.date(int(Todate[0]),int(Todate[1]),int(Todate[2]))
			results = Report.objects.filter(date__range=(first_date, last_date),
				bankname=bankname,consultants__in=[me,])
			print(results)
			return render(request,'Report/results.html',{'results':results })
	else:
		form=SearchForm()

	return render(request,"Report/search.html",{"form":form})


@login_required
def QReportList(request):
	val='Quaterly Report'
	results=Q_Report.objects.all()
	return render(request,'Report/qrlist.html',{'results':results,'obj': val })

	