from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from .forms import UserForm,CustomerForm
import services
import config

def home(request):
    form = CustomerForm()
    if request.method == 'GET':
        return render(request,'first_app/home.html',context={'form':form})
    elif request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            gender = form.cleaned_data['gender']
            symptoms_list = services.DiagnosisClient(config.username,config.password,config.authorization,config.language,config.health).loadSymptoms()
            symptoms_dict = {'access_symptoms':symptoms_list,'name':name,'gend':gender}
            return render(request,'first_app/symptoms.html',context=symptoms_dict)

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'first_app/index.html',context=date_dict)
# Create your views here.

def symptoms(request):
    symptoms_list = services.DiagnosisClient(config.username,config.password,config.authorization,config.language,config.health).loadSymptoms()
    symptoms_dict = {'access_symptoms':symptoms_list}
    return render(request,'first_app/symptoms.html',context=symptoms_dict)

def medical_conditions(request,id,gender):
    issues_list = services.DiagnosisClient(config.username,config.password,config.authorization,config.language,config.health).loadDiagnosis([id],gender,1998)
    issues_dict = {'access_issues':issues_list}
    print(issues_list)
    print("Hello")
    # print(symptom_issues_list)
    return render(request,'first_app/issues.html',context=issues_dict)

def search(request):
    if request.method == 'POST':
        search_id = request.POST
        print(search_id)
        symptoms_list = services.DiagnosisClient(config.username,config.password,config.authorization,config.language,config.health).loadSymptoms()
        for i in symptoms_list:
            if i[Name]==search_id:
                symptoms_dict={'access_symptoms':list(i)}
                return render(request,'first_app/symptoms.html',context=symptoms_dict)
    else:
        return render(request, 'forms.html')
def NewUser(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            webpages_list = AccessRecord.objects.order_by('date')
            date_dict = {'access_records':webpages_list}
            return render(request,'first_app/index.html',context=date_dict)
        else:
            print("Form invalid")
    return render(request,'first_app/forms.html',context={'form':form})
