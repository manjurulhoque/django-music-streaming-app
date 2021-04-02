from __future__ import unicode_literals

import math
import os
from time import strftime

from celery import shared_task
from django.conf import settings
import youtube_dl
from youtube_dl.utils import format_bytes

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music.settings')

# from celery import task

MEDIA_ROOT = settings.MEDIA_ROOT
MEDIA_FOLDER = settings.MEDIA_FOLDER


def file_size(size):
    if size == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size, 1024)))
    p = math.pow(1024, i)
    s = round(size / p, 2)
    return "%s %s" % (s, size_name[i])


def size_human(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def progress_hook_video(pr):
    print(pr)
    if pr['status'] == 'finished':
        print('finished')
    else:
        prgstr = 'Getting Video ' + str(round(pr['downloaded_bytes'] / (pr['total_bytes'] / 100))) + '% (' + size_human(pr['downloaded_bytes']) + '/' + size_human(pr['total_bytes']) + ')'


@shared_task
def download_audio_from_youtube(video_url):
    # Mp3 format options
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{MEDIA_ROOT}/songs/{strftime("%Y/%m/%d")}/%(title)s.mp3',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [progress_hook_video]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as yld:
        # yld.add_progress_hook(progress_hook_video)
        file_data = yld.extract_info(video_url, download=True)
        print(file_data)
        title = file_data["title"]
        url = f'{MEDIA_ROOT}/songs/{strftime("%Y/%m/%d")}/{title}.mp3'
        url = f"/{MEDIA_FOLDER}{url.split(MEDIA_ROOT)[1]}"
        # for f in file_data['formats']:
        #     print(format_bytes(f['filesize']))
        size = file_data['formats'][0]['filesize']
        description = file_data.get('description', '')

    return title, url, file_size(size), description

# print(download_audio_from_youtube('https://www.youtube.com/watch?v=TQR70KKYMmQ&ab_channel=PopChartbusters'))
