from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .forms import LoginForm, RegistrationForm, AddGameForm
from django.contrib.sessions.models import Session
from authtest.models import CustomUser, Games, PurchasedGame
import datetime
from django.views.decorators.clickjacking import xframe_options_exempt
from hashlib import md5

@xframe_options_exempt
def index(request):
    if request.session.session_key != None :
        session_key = request.session.session_key
        session = Session.objects.get(session_key=session_key)
        uid = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=uid)
        
        if user.customuser.status == 1:
            return HttpResponseRedirect(reverse('developerhome'))
        else:
            return HttpResponseRedirect(reverse('playerhome'))

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            #process data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.customuser.status == 1:
                    login(request, user)
                    return HttpResponseRedirect(reverse('developerhome'))
                else:
                    login(request, user)
                    return HttpResponseRedirect(reverse('playerhome'))
                
            else:
                #if (request.session.session_key == None):
                return HttpResponse("user is not authenticated")
        else:
            return HttpResponse("form is not valid")
    form = LoginForm()
    return render(request, 'authtest/login.html', {'form': form})
@xframe_options_exempt
def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirmPassword = form.cleaned_data['confirmPassword']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            status = form.cleaned_data['status']
            user = User.objects.create_user(username, email, password)
            c = CustomUser(user = user, status = int(status))
            c.save()
            return render(request, 'authtest/registration.html', {'form':form, 'flag':True})
            
    form = RegistrationForm()
    return render(request, 'authtest/registration.html', {'form':form})

def addgame(request):
    session_key = request.session.session_key
    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(pk=uid)
    developer = CustomUser.objects.get(user=user)
    form = AddGameForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        category = form.cleaned_data['category']
        price = form.cleaned_data['price']
        url = form.cleaned_data['url']
        imagepath = form.cleaned_data['imagepath']
        description = form.cleaned_data['description']
        game = Games(name=name, category=category, price=price, url=url, developer = developer, image_path=imagepath, description = description)
        game.save()
        return render(request, 'authtest/addgame.html', {'form':form, 'flag': True})
    else:
        return render(request, 'authtest/addgame.html', {'form':form, 'formFlag': False})
        
    form = AddGameForm()
    return render(request, 'authtest/addgame.html', {'form':form})
def deletegame(request, game_id):
    game = Games.objects.get(pk=game_id)
    game.delete()
    return HttpResponseRedirect(reverse('developerhome'))
def editgame(request, game_id):
    game = Games.objects.get(pk=game_id)
    if request.method=="POST":
        game.name = request.POST.get('name')
        game.category = request.POST.get('category')
        game.price = request.POST.get('price')
        game.url = request.POST.get('url')
        game.image_path = request.POST.get('imagepath')
        game.description = request.POST.get('description')
        game.save()
        return render(request, 'authtest/editgame.html', {'flag':True})
    return render(request, 'authtest/editgame.html', {'game':game})
def allgames(request):
    games = Games.objects.all()
    return render(request, 'authtest/allgames.html', {'games':games})
@xframe_options_exempt
def developerhome(request):
    session_key = request.session.session_key
    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(pk=uid)
    developer = CustomUser.objects.get(user=user)
    games = Games.objects.filter(developer = developer)
    return render(request, 'authtest/developerhome.html', {'games':games})

@xframe_options_exempt
def playerhome(request):
    session_key = request.session.session_key
    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(pk=uid)
    player = CustomUser.objects.get(user=user)
    games = Games.objects.all()
    deleted = []
    for g in games:
        if PurchasedGame.objects.filter(game = g, player = player).exists():
            games = games.exclude(id=g.id)
    if request.method == "POST":
        pid = request.POST.get('pid')
        sid = request.POST.get('sid')
        amount = request.POST.get('amount')
        secret_key = request.POST.get('token')
        checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, secret_key)
        m = md5(checksumstr.encode("ascii"))
        checksum = m.hexdigest()
        return JsonResponse({'checksum':checksum})
    return render(request, 'authtest/playerhometest.html', {'games':games, 'user':user})
def searchresults(request):
    games = Games.objects.all()
    session_key = request.session.session_key
    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(pk=uid)
    player = CustomUser.objects.get(user=user)
    if request.method=="POST":
        search = request.POST.get('search')
        cat = request.POST.get('cat')
        if cat=='all':
            games = Games.objects.filter(name__contains=search)
            for g in games:
                if PurchasedGame.objects.filter(game = g, player = player).exists():
                    games = games.exclude(id=g.id)
            return render(request, 'authtest/searchresults.html', {'games':games})
        else:
            games = Games.objects.filter(name__contains=search, category=cat)
            for g in games:
                if PurchasedGame.objects.filter(game = g, player = player).exists():
                    games = games.exclude(id=g.id)
    return render(request, 'authtest/searchresults.html', {'games':games})
        

@xframe_options_exempt   
def mygames(request):
    session_key = request.session.session_key
    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(pk=uid)
    player = CustomUser.objects.get(user=user)
    boughtGames = PurchasedGame.objects.filter(player = player)
    return render(request, 'authtest/mygamestest.html', {'boughtGames':boughtGames, 'user':user})

@xframe_options_exempt
def gameplay(request, game_id):
    session_key = request.session.session_key
    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(pk=uid)
    player = CustomUser.objects.get(user=user)
    game = Games.objects.get(pk=game_id)
    playGame = PurchasedGame.objects.get(player=player, game=game)
    hscores = PurchasedGame.objects.filter(game=game).order_by('-highScore')
    if request.method == "POST":
        requestType = request.POST.get('type')
        if (requestType == "SCORE"):
            score = request.POST.get('score')
            playGame.score = int(score)
            if playGame.highScore < int(score):
                playGame.highScore = int(score)
            playGame.save()
                
            return JsonResponse({'success':'success'})
        else:
            score = request.POST.get('score')
            gameState = request.POST.get('gameState')
            playGame.score = int(score)
            playGame.gameState = gameState;
            if playGame.highScore < int(score):
                playGame.highScore = int(score)
            playGame.save()
            return JsonRespone({'success':'success'})
    return render(request, 'authtest/gameplay.html', {'game':playGame,'hscores':hscores})

def success(request, game_id):
        session_key = request.session.session_key
        session = Session.objects.get(session_key=session_key)
        uid = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=uid)
        gameID = game_id
        game = Games.objects.get(pk=gameID)
        game.salesCount = game.salesCount + 1
        game.save()
        date_time = datetime.datetime.now()
        player = CustomUser.objects.get(user=user)
        boughtGame = PurchasedGame(player = player, game = game, time_of_purchase = date_time)
        boughtGame.save()
        return HttpResponseRedirect(reverse('mygames'))

def error(request, game_id):
    return HttpResponse("game failed")

def cancel(request, game_id):
    return HttpResponseRedirect(reverse('playerhome'))
    
@xframe_options_exempt
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


    
