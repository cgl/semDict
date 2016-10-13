from django.shortcuts import render
from semDict.models import Token

def token_list(request):
    tokens = Token.objects.all()
    return render(request, 'semDict/token_list.html', {'tokens' : tokens,
                                                       'flag': True})
