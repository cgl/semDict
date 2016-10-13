from django.shortcuts import render

def token_list(request):
    return render(request, 'semDict/token_list.html', {})
