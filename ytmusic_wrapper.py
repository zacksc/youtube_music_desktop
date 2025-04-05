import webview
import sys
import time
import threading
import json

YOUTUBE_MUSIC_URL = "https://music.youtube.com"

current_track_info = {"title": None, "artist": None}
window_ready = False

def get_track_info(window):
    global window_ready
    if not window_ready:
        return None
    try:
        js_code = """
            (function(){
                try{
                    var titleElement = document.querySelector('ytmusic-player-bar .title');
                    var artistElement = document.querySelector('ytmusic-player-bar .byline a.yt-simple-endpoint');
                    var artworkElement = document.querySelector('ytmusic-player-bar img.image');

                    var title = null;
                    if (titleElement){
                        title = titleElement.getAttribute('title');
                        if (!title || title.trim() === ''){
                            title = titleElement.innerText;
                        }
                    }
                    
                    var artist = artistElement ? artistElement.innerText : null;
                    var artworkUrl = artworkElement ? artworkElement.src : null;

                    return JSON.stringify({
                        'title': title ? title.trim() : null,
                        'artist': artist ? artist.trim() : null,
                        'artwork': artworkUrl,
                        'error': null
                    });
                } catch (e) {
                    return JSON.stringify({'error': e.toString()});
                }
            })();
                """
        
        result_json = window.evaluate_js(js_code)

        if result_json:
            data = json.loads(result_json)
            if data.get('error') is None:
                if data.get('title'):
                    return data
                else:
                    print("JS Executado, mas título não encontrado.")
                    return None
            else:
                print(f"JS Error {data['error']}")
                return None
            return None
    except Exception as e:
            print(f"Python Error evaluating JS: {e}")
            return None

def update_title_periodically(window):
    global current_track_info
    while True:
        track_info = get_track_info(window)
        if track_info != current_track_info:
            if track_info and track_info.get('title'):
                current_track_info = track_info
                title = track_info.get('title', '')
                artist = track_info.get('artist', '')
                new_window_title = f"{title} - {artist} | YT Music"
                print(f"Música atualizada: {title} - {artist}")
                try:
                    window.set_title(new_window_title)
                except Exception as e:
                    print(f"Error setting title {e}")

        time.sleep(5)

def on_loaded():
    global window_ready
    print(">>> Página carregada, JS habilitado.")
    window_ready = True

def on_closing():
    global window_ready
    print(">>> Fechando aplicação...")
    window_ready = False


def main():
    print("Iniciando o Youtube Music...")
    try:
        window = webview.create_window(
            title="Youtube Music Desktop",
            url=YOUTUBE_MUSIC_URL,
            width=1000,
            height=700,
            resizable=True,
            confirm_close=True,
        )
        
        window.events.loaded += on_loaded
        window.events.closing += on_closing

        monitor_thread = threading.Thread(target=update_title_periodically, args=(window,), daemon=True)
        monitor_thread.start()
        print("Thread de monitoramento iniciada.")

        webview.start(debug=False)

        print("Aplicação fechada.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()