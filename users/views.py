from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from .models import AuthUser, pcGuid, pcGuidLog, Visuallog, tbUsername, jdUsername, real_name,blacklistlog
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm, tbForm, jdForm
from cryapp.models import CryOrder
from goods.models import Goods
from financial.models import deposit
from cryapp.views import authenticationlogin
# Create your views here.

@login_required
def seller(request):
    '''sellerindex'''
    return render(request, 'index/index.html')

@login_required
def logout(request):
    '''注销登录'''
    auth.logout(request)
    return redirect('login')

def AuUserlogin(request):
    authen = request.user.is_authenticated()
    if authen == False:
        return render(request, 'login.html')
        pass


class RegisterView(View):
    template_name = 'register.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name)
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            return render(request, 'register.html', {"msg": "密码两次输入不一致"})

        user_profile = AuthUser()
        user_profile.username = username
        # user_profile.email = username
        user_profile.password = make_password(password)
        user_profile.is_active = True
        user_profile.save()
        createdeposit = deposit.objects.create(user=user_profile, deposit=0)
        createdeposit.save()
        return redirect('login')
class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, "login.html", {"login_form": form})

        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST.get('cpuid'))
        print(request.POST.get('visual'))
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('buyerindex')
        else:
            return render(request, 'login.html', {'msg': '账号密码错误'})


##pc hardware insert
def PcHardwareInsert(request):
    if request.method == 'GET':
        return render(request, 'users/usersRequest.html', {'usersRequest':1});
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'users/usersRequest.html', {'usersRequest':form});
        #get hardVisual
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpuid = request.POST.get('cpuid')
        visual = int(request.POST.get('visual'))
        diskid = request.POST.get('diskid')
        biosid = request.POST.get('biosid')
        boardid = request.POST.get('boardid')
        hardkey = int(request.POST.get('hardkey'))
        print(hardkey)
        #get hardVisual
        ### down get ip###
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        ###above get ip###
        #-------return add rules ------------#

        #next authuser
        user = auth.authenticate(username=username, password=password)
        usersRequest = ''
        if user is not None:
            usersRequest = 'usernamehave'
            auth.login(request, user)
            #visual rules
            if visual == 1:
                user = AuthUser.objects.get(username=username)
                visuallog = Visuallog.objects.create(user=user, resip=ip)
                Visuallog.save()
                BlackListUpdate = AuthUser.objects.update(username=user, is_blacklist=1)
                BlackListUpdate.save()
                usersRequest = 1
                return render(request, 'users/usersRequest.html', {'usersRequest':usersRequest});
            else:
                user = AuthUser.objects.get(username=username)
                usersRequest = 1
                try:
                    pcguidTurn = pcGuid.objects.get(PcGuid=hardkey, user=user)
                    pcGuidLogturn =pcGuidLog.objects.create(user=user, PcGuid=pcguidTurn, resip=ip)
                    pcGuidLogturn.save()
                except:
                    savehard = pcGuid.objects.create(user=user, PcGuid=hardkey, cpuid=cpuid, diskid=diskid, boardid=boardid, biosid=biosid, resip=ip)
                    savehard.save()
                    pcguidTurn = pcGuid.objects.get(PcGuid=hardkey)
                    pcGuidLogturn = pcGuidLog.objects.create(user=user, PcGuid=pcguidTurn, resip=ip)
                    pcGuidLogturn.save()

            return render(request, 'users/usersRequest.html', {'usersRequest':usersRequest});
        else:
            usersRequest = 0
            return render(request, 'users/usersRequest.html', {'usersRequest':usersRequest});


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



#--------- tb 1688 -----#
def tb(request):
    authenticationlogin_def = authenticationlogin(request)
    if not authenticationlogin_def is None:
        return authenticationlogin_def
    if request.method == 'GET':
        pass
    elif request.method == "POST":
        form = tbForm(request.POST)
        if not form.is_valid():
            return render(request, 'users/usersRequest.html', {'usersRequest':form});
        selecttbid = tbUsername.objects.filter(tbUsername=request.POST['tbusername'])
        if len(selecttbid.values()) > 0:
            blacklistlogsave = blacklistlog.objects.create(user=request.user, resip=get_client_ip(request), Remarks ='tbiderror:'+ request.POST['tbusername'])
            blacklistlogsave.save()
            return render(request, 'users/usersRequest.html', {'usersRequest':'ID exist'});
        createtbid = tbUsername.objects.create(user = request.user, tbUsername = request.POST['tbusername'])
        createtbid.save()
        return redirect('/cryapp/buyer/users/')

def jd(request):
    authenticationlogin_def = authenticationlogin(request)
    if not authenticationlogin_def is None:
        return authenticationlogin_def
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        form = jdForm(request.POST)
        if not form.is_valid():
            return render(request, 'users/usersRequest.html', {'usersRequest':form});
        selecttbid = jdUsername.objects.filter(jdUsername=request.POST['jdusername'])
        if len(selecttbid.values()) > 0:
            blacklistlogsave = blacklistlog.objects.create(user=request.user, resip=get_client_ip(request), Remarks ='jdiderror:'+ request.POST['jdusername'])
            blacklistlogsave.save()
            return render(request, 'users/usersRequest.html', {'usersRequest':'ID exist'});
        createjdid = jdUsername.objects.create(user = request.user, jdUsername = request.POST['jdusername'])
        createjdid.save()
        return redirect('/cryapp/buyer/users/')