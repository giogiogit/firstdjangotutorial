from django.shortcuts import render, get_object_or_404
from .models import Album

def index(request):
# as explaind in video 12/14 will be replaced by templates
#    all_albums = Album.objects.all()
#    html = ''
#    for album in all_albums:
#        url = '/music/' + str(album.id) + '/'
#        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)
#    template = loader.get_template('music/index.html')
#    context = {'all_albums': all_albums}
#    return HttpResponse(template.render(context, request))

def detail(request, album_id):
#    return HttpResponse("<h2>Details for Album id: " + str(album_id) + " </h2>")
    album = get_object_or_404(Album,pk=album_id)
    return render(request, 'music/detail.html', {'album': album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})