from django.shortcuts import render




def Home_view(request):
    return render(request,"index.html")