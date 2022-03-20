from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django .contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib import messages
from .models import TestResults

from .forms import RegisterForm

from business_services.rest_data import liza_retern_2_lists



def register_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')
    else:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                # group = Group.objects.get(name = 'customer')
                # user.groups.add(group)
                messages.success(request, "Вы успешно зарегистрировались под ником " + username)
                return redirect('accounts:login')
        context = {'form':form}
        return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('accounts:home')
            else:
                messages.info(request, 'Имя пользователя или пароль введены неверно.')
        context = {}
        return render(request, 'accounts/login.html', context)


@login_required(login_url = 'accounts:login')
def logout_view(request):
    logout(request)
    #request.user == Anon user
    return redirect('accounts:login')


@login_required(login_url = 'accounts:login')
def home(request):
    users_test_data = TestResults.objects.filter(author = request.user.pk).order_by('-created').first()
    if users_test_data:
        data = liza_retern_2_lists(
            users_test_data.investment_amount, 
            str(users_test_data.investment_horizon), 
            str(users_test_data.portfolio_type)
        )
        # print(data)
        list_akzii = data[0]
        list_oblig = data[1]

        l_akzii = []
        for i in range(len(list_akzii)):
            for j in range(len(list_akzii[i][1])):
                l_t = []
                l_t.append(list_akzii[i][0])
                l_t.append(list_akzii[i][1][j][0])
                l_t.append(list_akzii[i][1][j][1])
                l_t.append(list_akzii[i][1][j][2])
                l_t.append(round(list_akzii[i][1][j][3],4))
                l_t.append(round(list_akzii[i][1][j][4],4))
                l_akzii.append(l_t)

        l_oblig = []
        for i in range(len(list_oblig)):
            for j in range(len(list_oblig[i][1])):
                l_to = []
                l_to.append(list_oblig[i][0])
                l_to.append(list_oblig[i][1][j][0])
                l_to.append(list_oblig[i][1][j][1])
                l_to.append(list_oblig[i][1][j][2])
                l_to.append(list_oblig[i][1][j][3][:4])
                l_to.append(list_oblig[i][1][j][4])
                l_oblig.append(l_to)
        context = {
                    'datas_akzii':l_akzii,
                    'datas_oblig':l_oblig,
                    'user_data':users_test_data,
        }
        return render(request, 'accounts/home.html',context)
    else:
        context = {
            'user_data':None,
        }
        return render(request, 'accounts/home.html',context)


@login_required(login_url = 'accounts:login')
def quiz_page(request):
    if request.method=='POST':
        # print(request.POST)
        author=User.objects.get(username = request.user)
        portfolio_type=request.POST['q1']
        investment_horizon = request.POST['q2']
        amount_money = request.POST['sum_in_mounth']
        results = TestResults.objects.create(
                                    author=author,
                                    portfolio_type=portfolio_type,
                                    investment_horizon=investment_horizon,
                                    investment_amount = amount_money)
        return redirect('accounts:home')
    context={}
    return render(request, 'accounts/quiz.html', context)


@login_required(login_url = 'accounts:login')
def datalens_analytics(request):
    return render(request, 'accounts/datalens-analyze.html')


@login_required(login_url = 'accounts:login')
def support(request):
    return render(request, 'accounts/support.html')
