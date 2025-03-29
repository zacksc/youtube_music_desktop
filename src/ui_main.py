# src/ui_main.py
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QLineEdit,
    QPushButton, QListWidget, QLabel
)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Youtube Music Desktop")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        layout = QVBoxLayout()

        # Barra de busca
        search_layout = QHBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Pesquisar música...")
        self.search_button = QPushButton("Buscar")
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.search_button)
        layout.addLayout(search_layout)

        # Lista de resultados
        self.results_list = QListWidget()
        layout.addWidget(self.results_list)

        # Seção de reprodução
        controls_layout = QHBoxLayout()
        self.play_button = QPushButton("Play")
        self.pause_button = QPushButton("Pause")
        self.stop_button = QPushButton("Stop")
        controls_layout.addWidget(self.play_button)
        controls_layout.addWidget(self.pause_button)
        controls_layout.addWidget(self.stop_button)
        layout.addLayout(controls_layout)

        # Exibição da música atual
        self.track_info_label = QLabel("Nenhuma música tocando")
        self.track_info_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.track_info_label)

        central_widget.setLayout(layout)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
