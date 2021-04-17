from django.shortcuts import render, HttpResponse, redirect
import pymongo
import re

# Create your views here.
def index(request):
    return render(request,"index.html")

def grants(request):
    return render(request,"grants.html")

def case_studies(request):
    return render(request,"case_studies.html")

def view_grant(request):
    if request.method == "POST":
        fund_title=request.POST.get('fund_title')

        myclient = pymongo.MongoClient("mongodb+srv://admin-parag:test123@cluster0.gq3uj.mongodb.net/test")
        mydb = myclient['scrap_data']
        mycol = mydb["grants"]

        result = mycol.find({'fund_title': re.compile(fund_title, re.IGNORECASE)})

        if result.count()==0:
            return render(request,"no_grant.html")
        data = dict({'results': result})

        return render(request,"view_grant.html",data)
    return render(request,"404.html")

def view_case_study(request):
    if request.method == "POST":
        title=request.POST.get('title')

        myclient = pymongo.MongoClient("mongodb+srv://admin-parag:test123@cluster0.gq3uj.mongodb.net/test")
        mydb = myclient['scrap_data']
        mycol = mydb["case_studies"]

        result = mycol.find({'title': re.compile(title, re.IGNORECASE)})

        if result.count()==0:
            return render(request,"no_case_study.html")

        data = dict({'results': result})

        return render(request,"view_case_study.html",data)
    return render(request,"404.html")

def handler404(request, *args, **argv):
    return render(request,"404.html")
