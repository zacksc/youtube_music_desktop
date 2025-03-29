# src/youtube_helper.py
from yt_dlp import YoutubeDL

def search_youtube(query, max_results=5):
    search_query = f"ytsearch{max_results}:{query}"
    ydl_opts = {'quiet': True, 'skip_download': True}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_query, download=False)
    return info.get('entries', [])

def get_audio_url(video_url):
    ydl_opts = {
        'quiet': True,
        'format': 'bestaudio/best',
        'skip_download': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        return info.get('url'), info
