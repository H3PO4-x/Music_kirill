
from django.shortcuts import render,redirect
from .forms import GenreForm,TrackForm
from .models import Genre
from django.http import HttpResponseRedirect,HttpResponse
from .models import Track
def index (request):
    return render (request,'index.html', {'page':'main'})

  
def music (request):
    genres = Genre.objects.all() 
    return render(request, 'genres.html', {'genres': genres, 'page': 'genres'})

def track (request):
    trackes = Track.objects.all()
    genres = Genre.objects.all()
    return render(request, 'track.html', {'trackes': trackes, 'genres': genres, 'page': 'trackes'})

def deleteop(request,id_genres):
    genres = Genre.objects.get(id=id_genres)
    genres.delete()
    return HttpResponse('<h1>Жанр успешно удален</h1><br><a href="/">На главную</a>')


def add_genre (request):
    if request.method =="POST":
        name_ru = request.POST.get("name_ru")
        name_en = request.POST.get("name_en")``
        desc = request.POST.get("description")
        genre = Genre()
        genre.name_ru=name_ru
        genre.name_en=name_en
        genre.description=desc
        genre.save()
        return redirect ('/genres')
    else: 
        genreform = GenreForm()
        return render(request, "add_genre.html",{'form':genreform})

def edit_genre (request,id_genre):
    g = Genre.objects.get(id=id_genre)
    if request.method =="POST":
        genre = GenreForm(request.POST,instance=g)
        if genre.is_valid():
            genre.save()
        
        return redirect ('/genres')
    else: 
        genreform = GenreForm(instance=g)
        return render(request, "edit_genre.html",{'form':genreform})

def deletetrack(request,id_track):
    track = Track.objects.get(id=id_track)
    track.delete()
    return HttpResponse('<h1>Трек успешно удален</h1><br><a href="/">На главную</a>')


    
def edit_track (request,id_track):
    g = Track.objects.get(id=id_track)
    if request.method =="POST":
        track = TrackForm(request.POST,instance=g)
        if track.is_valid():
            track.save()
        
        return redirect ('/track')
    else: 
        trackform = TrackForm(instance=g)
        return render(request, "add_track.html",{'form':trackform})

def add_track(request):
   
    if request.method == "POST":
        
        track = TrackForm(request.POST)
        if track.is_valid():
            track.save()
        return redirect('/track')
    
    else:
        trackform = TrackForm()
        return render(request, "add_track.html", {'form': trackform})