from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import render,get_object_or_404
from django.template.context_processors import request, csrf
from django.http import Http404,HttpResponseRedirect
from .models import AllUser
from django.contrib.sessions.models import Session
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect



global userid,usertype,userspec
userid,usertype,userspec="","",""
# Create your views here.
def index(request):

    return render(request, 'login/index.html', {"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})

def login(request):
    return render(request, 'login/login.html', {})

def logout(request):
    request.session['userid']=""
    request.session['usertype']=""
    request.session['userspec']=""
    return render(request, 'login/index.html', {"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})

def auth_view(request):
    
    username = request.POST['username']
    password = request.POST['pwd']
    type_label = request.POST['sel1']
    try:
        user = AllUser.objects.get(username=username,password=password,type_label=type_label)
        #str(AllUser.getSpec(user))
        if user is not None:
            request.session['userid']=str(user)
            request.session['usertype']=AllUser.getType(user)
            request.session['userspec']=AllUser.getSpec(user)
            return redirect('login:index')
        #return HttpResponseRedirect('')
    except AllUser.DoesNotExist:
        a=[]
        a.append('INAVLID ID OR PASSWORD')
        return render(request, 'login/login.html', {"error":'Invalid Input'})
    
    
  
