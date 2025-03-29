# src/main.py
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

from ui_main import MainWindow
import youtube_helper

class MusicApp(MainWindow):
    def __init__(self):
        super().__init__()
        # Inicializa o player do PyQt5
        self.player = QMediaPlayer()
        # Conecta os sinais dos botões da UI aos métodos
        self.search_button.clicked.connect(self.perform_search)
        self.results_list.itemDoubleClicked.connect(self.select_track)
        self.play_button.clicked.connect(self.play_track)
        self.pause_button.clicked.connect(self.pause_track)
        self.stop_button.clicked.connect(self.stop_track)
        # Armazena informações da música selecionada
        self.current_track_info = None

    def perform_search(self):
        query = self.search_bar.text().strip()
        if not query:
            QMessageBox.warning(self, "Atenção", "Digite um termo para pesquisar.")
            return
        self.results_list.clear()
        results = youtube_helper.search_youtube(query)
        self.search_results = results  # Guardamos para uso posterior
        for item in results:
            # Exibindo título e, se disponível, o canal ou outra info
            title = item.get('title', 'Sem título')
            self.results_list.addItem(title)

    def select_track(self, item):
        index = self.results_list.currentRow()
        track_info = self.search_results[index]
        video_url = track_info.get('webpage_url')
        audio_url, full_info = youtube_helper.get_audio_url(video_url)
        self.current_track_info = full_info
        # Atualiza o label com informações da música
        title = full_info.get('title', 'Desconhecido')
        self.track_info_label.setText(f"Tocando: {title}")
        # Define a mídia a ser reproduzida
        self.player.setMedia(QMediaContent(QUrl(audio_url)))
        # Inicia a reprodução

    def play_track(self):
        self.player.play()

    def pause_track(self):
        self.player.pause()

    def stop_track(self):
        self.player.stop()
        self.track_info_label.setText("Nenhuma música tocando")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MusicApp()
    window.show()
    sys.exit(app.exec_())
