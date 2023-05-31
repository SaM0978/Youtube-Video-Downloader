from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os

def youtube_download(link):
    try:
        from pytube import YouTube

        yt = YouTube(link)

        video = yt.streams.get_highest_resolution()
        os.chdir('/workspaces/codespaces-blank/youtube_downloader/media')
        video.download()
        
        return yt.title
    except Exception as e:
        print(e)
        return 'Enter The Correct Url'

def index(request):
    return render(request, 'main/index.html')

@csrf_exempt
def success(request):
    user_url = request.POST.get('url')
    name = youtube_download(user_url)
    name = name + '.mp4'
    if '|' in name:
        name = name.replace('|', '')
    print(user_url, name)
    if name == 'Enter The Correct Url':
        return render(request, 'main/error.html')
    else:
        return render(request, 'main/success.html', {"name": name})