from json import dumps
from tennis_app.models import gamePlayer
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    #context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    # player = list(gamePlayer.objects.all())
    # player_list = []
    #
    # for p in player:
    #     player_list.append({'Game Players': p.name})

    # context_dict = {'Game Players': gamePlayer_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    # return render_to_response('tennis_app/index.html', context_dict, context)
    return render(request, "tennis_app/index.html")


# def ajax(request):
#
#     if request.method == "POST":
#         player = gamePlayer()
#         player.name = request.POST["name"]
#         player.save()
#
#
#     player = list(gamePlayer.objects.all())
#     player_list = []
#     for p in player:
#         player_list.append({"name": p.name})
#
#     return HttpResponse(dumps(player_list, indent=4), content_type="application/json")
#
# def dom(request):
#     if request.method == "POST":
#         print request.POST

    #return render(request, 'tennis_app/dom.html')

def register(request):
    if request.method == "POST":
        User.objects.create_user(request.POST["username"], None, request.POST["password"])
    return render(request, 'tennis_app/index.html')

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST["username"],
                                 password=request.POST["password"])

        if user is not None:
            #the password verified for the user
            if user.is_active:
                print("User is vaid, active and authenticated")
                return redirect('/tennis_app/')
            else:
                print("The password is valid, but the account has been disabled!")

        else:
            print("The username and password")
    return render(request, 'tennis_app/index.html')

