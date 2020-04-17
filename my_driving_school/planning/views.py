from django.shortcuts import render

def planning_index(request): 
    return render(request, 'planning/planning_index.html')

