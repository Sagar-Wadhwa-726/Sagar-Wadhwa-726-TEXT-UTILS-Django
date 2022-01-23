import requests
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    info = {
        'name': 'Sagar',
        'place': 'mars'
    }
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('user_text', 'default')
    removepunc = request.POST.get('removepunc', 'False')
    toupper = request.POST.get('toupper', 'False')
    newlineremover = request.POST.get('newlineremover', 'False')
    extraspaceremover = request.POST.get('extraspaceremover', 'False')
    charcounter = request.POST.get('charcounter', 'False')

    # logic for removing the punctuations from the entered text

    analyzed = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {
            'purpose': 'Removed Punctuations',
            'analyzedtext': analyzed
        }

        return render(request, 'analyze2.html', params)

    elif toupper == "on":
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {
            'purpose': 'Convert To Upper Case',
            'analyzedtext': analyzed
        }

        return render(request, 'analyze2.html', params)

    elif newlineremover == "on":
        for char in djtext:
            if char != '\n' and char != '\r' :
                analyzed = analyzed + char

        params = {
            'purpose': 'Removed New Lines',
            'analyzedtext': analyzed
        }

        return render(request, 'analyze2.html', params)

    elif extraspaceremover == "on":
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {
            'purpose': 'Removed Extra Spaces',
            'analyzedtext': analyzed
        }

        return render(request, 'analyze2.html', params)

    elif charcounter == "on":
        count = 0
        for i in range(0, len(djtext)):
            if djtext[i] != '\n' and djtext[i] != '':
                count = count + 1
            else:
                pass

        params = {
            'purpose': 'Character Count',
            'analyzedtext': analyzed,
            'count': count
        }

        return render(request, 'count.html', params)

    else:
        return render(request,"error.html")


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
