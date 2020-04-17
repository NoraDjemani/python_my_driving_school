from django.shortcuts import render


def forfait_index(request): 
    return render(request, 'forfait/forfait_index.html')

