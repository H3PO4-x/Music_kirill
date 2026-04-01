
from django.shortcuts import render,redirect
from .forms import GenreForm,TrackForm,ArtistForm
from .models import Genre,Artist
from django.http import HttpResponseRedirect,HttpResponse
from .models import Track
def index (request):
    return render (request,'index.html', {'page':'main'})

  
def music (request):
    genres = Genre.objects.all() 
    return render(request, 'genres.html', {'genres': genres, 'page': 'genres'})

def track (request):
    tracks = Track.objects.all() 
    artists = Artist.objects.all()
    artist = None
    if request.method == "POST":
        id_artist = request.POST.get('artist')
        artist = Artist.objects.get(id=id_artist)
        tracks = Track.objects.filter(artist=artist)
    return render(request, 'track.html', {'tracks': tracks, 'artists':artists, 'current_artist': artist, 'page': 'tracks'})

def deleteop(request,id_genres):
    genres = Genre.objects.get(id=id_genres)
    genres.delete()
    return HttpResponse('<h1>Жанр успешно удален</h1><br><a href="/">На главную</a>')


def add_genre (request):
    if request.method =="POST":
        name_ru = request.POST.get("name_ru")
        name_en = request.POST.get("name_en")
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


def artists(request):
    a=Artist.objects.all()
    return render(request,'artists.html',{'artists':a})



def deleteartist(request, id):
    artist = Artist.objects.get(id=id_artist)
  
    Track.objects.filter(artist=artist).delete()
    
    artist.delete()
    return redirect('artists')  

def add_artist(request):
    if request.method == "POST":
        name = request.POST.get("name")
        image = request.POST.get("image")
        artist=Artist()
        artist.name = name
        artist.image = image
        artist.save()
        return redirect('/genres')
    else:
        artistform = ArtistForm()
        return render(request, "add_artist.html", {'form':artistform})

