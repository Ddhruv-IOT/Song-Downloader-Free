import os
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import QApplication, QMainWindow, QListView, QPushButton, QVBoxLayout, QWidget

def get_music_files(folder_path):
    music_extensions = (".mp3", ".wav", ".flac", ".ogg", ".aac")
    music_files = [file for file in os.listdir(folder_path) if file.lower().endswith(music_extensions)]
    return music_files

class MusicListWindow(QMainWindow):
    def __init__(self, music_files):
        super().__init__()

        self.setWindowTitle("Music Files in Folder")
        self.setGeometry(300, 300, 800, 800)
        self.music_files = music_files
        
        # model = QStringListModel(self.music_files)

        # self.music_list_view = QListView(self)
        # self.music_list_view.setModel(model)
        # self.setCentralWidget(self.music_list_view)
        
        self.model = QStringListModel(self.music_files)

        self.music_list_view = QListView(self)
        self.music_list_view.setModel(self.model)
        self.music_list_view.setDragDropMode(QListView.InternalMove)

        save_button = QPushButton("Save", self)
        save_button.clicked.connect(self.save_music_order)

        layout = QVBoxLayout()
        layout.addWidget(self.music_list_view)
        layout.addWidget(save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def save_music_order(self):
        updated_music_files = [f"{i + 1}_{song}" for i, song in enumerate(self.music_files)]
        with open("music_order.txt", "w") as f:
            f.write("\n".join(updated_music_files))

if __name__ == "__main__":
    folder_path = "./z2"  # Replace with the actual path to your music folder

    app = QApplication(sys.argv)

    music_files = get_music_files(folder_path)

    window = MusicListWindow(music_files)
    window.show()

    sys.exit(app.exec_())
