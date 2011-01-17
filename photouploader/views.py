from django.shortcuts import render_to_response
from photouploader.models import Photo

def preview(request,token):
    # should shrink image before displaying it back to the user (using PIL)
    p = Photo.objects.get(receipt=token)
    
    if request.method == 'GET':
        if 'lat' in request.GET and 'long' in request.GET:
            p.latitude = request.GET['lat']
            p.longitude = request.GET['long']
            p.save()
    
    return render_to_response('preview.html',{'photo':p})
