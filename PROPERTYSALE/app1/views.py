from django.shortcuts import render

from .models import Appartment
from .models import NewPlot

def loginPage(request):
    return render(request,"index.html")


def loginCheck(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    if username == "admin" and password == "admin":
        return render(request,"one.html",{"welcome":"welocome to admin"})
    else:
        return render(request,"index.html",{"message":"username and password wrong"})


def plotregistration(request):
    return render(request,"one.html",{"message":"registration page"})


def plotSave(request):
    plotno=request.POST.get("number")
    roadno=request.POST.get("roadno")
    surveyno = request.POST.get("surno")
    squareno = request.POST.get("sqyno")
    otherex = request.POST.get("oexpno")
    boundary = request.POST.get("bouno")
    direction = request.POST.get("directions")
    status = request.POST.get("status")
    amount = request.POST.get("amount")
    savedata=NewPlot(plotno=plotno,roadnumber=roadno,surveyno=surveyno,costsqare=squareno,
            otherexpences=otherex,boundaries=boundary,facing=direction,status=status,
            totalcost=amount)
    savedata.save()
    return render(request,"one.html",{"saved":"sucessfull"})


def logouts(request):
    return loginPage(request)


def detailplot(request):
    return render(request,"one.html",{"viewplot":"viewplot details"})


def viewOneDetail(request):
    plot=request.POST.get("plotno")
    try:
        plotdata=NewPlot.objects.get(plotno=plot)
        return render(request,"one.html",{"details":plotdata})
    except:
        return render(request,"one.html",{"errordetails":"plot no is not available"})


def plotedit(request):

    return render(request,"one.html",{"editplot":"editdetails"})


def editemployee(request):
    plots=request.POST.get("editnumber")
    try:
        editdata=NewPlot.objects.get(plotno=plots)
        return render(request,"one.html",{"plotedit":editdata})
    except:
         return render(request,"one.html",{"editedplot":"plot is not edited","data":plots})


def saveEditPlot(request):
    epno=request.POST.get("number")
    eroad=request.POST["roadno"]
    esurno=request.POST["surno"]
    esqyno=request.POST["sqyno"]
    eoexpno=request.POST["oexpno"]
    ebouno=request.POST["bouno"]
    edirections=request.POST["directions"]
    estatus=request.POST["status"]
    eamount=request.POST["amount"]
    NewPlot(plotno=epno,roadnumber=eroad,surveyno=esurno,costsqare=esqyno,
            otherexpences=eoexpno,boundaries=ebouno,facing=edirections,status=estatus,
            totalcost=eamount).save()
    return render(request,"one.html",{"editsaved":"edited values saved successfully"})


def bookappartment(request):
    return render(request,"one.html",{"appartment":"app"})


def regappartment(request):
    apn=request.POST["apname"]
    apno=request.POST["apno"]
    nof=request.POST["numberofflats"]
    pac=request.POST["platcost"]
    vac=request.POST["vacancies"]
    Appartment(apartname=apn,apartno=apno,noofplats=nof,costofplat=pac,
               noofvacant=vac).save()
    return render(request,"one.html",{"appmessage":"successfully register details"})


def apartmentview(request):
    return render(request,"one.html",{"appview":"viewapp"})


def appdetailsshow(request):
    vappno=request.POST.get("appno")
    try:
        res=Appartment.objects.get(apartno=vappno)
        return render(request,"one.html",{"vappno":res})
    except:
        return render(request,"one.html",{"errorvappno":"appartment is not available"})


def eeditapartment(request):
    res=Appartment.objects.all()
    return render(request,"one.html",{"edit":res})


def editdetails(request):
    noedit=request.POST.get("editno")
    try:
       res1=Appartment.objects.get(apartno=noedit)
       return render(request,"one.html",{"detailedit":res1})
    except:
        return render(request,"one.html",{"merror":"invalid edit"})


def editingdata(request):
    eapname=request.POST["apname"]
    eapno=request.POST["apno"]
    eflats=request.POST["numberofflats"]
    eplatcost=request.POST["platcost"]
    evacancies=request.POST["vacancies"]
    Appartment(apartname=eapname,apartno=eapno,noofplats=eflats,
               costofplat=eplatcost,noofvacant=evacancies).save()
    return render(request,"one.html",{"successedit":"appartment data edit successfully"})


def aboutdetail(request):
    return render(request,"one.html",{"detailsabout":"detail"})


def homePage(request):
    return render(request,"one.html",{"welcome":"welcome to admin"})
