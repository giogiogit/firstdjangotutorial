from django.http import HttpResponse
from django.http import Http404
#from django.template import loader
# replaced by
from django.shortcuts import render
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
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album': album})