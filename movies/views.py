from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("movies app is live")
    # list of variables
    context = {
        'movies':['gladiator','top gun','bahubali','Kalki']

    }
    return render(request,'movies/index.html',context)

def about(request):
    return render(request,'movies/about.html',{})
